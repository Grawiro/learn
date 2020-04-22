from stolica import stolica
from threading import Thread, Lock
from time import time
  
panstwa=['Polska','Niemcy','Litwa','Szwecja','Estonia','Norwegia','Finlandia','Łotwa']


def w_stolica(i,l):
  with l:
    print stolica(i)
  

l=Lock()
watki=[Thread(target=w_stolica,args=(p,l)) for p in panstwa)]
  
t=time()
for w in watki:
  w.start()
for w in watki:
  w.join()
print 'Czas wykonania:', time()-t
