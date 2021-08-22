import requests
from bs4 import BeautifulSoup
import smtplib 
from email.mime.text import MIMEText
from email.header import Header
import schedule
import time
account='294334611sang@gmail.com'
pwd='sang576488016'
receiver='294334611@qq.com'
def food_list():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    res_foods = requests.get('http://www.xiachufang.com/explore/',headers=headers)
    bs_foods = BeautifulSoup(res_foods.text,'html.parser')
    list_foods = bs_foods.find_all('div',class_='info pure-u')

    list_all = ''
    num=0
    for food in list_foods:
        num=num+1
        tag_a = food.find('a')
        name = tag_a.text.strip()
        url = 'http://www.xiachufang.com'+tag_a['href']
        tag_p = food.find('p',class_='ing ellipsis')
        ingredients = tag_p.text.strip()
        food_info = '''
        序号: %s
        菜名: %s
        链接: %s
        原料: %s
        '''%(num,name,url,ingredients)
        list_all=list_all+food_info
    return list_all
def send_email(list_all):
    smtp_server='smtp.gmail.com'
    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server,465)
    server.login(account,pwd)
    content= list_all
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '本周最受欢迎菜谱'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        server.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    server.quit()

def job():
    print('开始一次任务')
    list_all = food_list()
    print(list_all)
    # send_email(list_all)
    print('任务完成')
job()

# schedule.every().day.at("07:30").do(job) 
# while True:
#     schedule.run_pending()
#     time.sleep(1)
    