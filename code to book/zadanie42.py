from time import time

promienie = range(1,101)

t=time()
obwody=[]
for r in promienie:
  obwody.append(6.28*r)
print(time()-t)
t=time()
[6.28*r for r in promienie]
print(time()-t)
t=time()
list(map(lambda r:6.38*r,promienie))
print(time()-t)
t=time()
list(map(6.28.__mul__,promienie))
print(time()-t)
