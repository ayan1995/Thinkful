import scrapy

class Gizmodo_iphonex(scrapy.Spider):
    name = 'gizmodo_iphonex'

    def start_requests(self):
        urls = [
        'https://gizmodo.com/researcher-who-said-he-hacked-iphone-x-face-id-with-a-p-1831490792',
        'https://gizmodo.com/its-2018-and-the-iphone-is-still-super-annoying-1831096584',
        'https://gizmodo.com/apple-and-qualcomm-slap-fight-continues-with-ban-on-i-1830994133',
        'https://gizmodo.com/with-spigens-new-over-the-air-charging-case-were-one-s-1831590018',
        'https://gizmodo.com/some-notable-mobile-phone-firsts-in-history-1831103608',
        'https://gizmodo.com/lawsuit-claims-apple-lied-about-its-display-and-shady-m-1831124404',
        'https://gizmodo.com/some-more-extremely-minor-things-from-ces-2019-that-you-1831585649',
        'https://gizmodo.com/another-exploding-phone-story-reveals-the-one-good-thin-1831400950',
        'https://gizmodo.com/the-tricky-economics-of-the-iphone-xs-and-the-iphone-xr-1829996656',
        'https://gizmodo.com/maybe-people-like-the-home-button-1830224289',
        'https://gizmodo.com/the-iphone-xs-is-forever-1829305262',
        'https://gizmodo.com/check-out-the-iphone-xs-weirdo-battery-1829226450',
        'https://gizmodo.com/iphone-xs-guts-report-how-fast-is-the-a12-processor-a-1829388773',
        'https://gizmodo.com/rip-iphone-se-1829029330',
        'https://gizmodo.com/apples-super-big-and-pricey-iphone-is-significantly-o-1829279043',
        'https://gizmodo.com/major-complaints-about-the-iphone-xs-are-stacking-up-1829447724',
        'https://gizmodo.com/this-is-the-iphone-xs-you-should-buy-1829026224',
        'https://gizmodo.com/apple-iphone-xs-the-complete-rundown-1828979967',
        'https://gizmodo.com/the-iphone-xr-is-apples-new-real-big-deal-1829912968',
        'https://gizmodo.com/iphone-users-are-saying-colors-look-off-after-upgrading-1829267106'
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
    

    
