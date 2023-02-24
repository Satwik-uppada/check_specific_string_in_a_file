import numpy as np
import time
size=1_000
l1= (list(range(size)))
l2= (list(range(size)))
start=time.time()
l3=[]
for i in range(size):
    sum=l1[i]+l2[i]
    l3.append(sum)

print(l3)
l3_avg=np.average(l3)
print(l3_avg)
a1=np.average(size)
print(a1)



print("time taken by  lists",(time.time()-start)*1000)

import numpy as np
arr5=np.formiter([[1,2,3],[5,6,7,],[5,6,7],[5,6,7]],dtype='int')
print(arr5)

