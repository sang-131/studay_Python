import requests
from bs4 import BeautifulSoup

res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/')
soup = BeautifulSoup(res.text,'html.parser')
#print(soup)
items = soup.find_all(class_='comment-content')
for item in items:
    words = item.text
    print(words)
   