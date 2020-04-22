from socket import socket, SOL_SOCKET, SO_REUSEADDR


s=socket()
s.bind(('localhost',4444))
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(1)
try:
  c,a=s.accept()
  print('OK')
  x=c.recv(16)
  c.sendall(x)
  c.close()
finally:
  s.close()
