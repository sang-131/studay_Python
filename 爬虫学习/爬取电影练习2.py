import requests, bs4

# 为躲避反爬机制，伪装成浏览器的请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
list_move = []
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    
    num = bs.find_all('em',class_="")
        #查找序号
    title = bs.find_all('span', class_="title")
        #查找电影名
    if bs.find_all('span',class_="inq")!=None:
        #查找推荐语
        tes = bs.find_all('span',class_="inq")
    else:
        tes = '无'    
        # comment = bs.find_all('span',class_="rating_num")
    #     #查找评分
    # url_movie = bs.find_all('div',class_='pic').find('a')
    
    # for i in range(25):
    #     list1 = [num[i].text,title[1].text,tes[i].text,url_movie[i]['href']]
    #     list_move.append(list1)

    for i in range(25):
        print(num[i].text,title[i].text,tes[i].text)


