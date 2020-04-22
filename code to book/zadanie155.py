def srednia():
  def wew(x):
    try:
      wew.s+=x
      wew.n+=1
    except:
      pass
    return wew.s/wew.n if wew.n else None
  wew.s=0
  wew.n=0
  def reset():
    wew.s=0.
    wew.n=0
  wew.reset=reset
  return wew
  
s1=srednia()
s2=srednia()

print(s1(1))
print(s1(2))
print(s1(3))
print(s2(1))
print(s2(2))
s1.reset()
print(s1(10))
print(s2(6))
s2.reset()
print(s1(2))
print(s2(1))
