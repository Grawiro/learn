from threading import Thread


def f(N):
  for i in xrange(N):
    print i


watek1=Thread(target=f,args=(5,))
watek2=Thread(target=f,args=(5,))
watek1.start()
watek2.start()

print 'Koniec'
