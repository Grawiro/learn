from time import time


def timeintg():
  t0=time()
  while True:
    t=time()
    t0,t=t,t-t0
    yield t

    
T=timeintg()    
for i in range(10):
  print(next(T))
