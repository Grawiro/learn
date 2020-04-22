from threading import Thread, Lock
    
    
def f(N,l):
  for i in xrange(N):
    with l:
      print i


l=Lock()
watek1=Thread(target=f,args=(5,l))
watek2=Thread(target=f,args=(5,l))
watek1.start()
watek2.start()
watek1.join()
watek2.join()

print 'Koniec'
