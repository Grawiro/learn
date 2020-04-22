from random import randint
from sqlite3 import connect


def dodaj_ankiete(nazwa,kto,terminy):
  with connect('/var/www/baza.db') as conn:
    c=conn.cursor()
    while True:
      klucz = ''.join([chr(randint(97,122)) for i in range(16)])
      c.execute('SELECT klucz FROM ankiety WHERE klucz=?',(klucz,))
      if c.fetchone()==None:
        break
    c.execute('INSERT INTO ankiety(nazwa,kto,terminy,klucz) VALUES(?,?,?,?);',(nazwa,kto,terminy,klucz))
    try:
      conn.commit()
      return klucz # zwrócona wartość None informuje o błędzie zapisu do bazy danych
    except:
      conn.rollback()

      
def dodaj_propozycje(kto,klucz,terminy):
  with connect('/var/www/baza.db') as conn:
    c=conn.cursor()
    c.execute('SELECT klucz FROM ankiety WHERE klucz=?;',(klucz,))
    if c.fetchone():
      c.execute('SELECT klucz FROM propozycje WHERE klucz=? AND kto=?;',(klucz,kto))
      if c.fetchone():
        c.execute('UPDATE propozycje SET terminy=? WHERE kto=? AND klucz=?',(terminy,kto,klucz))
      else:
        c.execute('INSERT INTO propozycje(kto,klucz,terminy) VALUES(?,?,?);',(kto,klucz,terminy))
    else:
      return 1
    try:
      conn.commit()
    except:
      conn.rollback()

      
def pobierz_propozycje(klucz):
  with connect('/var/www/baza.db') as conn:
    c=conn.cursor()
    c.execute('SELECT kto,terminy FROM propozycje WHERE klucz=?;', (klucz,))
    res = c.fetchall()
  return res

  
def pobierz_ankiete(klucz):
  with connect('/var/www/baza.db') as conn:
    c=conn.cursor()
    c.execute('SELECT nazwa,kto,terminy FROM ankiety WHERE klucz=?;',(klucz,))
    res=c.fetchone()
  return res
