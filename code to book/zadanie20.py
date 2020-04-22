def f(l,pref=''):
  return sum([f(l[i],pref+str(i)) for i in xrange(len(l))],[]) if type(l)==list else [(l,pref)]
