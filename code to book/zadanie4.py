# x,s - zmienne, w których zdefiniowany jest ciąg i podciąg
l=[]
i=-1
while s in x:
  j=x.index(s)
  x=x[j+1:]
  i+=j+1
  l.append(i)
  
