import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from shoes_scraper.items import Shoe
import json

class SportChekSpider(CrawlSpider):
    name = 'sportChek'
    allowed_domains = ['www.sportchek.ca']
    start_urls = ['https://www.sportchek.ca/categories/men/footwear.all.html']  #categories/shop-by-sport/running/running-shoes/product/asics-mens-gel-excite-trail-running-shoes-color-333488429_01-333488429.html']

    rules = [Rule(LinkExtractor(allow=r'.*-shoes-[a-z]+\-[0-9]+\.html.*'), callback='parse_info', follow=True)]
    def parse_info(self, response):
        print("*********************\n*********************\n",response.url,"*********************\n*********************")
        shoe = Shoe()

        shoe['url'] = response.url

        data = json.loads(response.xpath('//script[@type="application/ld+json"]/text()').get())
        shoe['brand'] = data['brand']['name']
        shoe['name'] = data['name']
        shoe['color'] = data['color']
        shoe['description'] = data['description']
        if 'aggregateRating' in data:
            shoe['rating'] = data['aggregateRating']['ratingValue']
        else: shoe['rating'] = None
        shoe['price'] = data['offers'][0]['price']
        shoe['currency'] = data['offers'][0]['priceCurrency']
        shoe['productCode'] = data['sku']

        shoe['category'] = 'NA' #response.xpath('//a[@class="page-breadcrumb__link"]/span/text()').get()

        return shoe
