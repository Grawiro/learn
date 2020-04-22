from socket import socket, SOL_SOCKET, SO_REUSEADDR
from threading import Thread, Lock


def polaczenie(c,a):
  global l
  global d
  print('Połączenie z adresu %s' % (a,))
  while True:
    c.sendall(b'Podaj nick:')
    nick=c.recv(1024)
    if nick==b'':
      c.close()
      print('Połączenie z adresu %s zakończone' % (a,))
      return
    nick=nick.strip()
    with l:
      if nick in d:
        c.sendall(b'Nick istnieje\n')
      else:
        d[nick]=c
        break
  while True:
    x=c.recv(1024)
    if x==b'':
      with l:
        del d[nick]
      c.close()
      print('Połączenie z adresu %s zakończone' % (a,))
      break
    c.sendall(x)


l=Lock()
d={}

s=socket()
s.bind(('localhost',4444))
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(1)
try:
  while True:
    w=Thread(target=polaczenie,args=s.accept())
    w.daemon=True
    w.start()
finally:
  s.close()
