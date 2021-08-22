from gevent import monkey
monkey.patch_all()
import gevent,time,requests,bs4,csv
from gevent.queue import Queue


#师士传说  下载
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
start = time.time()
work = Queue()
url = 'https://www.biquwx.la/12_12588/'
re = requests.get(url,headers=headers)
print(re.status_code)
re.encoding = 'utf-8'
bs = bs4.BeautifulSoup(re.text,'html.parser')
url_papers = bs.find('div',id="list").find_all('dd')
count = 0
for url_paper in url_papers:
    count +=1
    url_cont = '{}{}+{:0>4d}'.format(url,url_paper.find('a')['href'],count)
    work.put_nowait(url_cont)
def crawler():
    while not work.empty():
        url=work.get_nowait()
        try:
            re = requests.get(url[:-5],headers=headers)
            print(re.status_code)
            re.encoding = 'utf-8'
            bs = bs4.BeautifulSoup(re.text,'html.parser')
            title = bs.find('div',class_="bookname").find('h1').text
            # print(url[-4:],title)
            content = bs.find('div',id="content").text.strip()
            with open (r'D:\文档\我的小说\师士传说\{}.txt'.format(url[-4:]),'a',encoding='utf-8') as f:
                f.write(title)
                f.write('\r\n')
                f.write(content)
            info = '任务进行中，剩余{}个'.format(str(work.qsize()))
            print(info,end="")
            print("\b"*(len(info)*2),end="",flush=True)
            time.sleep(2)
        except Exception as e:
            e
            print(url)
            with open (r'D:\文档\我的小说\师士传说\shisi_log.txt','a',encoding='utf-8') as f:
                f.write(url,',')
task_list = []
for x in range(2):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)
end=time.time()
run_time = round(end-start)
print('已完成，耗时：',run_time,'秒','(',round(run_time/60),'分',').')


