from zadanie93 import *


def index(termin=None,nazwa=None,autor=None):
  if nazwa==None:
    return nowa_ankieta.format('')
  if termin == None:
    return nowa_ankieta.format(b'B\xc5\x82\xc4\x85d: Nale\xc5\xbcy wprowadzi\xc4\x87 co najmniej jeden pasuj\xc4\x85cy termin'.decode('utf8'))
  if nazwa == '':
    return nowa_ankieta.format(b'B\xc5\x82\xc4\x85d: Nale\xc5\xbcy wprowadzi\xc4\x87 nazw\xc4\x99 ankiety'.decode('utf8'))
  if autor == '':
    return nowa_ankieta.format(b'B\xc5\x82\xc4\x85d: Nale\xc5\xbcy wprowadzi\xc4\x87 imi\xc4\x99 i nazwisko autora ankiety'.decode('utf8'))
