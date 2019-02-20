import scrapy

class Gizmodo_iphonex(scrapy.Spider):
    name = 'gizmodo_huaweimate'

    def start_requests(self):
        urls = [
        'https://gizmodo.com/the-great-huawei-disconnect-1832194644',
        'https://gizmodo.com/huaweis-mate-20-pro-is-a-technical-marvel-1830346004',
        'https://gizmodo.com/huaweis-mate-20-pro-is-absolutely-loaded-1829779386',
        'https://gizmodo.com/whatever-this-mysterious-bendy-screen-phone-is-i-want-1831470620',
        'https://gizmodo.com/nokias-long-rumored-five-camera-beast-could-get-announ-1831400466',
        'https://gizmodo.com/samsung-cant-afford-to-hold-back-anymore-1831178495',
        'https://gizmodo.com/the-pixel-3-is-proof-that-google-doesnt-care-about-hard-1831096115',
        'https://gizmodo.com/huaweis-triple-camera-p20-pro-is-too-cool-for-america-1825647834',
        'https://gizmodo.com/the-best-phones-you-can-buy-right-now-1830552418',
        'https://gizmodo.com/huaweis-mate-10-pro-is-a-valiant-attempt-to-slay-the-ip-1820480251',
        'https://gizmodo.com/huaweis-new-triple-camera-smartphone-could-start-a-tech-1824093276',
        'https://gizmodo.com/huawei-s-mate-10-wants-to-be-the-smartest-phone-on-the-1819493681',
        'https://gizmodo.com/the-incredible-evolution-of-the-smartphone-notch-from-1829852261',
        'https://gizmodo.com/honor-s-mid-range-phone-is-trying-to-save-us-from-the-1822838663'
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
    

    
