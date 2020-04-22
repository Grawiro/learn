from threading import Thread
from time import sleep


class Wagonik:

  def __init__(self):
    self.liczba_pasazerow=0
    
  def __enter__(self):
    if self.liczba_pasazerow>=3:
      raise ValueError('Wagonik już odjechał')
    self.liczba_pasazerow+=1
    print('Witamy pasażera!')
    while self.liczba_pasazerow<3:
      pass
      
  def __exit__(self,t,e,tb):
    pass


def f(x):
  with w:
    print('jedziemy!')


w=Wagonik()
Thread(target=f,args=('A',)).start()
Thread(target=f,args=('B',)).start()
Thread(target=f,args=('C',)).start()
Thread(target=f,args=('D',)).start()
