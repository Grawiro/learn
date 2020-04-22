from select import select
from socket import socket, SOL_SOCKET, SO_REUSEADDR

s=socket()
s.bind(('localhost',4444))
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(1)

read_wait=[s]
write_wait={}

while True:
  read_ready, write_ready, e = select(read_wait,write_wait.keys(),[],0.1)
  for i in read_ready:
    if i == s:
      read_wait.append(i.accept()[0])
    else:
      read_wait.remove(i)
      x=i.recv(1024)
      if x:
        write_wait[i]=x.strip()
      else:
        i.close()
  for i in write_ready:
    i.sendall(write_wait.pop(i))
    read_wait.append(i)
