ank = ('Kurs python','Gniewomir Sarbicki','11001010011101000110')
propozycje = [('Student Pierwszy','11100011011110001011'),('Student Drugi','10101001001111000000')]
  
from zadanie93 import *
  
def index():
  return ankieta.format(ank[0],ank[1],naglowek(ank[2])+''.join([wiersz(i[0],i[1],ank[2]) for i in propozycje])+form(ank[2]))
