###
# expercises
###

# 6
def sum_dict(dict_1,dict_2):
    res = dict_1.copy()
    for i in dict_2:
        if type(dict_2) == dict:
            res[i]=dict_2[i]
        elif type(dict_2) is list:
            res+=[i]
    return res

print(sum_dict({'a':1,'b':3},{'b':'v','c':5}))
print(sum_dict([1,2,3],[3,4,5]))

# 10
import time
# this is faster than import math
from math import sqrt
# import math
z = time.time()
x=[]
for i in range(1000000):
    x += [pow(i,.5)]
print('{}-{:.0f} -> {:.5f}'.format(x[0], x[-1], time.time()-z))
z = time.time()
x=[]
for i in range(1000000):
    x += [i**.5]
print('{}-{:.0f} -> {:.5f}'.format(x[0], x[-1], time.time()-z))
z = time.time()
x=[]
for i in range(1000000):
    # its fater only through another import method
    x += [sqrt(i)]
print('{}-{:.0f} -> {:.5f}'.format(x[0], x[-1], time.time()-z))
