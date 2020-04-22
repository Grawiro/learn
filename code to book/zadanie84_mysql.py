from random import randint
from mysql.connector import connect

    
def dodaj_ankiete(nazwa,kto,terminy):
  conn = connect(user='uzytkownik',password='haslo',database='baza')
  try:
    c=conn.cursor()
    while True:
      klucz = ''.join([chr(randint(97,122)) for i in range(16)])
      c.execute('SELECT klucz FROM ankiety WHERE klucz=%s',(klucz,))
      if c.fetchone()==None:
        break
    c.execute('INSERT INTO ankiety(nazwa,kto,terminy,klucz) VALUES(%s,%s,%s,%s);',(nazwa,kto,terminy,klucz))
    try:
      conn.commit()
      return klucz # zwrócona wartość None informuje o błędzie zapisu do bazy danych
    except:
      conn.rollback()
  finally:
    conn.close()


def dodaj_propozycje(kto,klucz,terminy):
  conn = connect(user='uzytkownik',password='haslo',database='baza')
  try:
    c=conn.cursor()
    c.execute('SELECT klucz FROM ankiety WHERE klucz=%s;',(klucz,))
    if c.fetchone():
      c.execute('SELECT klucz FROM propozycje WHERE klucz=%s AND kto=%s;',(klucz,kto))
      if c.fetchone():
        c.execute('UPDATE propozycje SET terminy=%s WHERE kto=%s AND klucz=%s',(terminy,kto,klucz))
      else:
        c.execute('INSERT INTO propozycje(kto,klucz,terminy) VALUES(%s,%s,%s);',(kto,klucz,terminy))   
    else:
      return 1
    try:
      conn.commit()
    except:
      conn.rollback()
  finally:
    conn.close()


def pobierz_propozycje(klucz):
  conn = connect(user='uzytkownik',password='haslo',database='baza')
  try:
    c=conn.cursor()
    c.execute('SELECT kto,terminy FROM propozycje WHERE klucz=%s;', (klucz,))
    res=c.fetchall()
  finally:
    conn.close()
  return res


def pobierz_ankiete(klucz):
  conn = connect(user='uzytkownik',password='haslo',database='baza')
  try:
    c=conn.cursor()
    c.execute('SELECT nazwa,kto,terminy FROM ankiety WHERE klucz=%s;',(klucz,))
    res=c.fetchone()
  finally:
    conn.close()
  return res
