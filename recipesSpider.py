import scrapy

class RecipeSpider(scrapy.Spider):
    name = "recipes"

    start_urls = ['https://www.intervalefoodhub.com/recipes']

    def parse(self, response):

        recipes = response.xpath('//div[@class="summary-title"]')
        
        # get recipe information
        
        for recipe in recipes:
            url = recipe.xpath('a/@href').extract_first()
            name = recipe.xpath('a/text()').extract_first()
            absolute_url = response.urljoin(url)
            #yield {'Name': name, 'URL': absolute_url}
            yield response.follow(absolute_url, self.parse_recipe, meta={'Name': name, 'URL': absolute_url})

    def parse_recipe(self, response):

        url = response.meta.get('URL')
        name = response.meta.get('Name')

        ingredients = response.xpath('//ul[@data-rte-list="default"]/li/p/text()').getall()

        if ingredients == []:
            ingredients = response.xpath('//ul/li/span/text()').getall()

        if ingredients == []:
            ingredients = response.xpath('//ul/li/text()').getall()
            
        if ingredients == []:
            ingredients = response.xpath('//div[@class="sqs-block-content"]/p/text()').getall()
            
        if ingredients == [] or ingredients[0] == "The Intervale Food Hub is a Social Enterprise of the " or ingredients[0] == "Recipe By ":
            ingredients = response.xpath('//div[@class="image-caption"]/p/text()').getall()

        if ingredients == []:
            ingredients = response.xpath('//em/span/text()').getall()

        if ingredients == []:
            ingredients = response.xpath('//em/text()').getall()

        if ingredients == []:
            ingredients = response.xpath('//p/span/text()').getall()

        if ingredients[0] == "From Anna Stockwell for ":
            ingredients = response.xpath('//ol/li/p/text()').getall()

        instructions = response.xpath('//ol[@data-rte-list="default"]/li/p/text()').getall()

        if instructions == []:
            instructions = response.xpath('//ol/li/text()').getall()
        
        #for ingredient in ingredients:
        yield {'Name': name, 'URL': url, 'Ingredients': ingredients, 'Instructions': instructions}

    def get_ingredients():

        ingredients = response.xpath('//ul[@data-rte-list="default"]/li/p/text()').getall()

        if ingredients == []:
            ingredients = response.xpath('//ul/li/span/text()').getall()

        if ingredients == []:
            ingredients = response.xpath('//ul/li/text()').getall()
            
        if ingredients == []:
            ingredients = response.xpath('//div[@class="sqs-block-content"]/p/text()').getall()
            
        if ingredients == [] or ingredients[0] == "The Intervale Food Hub is a Social Enterprise of the " or ingredients[0] == "Recipe By ":
            ingredients = response.xpath('//div[@class="image-caption"]/p/text()').getall()

        if ingredients == []:
            ingredients = response.xpath('//em/span/text()').getall()

        return ingredients
