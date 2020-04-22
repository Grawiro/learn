reduce(lambda a,b:a[:-1]+[a[-1]+sep+b] if a[-1].count('(')!=a[-1].count(')')  else a+[b],x[1:],[x[0]])
  