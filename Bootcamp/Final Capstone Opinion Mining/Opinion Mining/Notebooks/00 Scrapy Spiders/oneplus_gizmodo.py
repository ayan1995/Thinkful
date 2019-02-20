import scrapy

class Gizmodo_iphonex(scrapy.Spider):
    name = 'gizmodo_oneplus'

    def start_requests(self):
        urls = [
            'https://gizmodo.com/oneplus-6t-review-the-no-bullshit-best-deal-in-smartph-1830066240',
            'https://gizmodo.com/oneplus-killing-the-headphone-jack-is-more-about-money-1829041844',
            'https://gizmodo.com/the-best-phones-you-can-buy-right-now-1830552418',
            'https://gizmodo.com/oneplus-may-finally-get-its-chance-to-talk-you-out-of-d-1828421420',
            'https://gizmodo.com/it-s-kind-of-brilliant-how-this-dual-screen-smartphone-1830123400',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response

    def parse(self, response):
        for text in response.xpath("//div[@class='post-wrapper js_post-wrapper ']"):
            yield {
                'title': text.xpath("//h1[@class='headline hover-highlight entry-title js_entry-title']/a/text()").extract_first(),
                'author': text.xpath("//div[@class='meta__byline js_meta-byline author ']/a/text()").extract_first(),
                'text': text.xpath("//div[@class='post-content entry-content js_entry-content ']/p").extract()
            }
    

    
