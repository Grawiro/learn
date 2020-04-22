from itertools import combinations
    
def podgrafy(G,N):
  for i in combinations(range(len(G)),N):
    if podgraf(G,i):
      yield i
