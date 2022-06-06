import numpy as np
import random

sbox = []
for i in range(16) :
    for j in range(16) :
        ele = str(i) + "." + str(j)
        sbox.append(ele)
random.shuffle(sbox) 
sbox = np.array(sbox).reshape(16,16)


print(sbox)