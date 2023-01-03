import scrapy
from dj_crawler.items import Project
from scrapy.loader import ItemLoader


class ToScrapeCSSSpider(scrapy.Spider):
    name = "djc"

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        urls = [
            'https://pypi.org/search/?&o=&c=Framework+%3A%3A+Django'

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,headers=headers)


    def parse(self, response):
        for project_element in response.css('[aria-label="Search results"] > li'):
            projectName = project_element.css('[class="package-snippet__name"]::text').get()
            projectVersion = project_element.css('[class="package-snippet__version"]::text').get()
            projectCreated = project_element.css('[class="package-snippet__created"]>time::text').get()
            next_page = response.css('[class="button-group button-group--pagination"]>a:last-child::attr(href)').get()

            newProject = Project(projectName=projectName,projectVersion=projectVersion,projectCreated=projectCreated)

            yield newProject

            if next_page:
                yield scrapy.Request(url=response.urljoin(next_page))




