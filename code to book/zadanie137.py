graf=((0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0),
      (1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0),
      (0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0),
      (0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0),
      (1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0),
      (1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0),
      (0,1,1,0,0,1,0,1,0,0,0,1,0,0,0,0),
      (0,0,1,1,0,0,1,0,1,0,0,1,1,0,0,0),
      (0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0),
      (0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0),
      (0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,0),
      (0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0),
      (0,0,0,0,0,0,0,1,1,0,0,1,0,1,1,1),
      (0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1),
      (0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1),
      (0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0),  
      )
values = (1.710,2.308,1.440,1.189,1.018,3.475,2.086, 5.349,2.140,2.904,0.996,2.494,1.257,2.128,4.571, 3.373)
nazwy = ['zachodniopomorskie','pomorskie','warmińsko-mazurskie','podlaskie','lubuskie','wielkopolskie','kujawsko-pomorskie','mazowieckie','lubelskie','dolnośląskie','opolskie','łódzkie','świętokrzyskie','podkarpackie','śląskie','małopolskie']

l=[i for i in podzialy_grafu(graf,4)]    # dłuższe obliczenia!

def min_obszar(podzial):
  return min([sum(map(values.__getitem__,p)) for p in podzial])

def var(podzial):
  l = [sum(map(values.__getitem__,i)) for i in podzial]
  av = sum(l)/len(l)
  return sum([(i - av)**2 for i in l])

print(sorted(l,key=min_obszar,reverse=True)[:10])
print(sorted(l,key=var)[:10])

print(map(lambda x:[map(nazwy.__getitem__,i) for i in x],sorted(p,key=min_obszar,reverse=True)[:10]))
print(map(lambda x:[map(nazwy.__getitem__,i) for i in x],sorted(p,key=var)[:10]))
