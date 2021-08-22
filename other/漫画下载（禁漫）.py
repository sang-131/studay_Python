from gevent import monkey
monkey.patch_all()
import gevent,time,requests,bs4
from gevent.queue import Queue
import os

print('''
禁漫天堂https://18comic.vip/，
自动下载代码，
漫画将下载在D:\文档\漫画
''')
time.sleep(2)
cartoon_name = input('请输入漫画名称：')
time.sleep(1)
cartoon_url = input('请输入漫画首页网址：')
print('文件名：',cartoon_name)
while True:
    a = input('请输入y，开始下载：')
    if a == 'y':
        break
start = time.time()

path = r'D:\文档\漫画' 
os.mkdir(path + './{}'.format(cartoon_name))
file_name = '{}\\{}\\'.format(path,cartoon_name)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
work = Queue()
ps1=requests.get(cartoon_url,headers=headers)
bs1 = bs4.BeautifulSoup(ps1.text,'html.parser') 
cartoon_code={}
a=1
if bs1.find('ul',class_="btn-toolbar") != None:
    data_urls=bs1.find('ul',class_="btn-toolbar").find_all('a')
    for data_url in data_urls:
        cartoon_code[data_url['href'][7:]] = a
        urls = 'https://18comic.vip{}'.format(data_url['href'])
        a = a+1
        ps2 = requests.get(urls,headers=headers)
        bs2 = bs4.BeautifulSoup(ps2.text,'html.parser') 
        jpg_urls=bs2.find_all('div',style="text-align:center;")
        for jpg_url in jpg_urls:
            number = jpg_url['id']
            url = 'https://cdn-msp.18comic.vip/media/photos/{}/{}'.format(urls[26:],number)
            work.put_nowait(url)
else:
    data_urls=bs1.find('div',class_="p-t-5 p-b-5 read-block").find('a')
    cartoon_code[data_urls['href'][7:-1]] = a
    urls = 'https://18comic.vip{}'.format(data_urls['href'])
    ps2 = requests.get(urls,headers=headers)
    bs2 = bs4.BeautifulSoup(ps2.text,'html.parser') 
    jpg_urls=bs2.find_all('div',style="text-align:center;")
    for jpg_url in jpg_urls:
        number = jpg_url['id']
        url = 'https://cdn-msp.18comic.vip/media/photos/{}/{}'.format(urls[26:-1],number)
        work.put_nowait(url)
def crawler():
    while not work.empty():
        url=work.get_nowait()
        re = requests.get(url,headers=headers)
        picuture = re.content
        with open (r'{}{}-{}.jpg'.format(file_name,str(cartoon_code[url[41:-10]]).zfill(2),url[-9:-4]),'wb') as f:
            f.write(picuture)
        info = '任务进行中，剩余{}个'.format(str(work.qsize()))
        print(info,end="")
        print("\b"*(len(info)*2),end="",flush=True)
        time.sleep(1)
task_list = []
for x in range(3):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)
end=time.time()
print('已完成，耗时：',round(end-start),'秒.')



