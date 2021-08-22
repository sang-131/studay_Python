#练习从阳光电影网下载电影
import requests
from bs4 import BeautifulSoup
from urllib.request import quote
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

movie_name = input('请输入要查找的电影：')
movie_name = movie_name.encode('gbk')
movie_url = quote(movie_name)

url = 'http://s.ygdy8.com/plus/s0.php?typeid=1&keyword='+movie_url
res =requests.get(url,headers=headers)
print(res.status_code)
bs = BeautifulSoup(res.text,'html.parser')
url =bs.find('td',width='55%').find('a')['href']
url = 'https://www.ygdy8.com/'+url
res =requests.get(url,headers=headers)
res.encoding='gbk'
bs = BeautifulSoup(res.text,'html.parser')
movie_ad = bs.find('td',style="WORD-WRAP: break-word").find('a')['href']
print(movie_ad)


