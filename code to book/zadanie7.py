zamien=(a<b)
if zamien:
  a,b=b,a
k=(1,0,0,1)
while b:
  a,d,b=[b]+list(divmod(a,b))
  k = (k[2], k[3], k[0] - d*k[2], k[1] - d*k[3])
if zamien:
  x,y=k[1],k[0]
else:
  x,y=k[0],k[1]
# a = NWD
