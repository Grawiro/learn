class DataException(Exception):
  pass

def srednia():
  suma=0.0
  N=0
  s=None
  while True:
    try:
      yield s
    except DataException as e:
        x = e.args[0]
        try:
          suma+=x
          N+=1
          s=suma/N
        except:
          pass
    except GeneratorExit:
      break

s=srednia()
s.send(None)

print(s.throw(DataException(1)))
print(s.throw(DataException(2)))
print(s.throw(DataException(3)))
