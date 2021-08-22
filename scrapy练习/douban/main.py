from scrapy import cmdline
import os

os.chdir(r'D:\文档\python代码\scrapy练习\douban')
# print(os.getcwd())
cmdline.execute(['scrapy','crawl','douban'])