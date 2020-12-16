import scrapy
import csv
from ..items import AmazonItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']

    def start_requests(self):
        f = open("UPCTestFile50.csv", "r")
        url_item = csv.reader(f)
        for row in url_item:
            for item in row:
                amazon_url = "https://www.amazon.com/s?k=" + item + "&ref=nb_sb_noss"
                print(amazon_url)
                yield scrapy.Request(amazon_url, callback=self.parse)
        f.close()

    def parse(self, response):
        items = AmazonItem()

        product = response.css('.a-color-base.a-text-normal::text').get()  # Displays product names
        price = "$" + response.css('.a-price-whole::text').get() + "." + response.css('.a-price-fraction::text').get()  # Displays product prices
        # upc = response.css('.a-price-whole').get()

        items['amazon_item'] = product
        items['amazon_price'] = price
        # items['amazon_upc'] = upc

        yield items