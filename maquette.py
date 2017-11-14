import numpy as np
import matplotlib.pyplot as plt

x = [0,0,0,1,2,3,2,1,0,0,1,2,3,2,1,2,3,2,1,0,0,0,1,2,3,4,5,6,5,4,3,2,1,2,3,4,5,4,5,6,5,4,5,4,3,2,3,2,1,2,1,0,0,0,0,0]
N = len(x)
search = 10
sparse = np.zeros_like(range(search))
state = [False for elm in sparse]
step = 6/float(search)

for ii in range(N):
    for jj in range(len(sparse)):
        if x[ii] < jj*step and state[jj]:
            sparse[jj] += 1
            state[jj] = False
        elif x[ii] > jj*step and not state[jj]:
            sparse[jj] += 1
            state[jj] = True
            
print np.argmax(sparse)*step