# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TechradarSpider(CrawlSpider):
    name = 'techradar_iphonex'
    allowed_domains = ['www.techradar.com']
    start_urls = ['http://www.techradar.com/search?searchTerm=iphone+x/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@class='next']"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//*[@id='content']/section/div[2]/div[1]/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//*[@id='content']/section/div[2]/div[2]/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//*[@id='content']/section/div[2]/div[3]/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//*[@id='content']/section/div[2]/div[4]/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//*[@id='content']/section/div[2]/div[5]/a"), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        # yield {
        #     'title': response.xpath("//h1[@itemprop='name headline']/text()").extract_first(),
        #     'author': response.xpath("//a[@rel='author']/span[@itemprop='name']/text()").extract()
        # }
        
        for texts in response.xpath("//article[@class='news-article ']"):
            yield {
                'title': texts.xpath("//h1[@itemprop='name headline']/text()").extract_first(),
                'author': texts.xpath("//a[@rel='author']/span[@itemprop='name']/text()").extract(),
                'text': texts.xpath("//div[@class='text-copy bodyCopy auto']/p").extract()
                }
        for texts in response.xpath("//article[@class='review-article']"):
            yield {
                'title': texts.xpath("//h1[@itemprop='name headline']/text()").extract_first(),
                'author': texts.xpath("//a[@rel='author']/span[@itemprop='name']/text()").extract(),
                'text': texts.xpath("//div[@class='text-copy bodyCopy auto']/p").extract()
                }
