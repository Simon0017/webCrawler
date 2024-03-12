import scrapy


class SpidermanSpider(scrapy.Spider):
    name = "spiderman"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        pass
