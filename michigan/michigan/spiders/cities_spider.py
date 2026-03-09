from pathlib import Path

import scrapy

class CitiesSpider(scrapy.Spider):
    name = "cities"

    async def start(self):
        urls = [
        'https://en.wikipedia.org/wiki/List_of_municipalities_in_Michigan'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        table = response.xpath('//table[@class="wikitable sortable"]//tr')
        for row in table:
            yield {
                "name": row.xpath('td[1]//text()').get(),
                "type": row.xpath('td[2]//text()').get(),
                "county": row.xpath('td[3]//text()').get(),
                "pop2020": row.xpath('td[4]//text()').get(),
                "change": row.xpath('td[6]//text()').get(),
                "area": row.xpath('td[8]//text()').get(),
                "density": row.xpath('td[9]//text()').get()
            }
