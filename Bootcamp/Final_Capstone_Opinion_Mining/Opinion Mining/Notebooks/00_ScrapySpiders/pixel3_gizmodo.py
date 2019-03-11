import scrapy

class Gizmodo_iphonex(scrapy.Spider):
    name = 'gizmodo_pixel3'

    def start_requests(self):
        urls = [
            'https://gizmodo.com/leaked-video-of-alleged-pixel-3-lite-details-almost-eve-1831835472',
            'https://gizmodo.com/the-pixel-3-is-proof-that-google-doesnt-care-about-hard-1831096115',
            'https://gizmodo.com/google-pixel-3-users-say-the-phone-s-best-feature-is-bo-1830561287',
            'https://gizmodo.com/google-pixel-3-users-say-the-phone-s-best-feature-is-bo-1830561287',
            'https://gizmodo.com/the-pixel-3-wont-wirelessly-charge-at-max-speed-except-1829955945',
            'https://gizmodo.com/delightful-google-bug-seemingly-gives-pixel-3-xls-an-ex-1830080828',
            'https://gizmodo.com/googles-pixel-stand-is-a-smarter-breed-of-wireless-char-1829925295',
            'https://gizmodo.com/this-could-be-the-cheap-pixel-3-people-were-hoping-for-1830501985',
            'https://gizmodo.com/google-promises-a-fix-for-the-pixel-3s-biggest-issue-in-1830250889',
            'https://gizmodo.com/googles-incredible-night-sight-mode-was-worth-the-wait-1830432540',
            'https://gizmodo.com/our-google-pixel-3-liveblog-will-be-right-here-1829620327',
            'https://gizmodo.com/what-to-expect-from-googles-pixel-3-hardware-event-1829461865',
            'https://gizmodo.com/google-reportedly-vows-pixel-3-camera-will-work-properl-1829942407',
            'https://gizmodo.com/pixel-3-everything-about-googles-great-android-phone-h-1829623157',
            'https://gizmodo.com/phones-are-so-boring-i-want-to-believe-this-wild-pixel-1828886045',
            'https://gizmodo.com/google-pixel-3-review-the-other-way-to-make-a-killer-p-1829749807',
            'https://gizmodo.com/if-you-don-t-like-the-pixel-3-xl-s-new-notch-google-sa-1829662089',
            'https://gizmodo.com/leaked-pics-show-a-scary-big-notch-on-an-alleged-pixel-1827970939'
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
    

    
