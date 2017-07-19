import scrapy


class PunteggiSpider(scrapy.Spider):
    name = "punteggi"
    start_urls = [
        'http://leghe.fantagazzetta.com/fantascandalo/calendario'
        ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }