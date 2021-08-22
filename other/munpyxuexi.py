import numpy as np

a = np.arange(2,14).reshape((3,4))
print(a)
b =np.array([[1,2,3],
            [4,5,6]])
print(b)    
print(np.cumsum(b))       
print(np.transpose(b))  
print(np.vstack((a,b)))