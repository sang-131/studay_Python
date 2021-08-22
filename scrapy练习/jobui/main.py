from scrapy import cmdline
import os

os.chdir(r'D:\文档\python代码\scrapy练习\jobui')
# print(os.getcwd())
cmdline.execute(['scrapy','crawl','jobui'])
