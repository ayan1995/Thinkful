# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class TechradarSpider(CrawlSpider):
    name = 'techradar_test'
    allowed_domains = ['www.techradar.com']
    start_urls = ['https://www.techradar.com/reviews/iphone-x-review']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@class='next']"), callback='parse_item', follow=True),
    )

    def parse_start_url(self, response):
        return self.parse_item(response)

    def parse_item(self, response):
        yield {
            'title': response.xpath("//h1[@itemprop='name headline']/text()").extract_first(),
            'author': response.xpath("//a[@rel='author']/span[@itemprop='name']/text()").extract_first()
        }
        
        for texts in response.xpath("//div[@class='text-copy bodyCopy auto']"):
            yield {
                'review': texts.xpath("//div[@class='text-copy bodyCopy auto']/p").extract()
                }   
        
