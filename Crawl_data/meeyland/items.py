# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeeylandItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    number_of_bedrooms = scrapy.Field()
    price_per_metter = scrapy.Field()
    area = scrapy.Field()
    location = scrapy.Field()
    number_of_bathrooms = scrapy.Field()