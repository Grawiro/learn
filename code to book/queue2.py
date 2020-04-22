from threading import Thread, Lock
from Queue import Queue
from stolica import stolica


def f(q,pl,ql):
  work=True
  while work:
    with ql:
      if q.empty():
        work=False
      else:
        s=q.get()
    s=stolica(s)
    with pl:
      print s


pl=Lock()
ql=Lock()
q=Queue()
N=2

for i in ['Polska','Niemcy','Litwa','Estonia','Finlandia','Szwecja','Norwegia','Islandia']:
  q.put(i)
        
W=[Thread(target=f,args=[q,pl,ql]) for i in xrange(N)]
for w in W:
  w.start()
for w in W:
  w.join()
