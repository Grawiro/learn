from socket import socket, SOL_SOCKET, SO_REUSEADDR
from threading import Thread, Lock

def wyjscie(c,a):
  c.close()
  print('Połaczenie z adresu %s zakończone' % (a,))


def polaczenie(c,a):
  global l
  global d
  print('Połączenie z adresu %s' % (a,))
  while True:
    c.sendall(b'>Podaj nick:')
    nick=c.recv(1024)
    if nick==b'':
      return wyjscie(c,a)
    nick=nick.strip()
    if nick==b'':
      c.sendall('>Nick nie może być pusty\n'.encode('utf8'))
    elif nick[:1]==b'<':
      komenda=nick[1:]
      if komenda==b'E':
        return wyjscie(c,a)
      elif komenda==b'L':
        with l:
          lista=[i.decode('utf8') for i in d.keys()]
          lista='>Zalogowani użytkownicy:'+', '.join(lista)+'\n'
          c.sendall(lista.encode('utf8'))
      else:
        c.sendall(b'>Nieznana komenda\n')
    elif b'<' in nick or b'>' in nick:
      c.sendall(b'>Nick zawiera niedozwolone znaki < lub >\n')
    else:
      with l:
        if nick in d:
          c.sendall(b'>Nick instnieje\n')
        else:
          d[nick]=c
          break
  print('OK')
  while True:
    x=c.recv(1024)
    if x==b'':
      with l:
        del d[nick]
      return wyjscie(c,a)
    if b'<' not in x:
      c.sendall('>Nieprawidłowy format wiadomości\n'.encode('utf8'))
    else:
      x=x.split(b'<',1)
      if x[0]==b'':
        komenda=x[1].strip()
        if komenda==b'E':
          with l:
            del d[nick]
          return wyjscie(c,a)
        elif komenda==b'L':
          with l:
            lista=[i.decode('utf8') for i in d.keys()]
            lista='>Zalogowani użytkownicy:'+', '.join(lista)+'\n'
            c.sendall(lista.encode('utf8'))
        else:
          c.sendall(b'>Nieznana komenda\n')
      else:
        with l:
          odb=d.get(x[0])
        if odb==None:
          c.sendall(b'>Nick "'+x[0]+b'" nie istnieje\n')
        else:
          odb.sendall(nick+b'>'+x[1]+b'\n')


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
