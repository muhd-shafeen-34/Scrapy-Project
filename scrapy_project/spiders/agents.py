import scrapy #header file

class AgentSpider(scrapy.Spider):

    name = "agentspider" #spider name

    start_urls = ["https://www.compass.com/agents/locations/district-of-columbia-dc/30522/"]

    def parse(self, response):
        cards = response.css("div.agentCard") #storing the entire response 

        print(len(cards))  #checking the fetch worked




