from zadanie94v3 import *
from zadanie85sqlitev1 import *
#from zadanie85mysql import *

def index(akc='',szukaj='',np='',autor='',num_p='', no='', do=''):
  body = szukaj_form
  if (akc == 'Wyszukaj pytania' or akc == 'Powr\xc3\xb3t') and szukaj and not do:
    body+='\n'.join([p_form.format(*(list(i)+[szukaj])) for i in wyszukaj_pytania(szukaj)])
  elif akc == 'Nowe pytanie':
    body = np_form
  elif akc == 'Dodaj pytanie' and np and autor:
    dodaj_pytanie(np,autor)
  elif akc == 'Poka\xc5\xbc odpowiedzi' or (akc == 'Powr\xc3\xb3t' and do):
    try:
      num_p = int(num_p)
    except:
      num_p=''
    if num_p:
      argumenty = list(pobierz_pytanie(num_p))+['\n'.join([odp_temp.format(*i) for i in pobierz_odpowiedzi(num_p)]),szukaj]
      body = po_form.format(*argumenty)
  elif akc == 'Dodaj odpowied\xc5\xba':
    try:
      num_p = int(num_p)
    except:
      num_p=''
    if num_p:
      argumenty=list(pobierz_pytanie(num_p))
      if autor and no:
        dodaj_odpowiedz(no,autor,num_p)
        argumenty+=['\n'.join([odp_temp.format(*i) for i in pobierz_odpowiedzi(num_p)]),szukaj]
        body = po_form.format(*argumenty)
      else:
        argumenty.append(szukaj)
        body = do_form.format(*argumenty)
  
  return main.format(body)
