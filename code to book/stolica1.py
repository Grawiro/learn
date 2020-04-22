from stolica import stolica
from time import time
  
panstwa=['Polska','Niemcy','Litwa','Szwecja','Estonia','Norwegia','Finlandia','Łotwa']
  
t=time()
for p in panstwa:
  print '%s: %s' % (p,stolica(p))
print 'Czas wykonania:', time()-t
