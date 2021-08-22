import requests
import bs4
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title ='sheet1'
sheet['A1']='编号'
sheet['B1']='电影名'
sheet['C1']='评分'
sheet['D1']='推荐语'
sheet['E1']='链接'

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text #编号
        title = titles.find('span', class_="title").text #电影名
        comment = titles.find('span',class_="rating_num").text #评分
        url_movie = titles.find('a')['href'] #链接
        if titles.find('span',class_="inq") != None:
            tes = titles.find('span',class_="inq").text #推荐语
        else:
            tes = '无'
        sheet.append([num,title,comment,tes,url_movie])
                 
wb.save('豆瓣电影TOP250.xlsx')           