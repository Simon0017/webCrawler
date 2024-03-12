import scrapy
from ..items import GfgItemloadersItem

class GfgLoadbookdataSpider(scrapy.Spider):
    # name of spider 
    name = "gfg_loadbookdata"

    # domain to be scraped
    allowed_domains = ["books.toscrape.com"]

    # url to be scraped
    start_urls = ["https://books.toscrape.com/catalogue/category/books/womens-fiction_9"]

    # default parse callback method
    def parse(self, response):

        # create an object of an item class
        item  = GfgItemloadersItem()

        # loop thro' all the books
        for books in response.xpath('//*[@class="product_pod"]'):
            # xpath expression for that book price
            price = books.xpath('.//*[@class="product_price"]/p/text()').extract_first()

            # place price value in an item key
            item['price'] = price

            # Xpath expression for the book title
            title = books.xpath('.//h3/a/text()').extract()

            # place title value in item key
            item['title'] = title

            # yield the item
            yield item

      
