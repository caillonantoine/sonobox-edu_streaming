import numpy as np
import matplotlib.pyplot as plt

x = [0,0,0,1,2,3,2,1,0,0,1,2,3,2,1,2,3,2,1,0,0,0,1,2,3,4,5,6,5,4,3,2,1,2,3,4,5,4,5,6,5,4,5,4,3,2,3,2,1,2,1,0,0,0,0,0]
N = len(x)
search = 10
spare = np.zeros_like(range(search))
logical = [False for elm in spare]
pas = 6/float(search)

for i in range(N):
    for j in range(len(spare)):
        if x[i] < j*pas and logical[j]:
            spare[j] += 1
            logical[j] = False
        elif x[i] > j*pas and not logical[j]:
            spare[j] += 1
            logical[j] = True
            
print np.argmax(spare)*pas