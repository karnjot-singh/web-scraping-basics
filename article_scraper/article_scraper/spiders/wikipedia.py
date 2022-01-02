import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from article_scraper.items import Article

class WikipediaSpider(CrawlSpider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Kevin_Bacon']

    custom_settings = {
        'FEED_URI': 'articles.xml',
        'FEED_FORMAT': 'xml'
    }

    rules = [Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse_info', follow=True)]
    def parse_info(self, response):
        article = Article()
        
        article['title'] = response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()').get()
        article['url'] = response.url
        article['lastUpdated'] = response.xpath('//li[@id="footer-info-lastmod"]/text()').get()

        return article
