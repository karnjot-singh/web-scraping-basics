import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from shoes_scraper.items import Shoe
import json

class ReebokSpider(CrawlSpider):
    name = 'reebok'
    allowed_domains = ['www.reebok.ca']
    start_urls = ['https://www.reebok.ca/en/shoes']

    rules = [Rule(LinkExtractor(allow=r'en/.*-shoes/[A-Z0-9]{6}.html'), callback='parse_info', follow=True)]
    def parse_info(self, response):
        shoe = Shoe()

        shoe['url'] = response.url

        data = json.loads(response.xpath('//script[@data-rh="true"]/text()').get())
        shoe['brand'] = data['brand']['name']
        shoe['name'] = data['name']
        shoe['color'] = data['color']
        shoe['description'] = data['description']
        if 'aggregateRating' in data:
            shoe['rating'] = data['aggregateRating']['ratingValue']
        else: shoe['rating'] = None
        shoe['price'] = data['offers']['price']
        shoe['currency'] = data['offers']['priceCurrency']
        shoe['productCode'] = data['sku']

        shoe['category'] = response.xpath('//div[@data-auto-id="product-category"]/span/text()').get()

        return shoe
