import scrapy

class Gizmodo_iphonex(scrapy.Spider):
    name = 'gizmodo_htc'

    def start_requests(self):
        urls = [
            'https://gizmodo.com/htcs-u12-looks-like-an-awkward-budget-hybrid-of-an-ip-1828695303',
            'https://gizmodo.com/i-really-hope-htc-doesnt-go-out-like-this-1827380446',
            'https://gizmodo.com/htcs-u12-continues-to-set-itself-apart-with-a-squeeze-1826241870',
            'https://gizmodo.com/here-are-all-the-interesting-smartphones-announced-at-i-1828720660'  
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
    

    
