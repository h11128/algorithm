w = [0,2,2,6,5,4]
d = [0,6,3,5,4,6]
import numpy as np

def f(W,i):
    if w[i] > W:
        res[W,i] = res[W,i-1]
    elif w[i] <= W:
        res[W,i] = max(res[W,i-1],res[W-w[i],i-1]+d[i])
        if res[W-w[i],i-1]+d[i] == res[W,i]:
            print("update res[",W,",",i,"] by add d[",i,"]")

res=np.zeros((15,6),dtype=np.int32)

for i in range(1,6):
    for j in range(1,15):
        f(j,i)
    print(res)
