import re
a = 'https://18comic.vip/photo/198637/'
b = 'https://cdn-msp.18comic.vip/media/photos/198637/00007.jpg?v=1592624397'
c = '[杀不了的他与死不了的她][BD-720P/1080P-MP4][豆瓣7.0分][日语中字][1.89GB/4.68GB][2019][BT下载/迅雷下载]'
d = '\n標籤:\n韓漫, YAOI, 連載中 '
# result = re.findall('.*?(\d+)/',a)
# print(result)
# result = re.findall('.*jpg$',b)
# print(result)
# result = re.split(']',c)
# print(result)
result = re.search('.*:(\D*)',d).group()
print(result)
print(len(d))
for i,b in enumerate(d):
    print(i,b)
