from socket import socket, SOL_SOCKET, SO_REUSEADDR
from threading import Thread, Lock


znaki='XO'


def koniec(l,ostatni):
  # współrzędne ostatnio dodanego znaku
  oy,ox=divmod(ostatni,3)
  # ostatnio dodany znak
  znak = l[3*oy+ox]
  # kolumna
  if all([l[3*i+ox]==znak for i in range(3)]):
    return ''.join([str(3*i+ox) for i in range(3)])
  # wiersz
  if all([l[3*oy+i]==znak for i in range(3)]):
    return ''.join([str(3*oy+i) for i in range(3)])
  # przekątna
  if ox==oy and all([l[i]==znak for i in [0,4,8]]):
    return '048'
  # antyprzekątna
  if ox==2-oy and all([l[i]==znak for i in [2,4,6]]):
    return '246'


def gra(*gracze):
  for g in gracze:
    g.sendall('>Rozpoczynamy grę\n'.encode('utf8'))
  plansza=[' ']*9
  for r in range(9):
    while True:
      gracze[r % 2].sendall(b'>Podaj pole:')
      n=gracze[r % 2].recv(4).strip()
      if not n.isdigit() or int(n)<0 or int(n)>8:
        gracze[r % 2].sendall('>Nieprawidłowa wartość\n'.encode('utf8'))
      elif plansza[int(n)]!=' ':
        gracze[r % 2].sendall('>Nieprawidłowe pole\n'.encode('utf8'))
      else:
        break
    n=int(n)
    plansza[n] = znaki[r % 2]
    for g in gracze:
      g.sendall(''.join(['|'+''.join(plansza[3*i:3*(i+1)])+'|\n' for i in range(3)]).encode('utf8'))
    k=koniec(plansza,n)
    if k:
      gracze[r % 2].sendall('>Zwycięstwo\n'.encode('utf8'))
      gracze[(r+1) % 2].sendall(b'>Przegrana\n')
      for g in gracze:
        g.sendall((k+'\n').encode('utf8'))
        g.close()
      return
  for g in gracze:
    g.sendall(b'>Remis\n')
    g.close()
    
    
s=socket()
s.bind(('localhost',4444))
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(1)

try:
  while True:
    pierwszy=s.accept()[0]
    pierwszy.sendall(b'>Czekaj na drugiego gracza')
    drugi=s.accept()[0]
    w=Thread(target=gra,args=(pierwszy,drugi))
    w.daemon=True
    w.start()
finally:
  s.close()
