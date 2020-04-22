from queue import Queue


class Mikrowatek:

  def __init__(self,target):
    self.target=target

  def run(self):
    return self.target.send(None)

  def start(self,zarzadca):
    zarzadca.nowe_zadanie(self)


class Zarzadca:

  def __init__(self):
    self.kolejka_zadan = Queue()

  def nowe_zadanie(self,zadanie):
    self.kolejka_zadan.put(zadanie)

  def run(self):
    while not self.kolejka_zadan.empty():
      zadanie = self.kolejka_zadan.get()
      try:
        zadanie.run()
        self.kolejka_zadan.put(zadanie)
      except StopIteration:
        pass


def koprocedura(x):
  for i in range(5):
    print(x,i)
    yield


z=Zarzadca()
Mikrowatek(target=koprocedura('A')).start(z)
Mikrowatek(target=koprocedura('B')).start(z)
z.run()
