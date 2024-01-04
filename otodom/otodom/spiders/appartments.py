import scrapy


class AppartmentsSpider(scrapy.Spider):
    name = "appartments"
    allowed_domains = ["www.otodom.pl"]
    start_urls = [
        "https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/cala-polska"
    ]

    def parse(self, response):
        query = "/html//article[@class='css-1dzw04n e1n06ry50']"
        for article in response.xpath(query):
            address = article.xpath("//p[contains(@class, 'e1n06ry53')]/text()").extract()
            attributes = article.xpath("//span[@class='css-1cyxwvy ei6hyam2']/text()").extract()
            prices = attributes[::2]
            rooms = attributes[1::2]
            size = attributes[2::2]
            yield {
                "address": address,
                "price": prices,
                "rooms": rooms,
                "size": size,
            }
