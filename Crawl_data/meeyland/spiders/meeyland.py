import scrapy
from meeyland.items import MeeylandItem
class MeeyLand_Spider(scrapy.Spider):
    name = "meeyland"
    
    def start_requests(self):
        urls = [f"https://meeyland.com/ban-nha-rieng?page={i}" for i in range (1, 10)]
        
        for url in urls: 
            yield scrapy.Request(url=url, callback=self.parse)
        
    
    def parse(self, response):
        item = MeeylandItem()
        url = "https://meeyland.com/"
        
        products = response.xpath('//div[@class = "relative slider-hover"]')
        for product in products:
            item = MeeylandItem()
            item["name"] = product.xpath('.//a/div/div/div[2]/div/div/div/div/h3/a/text()').get()
            item["link"] = url + product.xpath('.//a').attrib["href"]
            item["location"] = product.xpath('.//a/div/div/div[2]/div/div/div/p/text()').get()
            item["area"] = product.xpath('.//div[@class="text-sm break-word line-clamp-1"][1]/span/text()[1]').get()
            item["number_of_bedrooms"] = product.xpath('.//div[@class="text-sm break-word line-clamp-1"][2]/span[2]/text()[1]').get()
            item["number_of_bathrooms"] = product.xpath('.//div[@class="text-sm break-word line-clamp-1"][3]/span[2]/text()[1]').get()
            item["price_per_metter"] = product.xpath('.//div[@class="whitespace-nowrap"][2]/text()').get()
            yield item
            
