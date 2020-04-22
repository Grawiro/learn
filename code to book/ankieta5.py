from zadanie93v1 import *
from zadanie84sqlite import *
#from zadanie84mysql import *


def index(klucz,uczestnik='',termin=None):
  ank = pobierz_ankiete(klucz)
  propozycje = pobierz_propozycje(klucz)
  if uczestnik and termin:
    if type(termin) == str:
      termin = [termin]
    s=20*['0']
    for i in termin:
      s[4*int(i[0])+int(i[1])]='1'
    s=''.join(s)
    dodaj_propozycje(uczestnik,klucz,s)
  ank = pobierz_ankiete(klucz)
  propozycje = pobierz_propozycje(klucz)
  return ankieta.format(ank[0],ank[1],naglowek(ank[2])+''.join([wiersz(i[0],i[1],ank[2]) for i in propozycje])+form(ank[2]),klucz)
