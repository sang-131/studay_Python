from gevent import monkey
monkey.patch_all()
import gevent,time,requests,bs4,csv
from gevent.queue import Queue

csv_file = open('韩漫明细.csv','w',newline='',encoding='utf-8-sig')
writer = csv.writer(csv_file)
writer.writerow(['名称','点赞数','标签','链接'])
last_page = int(input('请输入最后页数：'))
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
start = time.time()
work = Queue()
for i in range(1,last_page+1):
    url = 'https://18comic.vip/albums/hanman?page={}'.format(i)
    work.put_nowait(url)
def crawler():
    while not work.empty():
        url=work.get_nowait()
        re = requests.get(url,headers=headers)
        # print(re.status_code)
        bs = bs4.BeautifulSoup(re.text,'html.parser')
        datas = bs.find_all('div',class_='col-xs-6 col-sm-6 col-md-4 col-lg-3 list-col')
        for data in datas:
            link = data.find('div',class_='well well-sm').find('a')['href']
            link = 'https://18comic.vip{}'.format(link)
            name = data.find('span',class_='video-title').text
            label = data.find_all('div',class_='title-truncate')[1].text[5:]
            label = "".join(label.split())
            star = data.find('div',class_="label-loveicon").find('span').text
            writer.writerow([name,star,label,link])
        info = '任务进行中，剩余{}个'.format(str(work.qsize()))
        print(info,end="")
        print("\b"*(len(info)*2),end="",flush=True)
        time.sleep(0.5)
task_list = []
for x in range(2):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)
csv_file.close
end=time.time()
print('已完成，耗时：',round(end-start),'秒.')





