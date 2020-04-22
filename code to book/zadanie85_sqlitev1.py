from datetime import datetime
from sqlite3 import connect


def dodaj_pytanie(tresc,kto):
  with connect('/var/www/baza.db') as conn:
    c=conn.cursor()
    c.execute('INSERT INTO pytania VALUES(?,?,?);',(tresc,kto,str(datetime.now())))
    try:
      conn.commit()
    except:
      conn.rollback()

      
def dodaj_odpowiedz(tresc,kto,pytanie):
  with connect('/var/www/baza.db') as conn:
    c=conn.cursor()
    c.execute('INSERT INTO odpowiedzi VALUES(?,?,?,?);',(tresc,kto,str(datetime.now()),pytanie))
    try:
      conn.commit()
    except:
      conn.rollback()

      
def pobierz_odpowiedzi(pytanie):
  with connect('/var/www/baza.db') as conn:
    c=conn.cursor()
    c.execute('SELECT * FROM odpowiedzi WHERE pytanie=?;', (pytanie,))
    res=c.fetchall()
  return res

  
def pobierz_pytanie(pytanie):
  with connect('/var/www/baza.db') as conn:
    c=conn.cursor()
    c.execute('SELECT rowid,* FROM pytania WHERE rowid=?;', (pytanie,))
    res=c.fetchone()
  return res

  
def wyszukaj_pytania(lancuch):
  with connect('/var/www/baza.db') as conn:
    c=conn.cursor()
    c.execute('SELECT ROWID,* FROM pytania WHERE tresc LIKE ?;',(r'%'+lancuch+r'%',))
    res = c.fetchall()
  return res
