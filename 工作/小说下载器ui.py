import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox,filedialog
from ttkbootstrap import Style

from gevent import monkey
monkey.patch_all()
import gevent,time,requests,bs4,csv
from gevent.queue import Queue

root = tk.Tk()
# 给主窗口设置标题内容
root.title("小说下载器")
root.geometry('500x400')
style = Style()
def save_path_func():
    save_dir=filedialog.askdirectory()
    print(save_dir)
    save_path.set(save_dir)
def download():
#师士传说  下载
    path = save_path.get()
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
    url_amount = int(work.qsize())  
    pg['maximum'] = url_amount
    def crawler():
        while not work.empty():
            url=work.get_nowait()
            pg['value'] = url_amount - int(work.qsize())
            # pg_persent.set(int(work.qsize()))
            a = url_amount - int(work.qsize())
            pg_persent.set('{} %'.format(round(a/url_amount*100,2)))
            # 更新画面
            root.update()
            try:
                re = requests.get(url[:-5],headers=headers)
                print(re.status_code)
                re.encoding = 'utf-8'
                bs = bs4.BeautifulSoup(re.text,'html.parser')
                title = bs.find('div',class_="bookname").find('h1').text
                # print(url[-4:],title)
                content = bs.find('div',id="content").text.strip()
                with open (r'{}\{}.txt'.format(path,url[-4:]),'a',encoding='utf-8') as f:
                    f.write(title)
                    f.write('\r\n')
                    f.write(content)
                # print(int(url_amount),int(work.qsize()))
                # info = '任务进行中，剩余{}个'.format(str(work.qsize()))
                # print(info,end="")
                # print("\b"*(len(info)*2),end="",flush=True)
                time.sleep(2)
            except Exception as e:
                e
                print(url)
                with open (r'{}\log.txt'.format(path),'a',encoding='utf-8') as f:
                    f.write(url+'\n')
    task_list = []
    for x in range(2):
        task = gevent.spawn(crawler)
        task_list.append(task)
    gevent.joinall(task_list)
    end=time.time()
    run_time = round(end-start)
    print('已完成，耗时：',run_time,'秒','(',round(run_time/60),'分',').')
labe = ttk.Labelframe(root,text='下载', style='info.TLabelframe')
labe1 = ttk.Label(labe,text='输入书名', )
labe2 = ttk.Label(labe,text='输入书号', )
labe3 = ttk.Label(labe,text='保存位置', )
book_name = tk.StringVar()
entry1 = ttk.Entry(labe,textvariable=book_name)
book_code = tk.StringVar()
entry2 = ttk.Entry(labe,textvariable=book_code)
save_path = tk.StringVar()
entry3 = ttk.Entry(labe,textvariable=save_path)
btn1 = ttk.Button(labe, text='开始下载', style='info.TButton',command=download)
btn2 = ttk.Button(labe, text='...', style='info.TButton',command=save_path_func)
labe10 = ttk.Labelframe(root,text='文件合并', style='primary.TLabelframe')
labe11 = ttk.Label(labe10,text='目标位置', )
entry11 = ttk.Entry(labe10,)
btn11 = ttk.Button(labe10, text='开始合并', style='info.TButton')
pg = ttk.Progressbar(root, value=0, style='success.Striped.Horizontal.TProgressbar')
pg_persent = tk.StringVar()
pg_labe = ttk.Label(root,textvariable=pg_persent)
# 完成布局
labe.pack(side='top',fill='both',expand=True)
labe10.pack(side='top',fill='both',expand=True)
labe1.grid(row=0,column=0,padx=10,pady=10)
labe2.grid(row=1,column=0,padx=10,pady=10)
labe3.grid(row=2,column=0,padx=10,pady=10)
entry1.grid(row=0,column=1,padx=10,pady=10)
entry2.grid(row=1,column=1,padx=10,pady=10)
entry3.grid(row=2,column=1,padx=10,pady=10)
btn1.grid(row=3,column=1,padx=10,pady=10)
btn2.grid(row=2,column=2,padx=10,pady=10)
labe11.grid(row=2,column=0,padx=10,pady=10)
entry11.grid(row=2,column=1,padx=10,pady=10)
btn11.grid(row=4,column=1,padx=10,pady=10)
pg.pack(side='bottom',fill='x',anchor='s',padx=10,pady=10)
pg_labe.pack(side='bottom',anchor='s')
root.mainloop()
