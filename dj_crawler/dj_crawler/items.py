# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Project(scrapy.Item):
    # define the fields for your item here like:
    projectName = scrapy.Field()
    projectVersion = scrapy.Field()
    projectCreated = scrapy.Field()

