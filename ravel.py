import numpy as np  
x = np.array([[1, 3, 5], [11, -35, 56]])  
y = np.ravel(x, order='K')  
#z = np.ravel(x, order='C')  
#p = np.ravel(x, order='A')  
#q = np.ravel(x, order='K')  
print(y)  
#z  
#p  
#q  
