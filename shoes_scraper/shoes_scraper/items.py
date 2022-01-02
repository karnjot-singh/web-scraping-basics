# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Shoe(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    productCode = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()
    color = scrapy.Field()
    rating = scrapy.Field()
    brand = scrapy.Field()
    currency = scrapy.Field()
