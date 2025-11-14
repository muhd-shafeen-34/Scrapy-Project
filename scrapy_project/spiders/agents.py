import scrapy #header file

class AgentSpider(scrapy.Spider):

    name = "agentspider" #spider name
    allowed_domains = ["compass.com"]

    start_urls = ["https://www.compass.com/agents/locations/district-of-columbia-dc/30522/"]

    current_page = 1 # instance variable

    #function to crawl through the agent cards

    def parse(self, response):
        cards = response.css("div.agentCard") #storing the entire response 
        #in order to go throgh first card of the page 
        # need to get the follow links of each cards
        follow_links = cards.css("a.agentCard-imageWrapper::attr(href)").getall() 

        if not cards:
            self.logger.info(f"No cards found on page {self.current_page}. Stopping spider.")
            return
        
        #iam going throgh the first page

        for link in follow_links:
        
            if link:
                print("following first card link",link)
                print("printed details of the links")
                # yield response.follow(link, callback=self.parse_details)


        base_url = response.url.split('?')[0]  # Remove existing query parameters
        next_page = f"{base_url}?page={self.current_page}"
        yield response.follow(next_page,callback = self.parse)
        self.current_page += 1


        # base_url = response.url.split('?')[0]  # Remove existing query parameters
        # next_page = f"{base_url}?page={self.current_page}"
        # yield response.follow(next_page,callback = self.parse)



            #here i called the details extraction function of the follow links
    

    # #this function will parse the agent details
    # def parse_details(self,response):

    #     #Getting full name

    #     names = response.css("h1.profileCard-name.textIntent-headline1::text").get().split()
    #     #cleaning the name to yield first name middle name last name
    #     first , middle , last = "","",""
    #     if len(names) == 1:
    #         first = names[0]
    #     elif len(names) == 2:      
    #         first,last = names
    #     elif len(names) >=3:
    #         first,middle,last = names[0], names[1], names[-1]
        
    #     profile = response.url

    #     image = response.css("img.profile-image::attr(src)").get()

    #     #getting about
    #     # about = response.css("div.profile-body::text").getall()

    #     about = response.css("div.profile-about")
    #     full_texts = about.css("::text").getall()

    #     #cleaning about

    #     cleaned_texts = []
    #     for text in full_texts:
    #         strip = text.strip()
    #         if strip:
    #             cleaned_texts.append(strip)
    #     description = "".join(cleaned_texts).replace("\n","")


    #     # Getting social links  to make it as a dict

    #     social_links = response.css("div.profile-experience a::attr(href)").getall()

    #     #cleaning social links
    #     cleaned_links = []
    #     for i in social_links:
    #         if i not in cleaned_links:
    #             cleaned_links.append(i)


    #         #excluded concierge social becuase the example in the task has excluded the concierge social
    #     platforms = ['facebook', 'instagram', 'linkedin', 'twitter','youtube','tiktok','pintrest']
        

    #     # here store the link and its corresponding social media platforms
    #     social_links = {}

    # #this section is used to find the platform from the link using nester for loops
    
    #     for link in cleaned_links:
    #         lower_link = link.lower()
    #         for platform in platforms:
    #             if platform in lower_link:
    #                 if platform not in social_links:
    #                     social_links[platform] = link
    #                 break

    #     #getting emailc

    #     email = response.css("a.profileCard-email::text").get()

    #     #getting title

    #     title = response.css("div.titleCard.textIntent-body::text").get()

    #     #getting numbers

    #     numbers = response.css("div.phoneCard.textIntent-body a::text").getall()

    #     #cleaning numbers to yield

    #     phonenumbers = []
    #     officenumbers = []
    #     for i in numbers:
    #         if ": " in i:
    #             number = i.split(": ")[1]
    #             phonenumbers.append(number)
    #             if i.startswith("O: "):
    #                 number2= i.split(": ")[1]
    #                 officenumbers.append(number2)


    #     yield {
    #         "profile_url" : profile,
    #         "first_name": first,
    #         "middle_name": middle,
    #         "last_name" : last,
    #         "image_url": image,
    #         "desciption": description,
    #         "social": social_links,
    #         "email": email,
    #         "title": title,
    #         "agent_phone_numbers": phonenumbers,
    #         "office_phone_numbers": officenumbers,



    #     }







        





