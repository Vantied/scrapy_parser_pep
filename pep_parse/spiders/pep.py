import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        for category in response.css('#index-by-category section'):
            pep_links = category.css('a.pep::attr(href)').getall()

            for link in set(pep_links):
                yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        page_title = response.css('h1.page-title::text').get()
        if page_title:
            title_parts = page_title.split(' – ', 1)
            number = title_parts[0].replace('PEP ', '').strip()
            name = title_parts[1].strip() if len(title_parts) > 1 else ''
        else:
            number = ''
            name = ''

        status = response.xpath(
            '//dt[contains(., "Status")]'
            '/following-sibling::dd[1]//text()').get()

        yield PepParseItem(
            number=number,
            name=name,
            status=status.strip() if status else ''
        )
