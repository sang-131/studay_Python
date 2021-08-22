import requests, bs4

# 为躲避反爬机制，伪装成浏览器的请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('div',class_='item'):
        num = titles.find('em',class_="").text
        #查找序号
        title = titles.find('span', class_="title").text
        #查找电影名
        if titles.find('span',class_="inq")!=None:
        #查找推荐语
            tes = titles.find('span',class_="inq").text
        else:
            tes = '无'    
        #查找推荐语
        comment = titles.find('span',class_="rating_num").text
        #查找评分
        url_movie = titles.find('a')['href']

        print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)


