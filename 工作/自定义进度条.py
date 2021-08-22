from tqdm import tqdm
import time

print('|'*20)
for i in range(101):
    info = '任务进行中，完成 {} {} %'.format('█'*round(i/10),i)
    print(info,end="")
    print("\b"*(len(info)*2),end="",flush=True)
    time.sleep(0.1)
print(info)    
# for i in tqdm(range(100)):
#     i
#     time.sleep(0.1)