import requests
import bs4,re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

# url = 'http://btbtdy2.com/btdy/dy30651.html'
url = 'https://56.com-zx-56.com/share/c2b0e140029533c81a1793e5930e29ed'
re = requests.get(url,headers=headers)
print(re.status_code)
soup = bs4.BeautifulSoup(re.text,'html.parser')
datas= soup.find_all('script',type="text/javascript")
print(datas[2])
for i in range(30):
    print(datas[2][i])
# a = re.search(str(datas[2]),r'^main = "(.*)";')
# print(a)
# for i in datas:
#     print(i)
#     a = re.search(i,r'^main = "(.*)";')
#     print(a)
#     print('--------------------------------------------------')
# def get_uri_from_m3u8():
#     print("正在解析真实下载地址...")
#     # with open('temp.m3u8','wb') as file:
#     #     file.write(requests.get(realAdr).content)
#     m3u8Obj = m3u8.load('index.m3u8')
#     print("解析完成.")
#     return m3u8Obj.segments

# a = get_uri_from_m3u8()    
# print(a)
# print(type(a))
# https://56.com-zx-56.com/20200919/17827_a11c205d/index.m3u8?sign=7a857bc0123d5ca71b0a77085d5e7699
# https://56.com-zx-56.com/20200919/17827_a11c205d/1.jpg
# https://56.com-zx-56.com/20200919/17827_a11c205d/1000k/hls/index.m3u8
# https://56.com-zx-56.com/20200919/17828_5fa538b8/1000k/hls/index.m3u8
# 75563284dd7000000.ts
# # https://56.com-zx-56.com/20200919/17827_a11c205d/1000k/hls/75563284dd7000000.ts
# 1-http://btbtdy2.com/play/30651-0-0.html-https://56.com-zx-56.com/share/c2b0e140029533c81a1793e5930e29ed
# 2-http://btbtdy2.com/play/30651-0-1.html-https://56.com-zx-56.com/share/57a33a900c373d400a96043e9ef92461
