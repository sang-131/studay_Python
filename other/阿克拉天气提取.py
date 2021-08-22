# 引入requests
import requests
import csv

csv_file = open('阿克拉201907-202006天气数据.csv','w',encoding='utf-8-sig',newline='')
writer=csv.writer(csv_file)
writer.writerow(['日落时间','天气'])
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
nub = ['20190628','20190728','20190901','20190929',
        '20191027','20191201','20191229','20200126',
        '20200301','20200329','20200426','20200531']
for i in nub:        
    url='https://dsx.weather.com/wxd/v2/PastObsAvg/en_US/{}/35/5.66,-0.20?api=7bb1c920-7027-4289-9c96-ae5e263980bc'.format(i)
    res=requests.get(url,headers=headers)
    re=res.json()
    for i in re:
        sunset=i['SunData']['sunsetISOLocal']
        wxDetails=i['WxDetails']['wx']
        writer.writerow([sunset,wxDetails])
csv_file.close()