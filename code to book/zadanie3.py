n=169
d=1
pierwsza=True
while d*d<=n:
  d+=1
  if n%d==0:
    pierwsza=False
    break
print(pierwsza)
