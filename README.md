# recipe_aggregator
Scrapes and formats recipes from the Intervale recipe blog (https://www.intervalefoodhub.com/recipes)

Install the Scrapy python framework (https://scrapy.org/) and put the recipesSpider.py file in the spiders folder. 

Run the program from the command line with the command "scrapy crawl recipes -o recipes.jl" to create a JSON formatted file with the scraped information.

Next run the excelBuilder program to convert the JSON file to a more readable Excel file.

Included is an example excel file, recipes_formatted.xlsx, built on 8/25.
