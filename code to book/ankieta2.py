from zadanie93 import *
from zadanie84sqlitev1 import *
#from zadanie84mysql import *


def index(termin=None,nazwa=None,autor=None,send=''):
  if nazwa==None:
    return nowa_ankieta.format('')
  if termin == None:
    return nowa_ankieta.format(b'B\xc5\x82\xc4\x85d: Nale\xc5\xbcy wprowadzi\xc4\x87 co najmniej jeden pasuj\xc4\x85cy termin'.decode('utf8'))
  if nazwa == '':
    return nowa_ankieta.format(b'B\xc5\x82\xc4\x85d: Nale\xc5\xbcy wprowadzi\xc4\x87 nazw\xc4\x99 ankiety'.decode('utf8'))
  if autor == '':
    return nowa_ankieta.format(b'B\xc5\x82\xc4\x85d: Nale\xc5\xbcy wprowadzi\xc4\x87 imi\xc4\x99 i nazwisko autora ankiety'.decode('utf8'))
  if type(termin) == str:
    termin = [termin]
  s=20*['0']
  for i in termin:
    s[4*int(i[0])+int(i[1])]='1'
  s=''.join(s)
  klucz=dodaj_ankiete(nazwa,autor,s)
  return stworzono.format(klucz)
