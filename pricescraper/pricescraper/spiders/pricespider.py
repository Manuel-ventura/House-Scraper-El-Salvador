import scrapy


class PricespiderSpider(scrapy.Spider):
    name = "pricespider"
    allowed_domains = ["encuentra24.com"]
    start_urls = [
        "https://www.encuentra24.com/el-salvador-es/bienes-raices-venta-de-propiedades-casas?q=f_currency.USD%7Cwithcat.bienes-raices-venta-de-propiedades-casas,bienes-raices-venta-de-propiedades-apartamentos"
    ]

    def parse(self, response):
        print(f"URL: {response.url}")
        properties = response.css('div.d3-ad-tile__content')
        print(f"Found {len(properties)} properties on the page.")

        for property in properties:
            print("Processing a property.")

            # Extract location
            location = property.css(
                'div.d3-ad-tile__location').xpath('normalize-space()').get()
            print(f"Location: {location}")

            # Extract other details
            title = property.css('a.d3-ad-tile__title::text').get()
            print(f"Title: {title}")

            short_description = property.css(
                'div.d3-ad-tile__short-description::text').get()
            print(f"Short description: {short_description}")

            price = property.css('div.d3-ad-tile__price::text').get()
            print(f"Price: {price}")

            details = property.css(
                'ul.d3-ad-tile__details li.d3-ad-tile__details-item::text').getall()
            print(f"Details: {details}")

            yield {
                'localizacion': location,
                'titulo': title,
                'descripcion_corta': short_description,
                'precio': price,
                'detalles': details
            }

        # Find the link to the next page
        next_page = response.css(
            'a.d3-pagination__arrow--next::attr(href)').get()
        print(f"Next page: {next_page}")
        if next_page is not None:
            yield response.follow(next_page, self.parse)
