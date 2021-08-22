import scrapy
import bs4
from ..items import JobuiItem
class JobuiSpide(scrapy.Spider):
    name = 'jobui'
    allowed_domains = ['www.jobui.com']
    start_urls = ['http://www.jobui.com/rank/company/']
    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text,'html.parser')
        ul_list = bs.find_all('ul',class_='textList flsty cfix')
        for ul in ul_list:
            a_list = ul.find_all('a')
            for a in a_list:
                company_id = a['href']
                url = 'http://www.jobui.com{id}jobs'
                real_url = url.format(id = company_id)
                yield scrapy.Request(real_url,callback=self.parse_job)
        #return super().parse(response)
    def parse_job(self,response):
        bs = bs4.BeautifulSoup(response.text,'html.parser')
        company = bs.find(id="companyH1").text
        datas = bs.find_all('div',class_="c-job-list")
        for data in datas:
            item = JobuiItem()
            item['company'] = company
            item['position'] = data.find('a').find('h3').text
            item['address'] = data.find_all('span')[0]['title']
            item['detail'] = data.find_all('span')[1]['title']
            yield item
            
            
