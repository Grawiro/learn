with open('ex.txt') as f:
  l=filter(bool,map(lambda i:i.split('#',1)[0].strip(),f))
  