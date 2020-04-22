s=[(int(i[0]),i[1].rsplit('/',1)[-1]) for i in s]
r=0
while (len(s)>2) and s[-1][0]+r < s[0][0] and s[-1][0]<s[0][0]/40:
  r+=s.pop()[0]
if r:
  s.append((r,'reszta'))
