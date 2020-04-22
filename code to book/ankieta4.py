from zadanie93 import *
from zadanie84sqlitev1 import *
#from zadanie84mysql import *

def index(klucz):
  ank = pobierz_ankiete(klucz)
  propozycje = pobierz_propozycje(klucz)
  return ankieta.format(ank[0],ank[1],naglowek(ank[2])+''.join([wiersz(i[0],i[1],ank[2]) for i in propozycje])+form(ank[2]))
