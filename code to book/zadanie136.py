from itertools import product


def podzialy_grafu(G,N):
  n=len(G)
  for i in product(range(N),repeat=n-1):
    i=[0]+list(i)
    d=[[] for j in range(N)]
    for j in range(n):
      d[i[j]].append(j)
    m=0
    for j in d:
      if j==[] or j[0]<m:
        break
      else:
        m=j[0]
    else:
      if all([podgraf(G,j) for j in d]):
        yield d
