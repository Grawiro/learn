from select import select
from socket import socket, SOL_SOCKET, SO_REUSEADDR


read_wait=[]
write_wait={}

s=socket()
s.bind(('localhost',4444))
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(1)

c1=s.accept()[0]
c2=s.accept()[0]

read_wait.append(c1)
read_wait.append(c2)

while True:
  read_ready, write_ready, e = select(read_wait,write_wait.keys(),[],0)
  for i in read_ready:
    read_wait.remove(i)
    write_wait[i]=i.recv(1024).strip()
  for i in write_ready:
    i.sendall(write_wait.pop(i))
    read_wait.append(i)
