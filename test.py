import numpy as np
import random

length = []
for i in range(10000000):
    seq = []
    while len(seq) < 3 or not (seq[-3]==1 and seq[-2]==1 and seq[-1]==0):
        seq += [random.randint(0, 1)]
    length += [len(seq)]
print(sum(length)/len(length))