file1 = open('d:/图片/捕获.png','rb')
connent = file1.read()
file1.close
with open ('d:/桌面/test/12.png','wb') as f:
    f.write(connent)


