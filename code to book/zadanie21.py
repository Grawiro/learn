def pole(*args):
  if len(args)==1:
    return args[0]**2
  elif len(args)==2:
    return args[0]*args[1]
  elif len(args)==3:
    return args[0]*(args[1]+args[2])/2.0
  