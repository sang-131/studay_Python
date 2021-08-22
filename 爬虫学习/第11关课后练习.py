from gevent import monkey
monkey.patch_all()
import gevent,time,requests,bs4,csv
from gevent.queue import Queue
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
start = time.time()
work = Queue()
work.put_nowait('http://www.mtime.com/top/tv/top100/')
for i in range(2,11):
    url = 'http://www.mtime.com/top/tv/top100/index-{}.html'.format(i)
    work.put_nowait(url)
# print(work)
a_list =[]
a_list.append(['剧名','导演','主演','简介'])
def crawler():
    while not work.empty():
        url=work.get_nowait()
        re = requests.get(url,headers=headers)
        print(re.status_code)
        bs = bs4.BeautifulSoup(re.text,'html.parser')
        datas = bs.find_all('div',class_="mov_con")
        for data in datas:
            movie = data.find('a').text
            a = len(data.find_all('p'))
            if a > 1:
                director = data.find_all('p')[0].text
                actor = data.find_all('p')[1].text
            else:
                director = ''
                actor = data.find_all('p')[0].text   
            # if data.find_all('p')[1] !=None:
            #     director = data.find_all('p')[0].text
            #     actor = data.find_all('p')[1].text
            # else:
            #     director = ''
            #     actor = data.find_all('p')[0].text
            if data.find('p',class_="mt3") !=None:
                introduction = data.find('p',class_="mt3").text
            else:
                introduction = ''
            a_list.append([movie,director[4:],actor[4:],introduction])
task_list = []
for x in range(2):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)
end=time.time()
f= open('shiguotop100.csv','w',newline='',encoding='utf-8-sig')
writer=csv.writer(f)
writer.writerows(a_list)
f.close()
print(end-start)