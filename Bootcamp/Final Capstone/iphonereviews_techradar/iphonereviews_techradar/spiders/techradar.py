# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TechradarSpider(CrawlSpider):
    name = 'techradar'
    allowed_domains = ['www.techradar.com']
    start_urls = ['https://www.techradar.com/reviews/iphone-x-review']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@class='next']"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # yield {
        #     'title': response.xpath("//h1[@itemprop='name headline']/text()").extract_first(),
        #     'author': response.xpath("//a[@rel='author']/span[@itemprop='name']/text()").extract_first(),
        #     'verdict': response.xpath("//div[@class='sub-box full']/p/text()").extract_first(),
        #     'For': response.xpath("//div[@class='sub-box'][1]/ul/li/text()").extract(),
        #     'Against': response.xpath("//div[@class='sub-box'][2]/ul/li/text()").extract()
        # }
        
        for text in response.xpath("//*[@id='article-body']"):
            yield {
                'review': text.xpath("//*[@id='article-body']/p").extract(),
            }
        
        
