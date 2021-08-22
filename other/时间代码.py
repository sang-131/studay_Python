import time,datetime
# 格式化成2016-03-20 11:45:39形式
#print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  
# 格式化成2016-03-20 11:45:39形式
print (time.strftime('%y.%m.%d', time.localtime()) )
print (time.strftime('%m', time.localtime()) )
print (type(time.strftime('%m', time.localtime()) ))
print (time.localtime(time.time()))
print (time.strftime('%y.%m.%d', time.localtime(time.time()-86400)) )
print(datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%')