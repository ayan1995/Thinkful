# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TechradarSpider(CrawlSpider):
    name = 'digtrends_S9'
    allowed_domains = ['www.digitaltrends.com']
    start_urls = ['https://www.digitaltrends.com/?s=Samsung+Galaxy+S9']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='m-list-river--title']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for texts in response.xpath("//div[@class='l-stardust-post--col-2']"):
            yield {
                'title': texts.xpath("//div[@class='l-stardust-post--col-2']/header[@class='m-stardust-title-block ']/h1[@class='m-stardust-title-block--title']/text()").extract_first(),
                'author': texts.xpath("//*[@id='h-stardust-byline']/span[2]/a/span/text()").extract(),
                'text': texts.xpath("//*[@id='m-content']/p").extract()
                }