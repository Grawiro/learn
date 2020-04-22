from socket import socket, SOL_SOCKET, SO_REUSEADDR


s=socket()
s.bind(('localhost',4444))
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(1)
try:
  c,a=s.accept()
  print(c,a)
  while True:
    x=c.recv(16)
    if x==b'':
      c.close()
      break
    c.sendall(x)
finally:
  s.close()
