def czas(f):
  from datetime import datetime
  def nowa(*args):
    nowa.czas = datetime.now()
    return f(*args)
  nowa.czas = datetime.now()
  return nowa
  
@czas
def f(x):
  return 2*x

print(f.czas)
f(2)
print(f.czas)
