import scrapy
from scrapy.http import FormRequest, JsonRequest


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['www.httpbin.org']
    start_url = 'https://www.httpbin.org/post'
    data = {'name': 'germey', 'age': '26'}

    def start_requests(self):
        yield FormRequest(self.start_url, callback=self.parse, formdata=self.data)
        yield JsonRequest(self.start_url, callback=self.parse, data=self.data)

    def parse(self, response):
        # print('url', response.url)
        # print('request', response.request)
        # print('status', response.status)
        # print('headers', response.headers)
        print('text', response.text)
        # print('meta', response.meta)
