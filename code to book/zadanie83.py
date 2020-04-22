from socket import socket

s=socket()
s.connect(('localhost',4444))

s.sendall(b'Ala')
s.recv(1024)
s.sendall(b'<L')
print s.recv(1024)
s.sendall(b'<E')
  
