import scrapy
from scrapy.selector import Selector
from time import sleep
import random


def normalize_str(text) -> str:
    if text is None:
        text = ''
    text = str(text)
    text = text.strip()
    text = text.replace('\n', '')
    text = text.replace('  ', '')
    return text


class ProductSpider(scrapy.Spider):
    name = 'product'
    allowed_domains = ['digikala.com']
    start_urls = ['http://digikala.com/']

    def start_requests(self):
        urls = [
            # example urls
            'https://www.digikala.com/product/dkp-3942680/کابل-تبدیل-usb-به-usb-c-اچ-اند-ام-مدل-c04-طول-02-متر',
            'https://www.digikala.com/product/dkp-3329268/کابل-تبدیل-usb-به-usb-c-بیبوشی-مدل-ca003a-طول-1-متر',
            'https://www.digikala.com/product/dkp-3141369/کابل-تبدیل-usb-به-usb-c-بیبوشی-مدل-a05-طول-1-متر',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sleep(random.randint(1, 5))
        r = response
        product = dict()
        product['url'] = r.url
        product['title'] = normalize_str(r.css('div#content h1::text').get())
        product['sub_title'] = normalize_str(r.css('div#content div.c-product__config > span::text').get())
        product['description'] = normalize_str(r.css('div#desc div > div::text').get())
        attribute_keys = r.css('div#params li > div.c-params__list-key').getall()
        attribute_values = r.css('div#params li > div.c-params__list-value').getall()
        attributes_tmp = list(zip(attribute_keys, attribute_values))
        attributes = []
        for index, (attr_key, attr_val) in enumerate(attributes_tmp):
            key = Selector(text=attr_key).css('div > span::text').get()
            val = normalize_str(Selector(text=attr_val).css('div > span::text').get())
            if key is None:
                attributes[-1]['val'] += '\n' + val
            else:
                key = normalize_str(key)
                attributes.append({
                    'key': key,
                    'val': val,
                })
        product['attributes'] = attributes

        original_price = normalize_str(
            r.css('div#content div.c-product__seller-price-prev.js-rrp-price::text').get()).replace(',', '')
        product['original_price'] = original_price

        final_price = normalize_str(
            r.css('div#content div.c-product__seller-price-real.js-ab-old-price-value > div::text').get()) \
            .replace(',', '')
        product['final_price'] = final_price

        images = r.css(
            'div#gallery-content-1 div.c-remodal-gallery__thumbs.js-official-thumbs > div:not([class*="is-video"]) > img::attr(data-src)').getall()
        images_tmp = []
        for image in images:
            char_index = image.find('?')
            if char_index != -1:
                image = image[0:char_index]
            image = image.strip()
            images_tmp.append(image)

        images = images_tmp
        del images_tmp
        product['images'] = images

        yield product

