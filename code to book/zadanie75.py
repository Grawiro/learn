watki=[Thread(target=f,args=(5,l)) for i in xrange(2)]
for w in watki:
  w.start()
for w in watki:
  w.join()
  