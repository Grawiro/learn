x='abcd'
y='ABCD'


def f(indeksy):
  ix=iter(x)
  iy=iter(y)
  return ''.join([next(iy if j in indeksy else ix) for j in range(len(x)+len(y))])


import itertools as it
iterator = (f(i) for i in it.combinations(range(len(x)+len(y)),len(x)))

print([i for i in iterator])

