import scrapy
import csv
from ..items import HomeDepotItem


class HomeDepotSpider(scrapy.Spider):

    name = 'homeDepot'
    allowed_domains = ['homedepot.com']

    def start_requests(self):
        f = open("UPCTestFile.csv", "r")
        url_item = csv.reader(f)
        for row in url_item:
            for item in row:
                home_url = "https://www.homedepot.com/s/{" + item + "}"
                # print(home_url)
                yield scrapy.Request(home_url, callback=self.parse)
        f.close()

    def parse(self, response):   # self - references itself | response - source code of URLs we give the program
        items = HomeDepotItem()
        blank = ['']

        product = str.strip(response.css('.plp-pod__info a::text')[1].get())  # Displays product names #product-pod--ie-fix.product-pod__title__product.product-pod__title__product::text | .pod-plp__description a::text
        brand = response.css('span.pod-plp__brand-name::text').get()   # Displays brand of product
        price = "$" + response.css('.price__numbers::text, .price__format+ .price__format::text')[1].get() + "." + response.css('.price__numbers::text, .price__format+ .price__format::text')[2].get() # Displays product prices   .price__numbers   #.price-format__main-price span::text (gets prices without 'per package' or 'per box')

        if product == blank:
            product = ['This product is not sold at HomeDepot']

        items['homeDepot_item'] = product
        items['homeDepot_brand'] = brand
        items['homeDepot_price'] = price

        yield items

# Iterating through multiple pages
        # next_page = response.css('li.hd-pagination__item.hd-pagination__button a::attr(href)').get()
        #
        # if next_page == "/b/Hardware-Cabinet-Hardware-Drawer-Pulls/N-5yc1vZc29u?Nao=72":
        #     exit()
        # elif next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

# Trying to fill file with items not available
        #
        # na = str.strip(response.css('.results-nrf-hero__text::text')[1].get())
        # na1 = "Hmm...we couldn't find" This is what appears for na if the item is not there
        #
        # items['homeDepot_na'] = na

# Run with 'scrapy crawl homeDepot' or 'crawl homeDepot -o filename.filetype'
# Supports .json .csv .xml
# Displays product names #product-pod--ie-fix.product-pod__title__product.product-pod__title__product::text | .pod-plp__description a::text

