import scrapy

class Gizmodo_iphonex(scrapy.Spider):
    name = 'gizmodo_motog6'

    def start_requests(self):
        urls = [
            'https://gizmodo.com/motos-great-cheap-phones-are-back-now-with-a-face-id-k-1825371190',
            'https://gizmodo.com/motorola-s-making-the-cheap-smartphone-even-harder-to-r-1826916725',
            'https://gizmodo.com/this-cheap-smartphone-has-a-ridiculous-battery-and-it-1819196297',
            'https://gizmodo.com/9-things-to-know-about-the-samsung-galaxy-s8-and-bixby-1793710888'
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
    

    
