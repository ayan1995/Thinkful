# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from iphonereviews_techradar.items import ReviewItem


class TechradartestSpider(scrapy.Spider):
    name = 'techradartest'

    def start_requests(self):
        url = 'https://www.techradar.com/reviews/iphone-x-review/1'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for text in response.xpath("//*[@id='article-body']"):
            yield {
                # 'title': response.xpath("//h1[@itemprop='name headline']/text()").extract_first(),
                # 'author': response.xpath("//a[@rel='author']/span[@itemprop='name']/text()").extract_first(),
                # 'verdict': response.xpath("//div[@class='sub-box full']/p/text()").extract_first(),
                # 'For': response.xpath("//div[@class='sub-box'][1]/ul/li/text()").extract(),
                # 'Against': response.xpath("//div[@class='sub-box'][2]/ul/li/text()").extract(),
                'review': text.xpath("//*[@id='article-body']/p").extract()
            }

        next_page = response.xpath("//a[@class='next']").extract_first()

        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

        
        # loader = ItemLoader(item = ReviewItem(), response=response)
        # loader.add_xpath('title', "//h1[@itemprop='name headline']/text()")
        # loader.add_xpath('author', "//a[@rel='author']/span[@itemprop='name']/text()")
        # loader.add_xpath('verdict', "//div[@class='sub-box full']/p/text()")
        # loader.add_xpath('For', "//div[@class='sub-box'][1]/ul/li/text()")
        # loader.add_xpath('Against', "//div[@class='sub-box'][2]/ul/li/text()")
        # loader.add_xpath('review', "//*[@id='article-body']/p")
        # yield loader.load_item()