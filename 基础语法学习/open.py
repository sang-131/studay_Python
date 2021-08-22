# file1 = open('d:/桌面/test/abc.txt','r',encoding='utf-8') 
# filecontent = file1.read()   
# print(filecontent)
# file1.close()

# file1 = open('d:/桌面/test/abc.txt','w',encoding='utf-8') 
# file1.write('张无忌\n')
# file1.write('赵敏\n')


file1 = open('d:/桌面/test/abc.txt','a',encoding='utf-8') 
file1.write('张无忌\n')
file1.write('赵敏\n')
file1.close()
