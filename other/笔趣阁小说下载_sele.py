from selenium import  webdriver # 从selenium库总调用webdriver模块
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
# 从options模块中调用Options类
chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') 
chrome_options.add_argument('–disable-gpu')
chrome_options.add_argument('log-level=3')
# 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options = chrome_options) 
start = time.time()
path = r'D:\文档\我的小说\师士传说\log.txt'
f = open(path)
urls = f.readlines()
total = len(urls)
print('共',total,'个')
for index,url in enumerate(urls):
    url = url.strip()
    print('第',index+1,'个--',url)
    url_m = url[:-5]
    print(url_m)
    count = url[-4:]
    print(count)
    try:
        driver.get(url_m) # 访问页面
        time.sleep(1) # 暂停两秒，等待浏览器缓冲
        pageSource = driver.page_source # 获取页面信息，selenium的page_source方法可以直接返回页面源码
        bs = BeautifulSoup(pageSource,'html.parser')  # 使用bs解析网页
        title = bs.find('div',class_="bookname").find('h1').text
        content = bs.find('div',id="content").text.strip()
        with open (r'D:\文档\我的小说\师士传说\{}.txt'.format(count),'a',encoding='utf-8') as f:
            f.write(title)
            f.write('\r\n')
            f.write(content)
        print('成功，还剩',total-index-1,'个\n')
    except Exception as e:
            print(e)
            print('失败:',url)
            with open (r'D:\文档\我的小说\师士传说\log2.txt','a',encoding='utf-8') as f:
                f.write('{}\n'.format(url))

f.close()   
driver.close()
end = time.time()
result = end - start
print('运行结束，耗时：',result,'秒')