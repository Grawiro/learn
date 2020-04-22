import itertools as it


lancuchy=['ab','AB','123','xy']
dlugosci=list(map(len,lancuchy))


def wypelnij(lista_podstawien,wartosc,ile):
  pozycje_None = [i for i in range(len(lista_podstawien)) if lista_podstawien[i]==None]
  return ([wartosc if i in k else lista_podstawien[i] for i in range(len(lista_podstawien))] for k in it.combinations(pozycje_None,ile))


listy_podstawien = [[None]*sum(dlugosci)]
for j in range(len(dlugosci)):
  listy_podstawien = it.chain(*(wypelnij(i,j,dlugosci[j]) for i in listy_podstawien))


def f(indeksy):
  iteratory=list(map(iter,lancuchy))
  return ''.join([next(iteratory[indeksy[j]]) for j in range(sum(dlugosci))])


iterator = (f(i) for i in listy_podstawien)

print([i for i in iterator])


