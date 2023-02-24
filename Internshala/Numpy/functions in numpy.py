import numpy as np
from scipy import stats

data=np.array([1,1,2,3,4,5,6,7,8,9,10])
mode=stats.mode(data)
print(mode[0][0])
mean =np.mean(data)
median =np.median(data)
print(mode)
print(mean)
print(median)
