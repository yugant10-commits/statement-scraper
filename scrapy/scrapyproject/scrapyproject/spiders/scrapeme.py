import scrapy



class ScrapySpider(scrapy.Spider):
    name = 'login'
    # allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://banksmartxp.siddharthabank.com/']
 
    def parse(self, response):
        # username = response.xpath('//*[@id="nd-input-8"]')
        # password = response.xpath('//*[@id="nd-input-0"]')
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'abc', 'password': 'abc'},
            callback=self.parse_after_login
        )
    
    def parse_after_login(self, response):
        print(response.xpath('/html/body/app-root/app-container/header/div[2]/ul/li[2]/dropdown-menu/button/div').get())


    #     return scrapy.FormRequest.from_response(response, formdata={
    #         'Username':'',
    #         'Password':''
    #     },callback=self.parse_after_login)
    

    
 
    #     formdata = {}
    #     for input in inputs:
    #         name = input.css('::attr(type)').get()
    #         value = input.css('::attr(ndbutton)').get()
    #         formdata[name] = value
 
    #     formdata['Username'] = 'abc'
    #     formdata['Password'] = 'abc'
 
    #     return scrapy.FormRequest.from_response(
    #         response,
    #         formdata = formdata,
    #         callback = self.parse_after_login
    #     )
 
    
