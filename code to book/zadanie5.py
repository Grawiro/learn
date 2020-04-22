#coding = utf-8

# x,n - zmienne, w których zapisana jest podstawa i wykładnik

res=1
kw=x
while n:
  if n%2:
    res*=kw
  kw*=kw
  n/=2

# wynik w zmiennej res
  
#Uwaga: Obliczając dzielenie całkowitoliczbowe i resztę z dzielenia, dwa razy powtarzamy te same operacje. Funkcja wbudowana divmod pozwala znaleźć obie te wartości jednocześnie, dwukrotnie przyśpieszając algorytm:

res=1
kw=x
while n:
  n,m=divmod(n,2)
  if m:
    res*=kw
  kw*=kw

# wynik w zmiennej res

# Uwaga: Ponieważ dzielenie wykonujemy przez 2, a jest to podstawa zapisu binarnego, można zrealizować powyższy algorytm przez operacje bitowe. Resztę z dzielenia znajdujemy przez sprawdzanie ostatniego bitu - bitowe AND z liczbą 1, a dzielenie całkowite przez 2 to przesunięcie bitowe <<:

res=1
kw=x
while n:
  if n&1:
    res*=kw
  kw*=kw
  n>>=1 # równoważne: n=n>>1

# wynik w zmiennej res
