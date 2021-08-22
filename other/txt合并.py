import os
from tqdm import tqdm

files = r'D:\文档\我的小说\师士传说' #待合并文件路径
files_list= os.listdir(files)
fina_name = '师士传说.txt' #合并后文件名
fina_file = open(os.path.join(files,fina_name),'a',encoding='utf-8')
for i in tqdm(files_list,):
    files_path = os.path.join(files,i)
    with open (files_path,'r',encoding='utf-8') as f: 
        data = f.read()
    fina_file.write(data)
    fina_file.write('\r\n')
fina_file.close()    

