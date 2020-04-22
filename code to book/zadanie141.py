class ResetException(Exception):
  pass


def srednia():
  suma=0.0
  N=0
  s=None
  while True:
    try:
      x = yield s
      try:
        suma+=x
        N+=1
        s=suma/N
      except:
        pass
    except ResetException:
      suma=0.0
      N=0
      s=None
    except GeneratorExit:
      break


s=srednia()
s.send(None)

print(s.send(1))
print(s.send(2))
print(s.send(3))
s.throw(ResetException)
print(s.send(4))
print(s.send(5))
print(s.send(6))
