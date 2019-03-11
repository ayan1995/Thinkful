import scrapy

class Gizmodo_iphonex(scrapy.Spider):
    name = 'gizmodo_S9'

    def start_requests(self):
        urls = [
            'https://gizmodo.com/samsung-s-5g-ready-s10-x-sounds-like-a-powerhouse-tha-1831734610',
            'https://gizmodo.com/this-right-here-is-an-incredibly-annoying-thing-about-a-1831326627',
            'https://gizmodo.com/samsung-cant-afford-to-hold-back-anymore-1831178495',
            'https://gizmodo.com/nokias-long-rumored-five-camera-beast-could-get-announ-1831400466',
            'https://gizmodo.com/the-pixel-3-is-proof-that-google-doesnt-care-about-hard-1831096115',
            'https://gizmodo.com/samsung-s-new-theme-policy-sounds-like-some-bullshit-1830474527',
            'https://gizmodo.com/the-fancy-display-tech-samsung-apparently-wants-for-its-1829867330',
            'https://gizmodo.com/hell-yeah-bring-on-all-the-cameras-1830562377',
            'https://gizmodo.com/everything-you-need-to-know-about-the-samsung-note-9-1828211981',
            'https://gizmodo.com/samsungs-galaxy-note-9-is-the-best-big-phone-1828348138',
            'https://gizmodo.com/the-best-phones-you-can-buy-right-now-1830552418',
            'https://gizmodo.com/samsung-teases-galaxy-note-9-reveal-on-august-9-1827179763',
            'https://gizmodo.com/these-samsung-galaxy-s10-rumors-actually-sound-pretty-g-1827116632',
            'https://gizmodo.com/samsung-galaxy-note-9-rumors-everything-weve-heard-so-1827923738',
            'https://gizmodo.com/what-could-samsung-do-to-make-the-next-galaxy-tab-more-1827316986',
            'https://gizmodo.com/heres-what-is-actually-new-about-the-samsung-galaxy-s9-1823232526',
            'https://gizmodo.com/samsung-galaxy-s9-review-the-best-android-phone-dont-n-1823575944',
            'https://gizmodo.com/some-galaxy-s9-and-s9-users-say-their-phones-suffer-fr-1823984306'
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
    

    
