class Blokada(object):
  def __init__(self):
    self.b=False
  def __enter__(self):
    while self.b:
      pass
    self.b=True
  def __exit__(self,t,e,tb):
    self.b=False

from threading import Thread
from time import sleep

def f(x):
  for i in xrange(5):
    with b:
      print x,i
    sleep(1e-5)

b=Blokada()
Thread(target=f,args=('A',)).start()
Thread(target=f,args=('B',)).start()
