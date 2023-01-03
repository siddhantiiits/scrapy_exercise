# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import csv

class ProjectPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)
        if adapter.get('projectName') and adapter.get('projectVersion') and adapter.get('projectCreated'):
            print('Project Compatible')
            return item
        else:
            raise DropItem(f"Item not valid {item}")

class ToCSVPipeline:
    def process_item(self,item,spider):

        filename = "Django Projects.csv"

        adapter = ItemAdapter(item)
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([adapter.get('projectName'),adapter.get('projectVersion'),adapter.get('projectCreated')])

        return item


