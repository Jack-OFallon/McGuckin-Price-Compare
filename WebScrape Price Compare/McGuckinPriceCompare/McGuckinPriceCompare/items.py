# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#
# Set restrictions to only dump 400 - 500 items a day. Otherwise this IP will get blocked.

import scrapy


class AmazonItem(scrapy.Item):
    amazon_item = scrapy.Field()
    amazon_price = scrapy.Field()


class HomeDepotItem(scrapy.Item):
    homeDepot_item = scrapy.Field()
    homeDepot_brand = scrapy.Field()
    homeDepot_price = scrapy.Field()
    homeDepot_NA = scrapy.Field()


class TargetItem(scrapy.Item):
    target_item = scrapy.Field()
    target_price = scrapy.Field()
