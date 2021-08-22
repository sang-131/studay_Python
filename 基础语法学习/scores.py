file1=open('d:/桌面/test/scores.txt','r',encoding='utf-8')
file1_lines=file1.readlines()
file1.close()
print(file1_lines)

finel_result = []
for i in file1_lines:
    data = i.split()
    sum = 0
    for score in data[1:]:
        sum = sum + int(score)
    result = data[0] + str(sum)+'\n'
    finel_result.append(result)

winner = open('d:/桌面/test/winner.txt','w',encoding='utf-8')
winner.writelines(finel_result)
winner.close

