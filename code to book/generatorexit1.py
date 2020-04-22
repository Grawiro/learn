def zapisz(sciezka):
  f=open(sciezka,'w')
  while True:
    try:
      x=yield
      f.write(str(x))
    except GeneratorExit:
      print('teraz dziala metoda .close')
      f.close()
      break


konsument=zapisz('1.txt')
konsument.send(None)
for i in range(5):
  konsument.send(i)
for i in range(5):
  konsument.send(i)

#konsument = 2

print('Koniec')
