import scrapy #header file

class AgentSpider(scrapy.Spider):

    name = "agentspider" #spider name
    allowed_domains = ["compass.com"]

    start_urls = ["https://www.compass.com/agents/locations/district-of-columbia-dc/30522/"]

    #function to crawl through the agent cards

    def parse(self, response):
        cards = response.css("div.agentCard") #storing the entire response 
        #in order to go throgh first card of the page 
        # need to get the follow links of each cards
        follow_links = cards.css("a.agentCard-imageWrapper::attr(href)").getall() 
        
        #for understanding iam going throgh the first agent

        first_agent = follow_links[0]
        
        if first_agent:
            print("following first card link",first_agent)

            #here i called the details extraction function of the follow links

            yield response.follow(first_agent, callback=self.parse_details)
    

    #this function will parse the agent details
    def parse_details(self,response):

        #Getting full name

        names = response.css("h1.profileCard-name.textIntent-headline1::text").get().split()
        #cleaning the name to yield first name middle name last name
        first , middle , last = "","",""
        if len(names) == 1:
            first = names[0]
        elif len(names) == 2:      
            first,last = names
        elif len(names) >=3:
            first,middle,last = names[0], names[1], names[-1]
        
        profile = response.url

        image = response.css("img.profile-image::attr(src)").get()

        about = response.css("div.profile-body::text").getall()

        #cleaning about

        about_full = " ".join(about).replace("\n","")

        # Getting social links and its corresponding apps to make it as a dict

        social_links = response.css("div.profile-experience a::attr(href)").getall()
        social_text = response.css("div.profile-experience b::text").getall()
        social = dict(zip(social_text,social_links))
        
        #getting email

        email = response.css("a.profileCard-email::text").get()

        #getting title

        title = response.css("div.titleCard.textIntent-body::text").get()

        #getting numbers

        numbers = response.css("div.phoneCard.textIntent-body a::text").getall()

        #cleaning numbers to yield

        phonenumbers = []
        officenumbers = []
        for i in numbers:
            if ": " in i:
                number = i.split(": ")[1]
                phonenumbers.append(number)
                if i.startswith("O: "):
                    number2= i.split(": ")[1]
                    officenumbers.append(number2)


        yield {
            "profile_url" : profile,
            "first_name": first,
            "middle_name": middle,
            "last_name" : last,
            "image_url": image,
            "desciption": about_full,
            "social": social,
            "email": email,
            "title": title,
            "agent_phone_numbers": phonenumbers,
            "office_phone_numbers": officenumbers,



        }







        





