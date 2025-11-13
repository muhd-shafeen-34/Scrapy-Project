import scrapy #header file

class AgentSpider(scrapy.Spider):

    name = "agentspider" #spider name
    allowed_domains = ["https://www.compass.com/"]

    start_urls = ["https://www.compass.com/agents/locations/district-of-columbia-dc/30522/"]

    def parse(self, response):
        cards = response.css("div.agentCard") #storing the entire response 
        #in order to go throgh first card of the page 
        # need to get the follow links of each cards
        follow_links = cards.css("a.agentCard-imageWrapper::attr(href)").getall() 
        
        #for understanding iam going throgh the first agent

        first_agent = follow_links[0]
        
        if first_agent:
            print("following first card link",first_agent)




