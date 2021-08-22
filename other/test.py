import re
 
word = "test"
s = "test abcdas test 1234 testcase testsuite"
w = [m.start() for m in re.finditer(word, s)]
print(w)

# a = '1,2,3'
# c =a.split(',')
# print(c)
# print(type(c))
# a = ['1\n','2\n','3\n']
# file = open('11.txt','w')
# file.writelines(a)
# file.close()
file = open('11.txt','r')
con= file.readlines()
for i in con:
    print(i.strip())
    print(type(i))
    print(len(i))
    
file.close()

