from select import select
from socket import socket, SOL_SOCKET, SO_REUSEADDR


s=socket()
s.bind(('localhost',4444))
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(1)

read_wait=[]
write_wait={}
log_read_wait=[]
log_write_wait={}
close_write_wait={}
gniazdo={}
login={}

while True:
  if select([s],[],[], .01)[0]:
    c=s.accept()[0]
    log_write_wait[c]=b'>Witaj!\nPodaj login:'
  log_read_ready, log_write_ready = select(log_read_wait, log_write_wait.keys(), [], .01)[:2]
  read_ready, write_ready = select(read_wait, write_wait.keys(), [], .01)[:2]  
  close_write_ready = select([], close_write_wait.keys(), [], .01)[1]
  for i in log_read_ready:
    log_read_wait.remove(i)
    x=i.recv(1024)
    if x==b'':
      i.close()
      continue
    x=x.strip()
    if x==b'':
      log_write_wait[i]='>Login nie może być pusty!\nPodaj login:'.encode('utf8')
    elif x[:1]==b'<':
      if x[1:]==b'E':
        close_write_wait[i]='>Zamknąłeś połączenie, do zobaczenia!\nPodaj login:'.encode('utf8')
      elif x[1:]==b'L':
        lista=[i.decode('utf8') for i in gniazdo.keys()]
        log_write_wait[i]=('>Lista zalogowanych użytkowników: '+', '.join(lista)+'\nPodaj login:').encode('utf8')
      else:
        log_write_wait[i]='>Nieprawidłowa komenda\nPodaj login:'.encode('utf8')
    elif any([j in x for j in [b'>',b'*']]):
      log_write_wait[i]='>Login zawiera niedozwolone znaki\nPodaj login:'.encode('utf8')
    elif x in gniazdo:
      log_write_wait[i]='>Login już istnieje\nPodaj login:'.encode('utf8')
    else:
      gniazdo[x]=c
      login[c]=x
      write_wait[i]=(b'Zalogowano jako '+x+b'\n')
  for i in log_write_ready:
    i.sendall(log_write_wait.pop(i))
    if i not in log_read_wait:
      log_read_wait.append(i)
  for i in read_ready:
    read_wait.remove(i)
    x=i.recv(1024)
    if x==b'':
      i.close()
      n=login[i]
      del login[i]
      del gniazdo[n]
      continue
    x=x.strip()
    if b'<' not in x:
      write_wait[i]='>Nieprawidłowy format wiadomości!\n'.encode('utf8')
      continue
    adresat,wiadomosc=x.split(b'<',1)
    if adresat==b'':
      if wiadomosc==b'E':
        close_write_wait[i]='>Zamknąłeś połączenie, do zobaczenia!\n'.encode('utf8')
        n=login[i]
        del login[i]
        del gniazdo[n]
      elif wiadomosc==b'L':
        lista=[i.decode('utf8') for i in gniazdo.keys()]
        write_wait[i]=('>Lista zalogowanych użytkowników: '+', '.join(lista)+'\n').encode('utf8')
      else:
        write_wait[i]='Nieprawidłowa komenda\n'.encode('utf8')
    elif adresat==b'*':
      inni=login.keys()
      inni.remove(i)
      for j in inni:
        write_wait[j]=wiadomosc+b'\n'
    elif adresat in gniazdo:
      n=login[i]
      write_wait[gniazdo[adresat]]=n+b'>'+wiadomosc+b'\n'
      if i not in read_wait:
        read_wait.append(i)
    else:
      write_wait[i]='>Użytkownik nie istnieje\n'.encode('utf8')
  for i in write_ready:
    i.sendall(write_wait.pop(i))
    if i not in read_wait:
      read_wait.append(i)
  for i in close_write_ready:
    i.sendall(close_write_wait.pop(i))
    i.close()
