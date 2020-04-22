from datetime import datetime
from mysql.connector import connect

    
def dodaj_pytanie(tresc,kto):
  conn = connect(user='uzytkownik',password='haslo',database='baza')
  try:
    c=conn.cursor()
    c.execute('INSERT INTO pytania(tresc,kto,kiedy) VALUES(%s,%s,%s);',(tresc,kto,str(datetime.now())))
    try:
      conn.commit()
    except:
      conn.rollback()
  finally:
    conn.close()

    
def dodaj_odpowiedz(tresc,kto,pytanie):
  conn = connect(user='uzytkownik',password='haslo',database='baza')
  try:
    c=conn.cursor()
    c.execute('INSERT INTO odpowiedzi(tresc,kto,kiedy,pytanie) VALUES(%s,%s,%s,%s);',(tresc,kto,str(datetime.now()),pytanie))
    try:
      conn.commit()
    except:
      conn.rollback()
  finally:
    conn.close()

    
def pobierz_odpowiedzi(pytanie):
  conn = connect(user='uzytkownik',password='haslo',database='baza')
  try:
    c=conn.cursor()
    c.execute('SELECT tresc,kto,kiedy,pytanie FROM odpowiedzi WHERE pytanie=%s;', (pytanie,))
    res=c.fetchall()
    return res
  finally:
    conn.close()

    
def pobierz_pytanie(pytanie):
  conn = connect(user='uzytkownik',password='haslo',database='baza')
  try:
    c=conn.cursor()
    c.execute('SELECT rowid,* FROM pytania WHERE rowid=?;', (pytanie,))
    res=c.fetchone()
    return res
  finally:
    conn.close()

    
def wyszukaj_pytania(lancuch):
  conn = connect(user='uzytkownik',password='haslo',database='baza')
  try:
    c=conn.cursor()
    c.execute('SELECT * FROM pytania WHERE tresc LIKE %s;',(r'%'+lancuch+r'%',))
    res=c.fetchall()
    return res
  finally:
    conn.close()
