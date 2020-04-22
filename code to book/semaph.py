from stolica import stolica
from threading import Thread, Lock, Semaphore
from time import time


def w_stolica(i,l,s):
  with s:
    x=stolica(i)
  with l:
    print x

    
panstwa=['Polska','Niemcy','Litwa','Szwecja','Estonia','Norwegia','Finlandia','Łotwa']

l=Lock()
s=Semaphore(4)
watki=[Thread(target=w_stolica,args=(p,l,s)) for p in panstwa]

t=time()
for w in watki:
  w.start()
for w in watki:
  w.join()
print 'Czas wykonania:', time()-t
