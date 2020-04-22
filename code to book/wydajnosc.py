from time import time

l_in=range(10**6)

t=time()
l_out=[]
for i in l_in:
  l_out.append(i**2)
print(time()-t)

t=time()
l_out=[i**2 for i in l_in]
print(time()-t)

t=time()
l_out=list(map(lambda i:i**2, l_in))
print(time()-t)

t=time()
l_out=list(map((2).__rpow__, l_in))
print(time()-t)
