import scrapy

class Gizmodo_iphonex(scrapy.Spider):
    name = 'gizmodo_essphone'

    def start_requests(self):
        urls = [
            'https://gizmodo.com/essential-lurches-back-from-the-grave-to-offer-up-150-1830419810',
            'https://gizmodo.com/8-things-you-should-be-automating-on-your-smartphone-1831607495',
            'https://gizmodo.com/essentials-next-phone-will-be-a-wildly-different-ai-po-1829652226',
            'https://gizmodo.com/how-much-would-you-actually-pay-for-an-essential-phone-1828473807',
            'https://gizmodo.com/the-essential-phone-finally-makes-sense-1823185128',
            'https://gizmodo.com/the-red-hydrogen-one-is-a-phone-made-for-an-alternate-r-1830015204',
            
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
    

    
