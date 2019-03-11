# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Googlepixel3Spider(CrawlSpider):
    name = 'techradar_pixel3'
    allowed_domains = ['www.techradar.com']
    start_urls = ['https://www.techradar.com/search?searchTerm=Google+Pixel+3']


    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@class='next']"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='listingResult small result1 ']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='listingResult small result2 ']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='listingResult small result3 ']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='listingResult small result4 ']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='listingResult small result5 ']/a"), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        # yield {
        #     'title': response.xpath("//h1[@itemprop='name headline']/text()").extract_first(),
        #     'author': response.xpath("//a[@rel='author']/span[@itemprop='name']/text()").extract()
        # }
        
        for texts in response.xpath("//article[@class='review-article']"):
            yield {
                'title': texts.xpath("//h1[@itemprop='name headline']/text()").extract_first(),
                'author': texts.xpath("//a[@rel='author']/span[@itemprop='name']/text()").extract(),
                'text': texts.xpath("//div[@class='text-copy bodyCopy auto']/p").extract()
                }
        for texts in response.xpath("//article[@class='news-article ']"):
            yield {
                'title': texts.xpath("//h1[@itemprop='name headline']/text()").extract_first(),
                'author': texts.xpath("//a[@rel='author']/span[@itemprop='name']/text()").extract(),
                'text': texts.xpath("//div[@class='text-copy bodyCopy auto']/p").extract()
                }


