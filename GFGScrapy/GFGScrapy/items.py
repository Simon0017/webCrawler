# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import scrapy


class GfgscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class GfgItemloadersItem(scrapy):

    # scrape book price and title
    price = scrapy.Field()
    title = scrapy.Field()
