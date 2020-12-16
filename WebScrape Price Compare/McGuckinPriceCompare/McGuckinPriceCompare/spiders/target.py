import scrapy
import csv
from ..items import TargetItem


class TargetSpider(scrapy.Spider):
    name = 'target'
    allowed_domains = ['target.com']

    def start_requests(self):
        f = open("UPCTestFile.csv", "r")
        url_item = csv.reader(f)
        for row in url_item:
            for item in row:
                target_url = "https://www.target.com/s?searchTerm=" + item
                print(target_url)
                yield scrapy.Request(target_url, callback=self.parse)
        f.close()

    def parse(self, response):
        items = TargetItem()

        product = response.css('.h-text-bs.flex-grow-one').get()  # Displays product names
        price = response.css('.fsAyjy .h-text-bs').get()  # Displays product prices

        items['target_item'] = product
        items['target_price'] = price

        yield items
