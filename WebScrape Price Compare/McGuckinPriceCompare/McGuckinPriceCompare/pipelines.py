# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# Scraped data -> Item Containers -> JSON file
from itemadapter import ItemAdapter


class AmazonPipeline:
    def process_item(self, item, spider):
        print("Pipeline :" + item['amazon_item'][0])
        print("Pipeline :" + item['amazon_price'][0])
        return item

class HomeDepotPipeline:
    def process_item(self, item, spider):
        print("Pipeline :" + item['homeDepot_item'][0])
        print("Pipeline :" + item['homeDepot_brand'][0])
        print("Pipeline :" + item['homeDepot_price'][0])
        return item

class TargetPipeline:
    def process_item(self, item, spider):
        print("Pipeline :" + item['target_item'][0])
        print("Pipeline :" + item['target_price'][0])
        return item
