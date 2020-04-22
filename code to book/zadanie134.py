from itertools import starmap

def podgraf(G,l):
  G = list(map(list,G))
  l = list(l)
  x=l[0]
  l=l[1:]
  while l:
    for i in l:
      if G[x][i]:
        G[x]=list(starmap(int.__or__,zip(G[x],G[i])))
        l.remove(i)
        break
    else:
      return False
  return True
