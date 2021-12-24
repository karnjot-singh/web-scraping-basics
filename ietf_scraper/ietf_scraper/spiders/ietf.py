import scrapy
import w3lib.html

class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['https://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        #title = response.css('span/title::text').get()
        rfc = response.xpath('//span[@class="rfc-no"]/text()').get()
        author_name = response.xpath('//span[@class="author-name"]/text()').get()
        author_company = response.xpath('//span[@class="author-company"]/text()').get()
        date = response.xpath('//span[@class="date"]/text()').get()
        #title = response.xpath('//span[@class="title"]/text()').get()
        title = response.xpath('//meta[@name="DC.Title"]/@content').get()
        description = response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get()

        author_address = response.xpath('//span[@class="address"]/text()').getall()
        phone = response.xpath('//span[@class="phone"]/text()').get()
        email = response.xpath('//span[@class="email"]/text()').get()
        subtitle = response.xpath('//span[@class="subheading"]/text()').getall()
        text = response.xpath('//div[@class="text"]/text()').getall()
        text1 = w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get())
        
        return {"title": title, "authorName": author_name, "authorCompany": author_company, "address": author_address,
        "description": description,
         "text": text, "subtitle": subtitle, "date": date, "phone": phone, "email": email, "requestForCommentsCount": rfc,
         "test": text1}
