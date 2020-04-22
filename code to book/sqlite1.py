from sqlite3 import connect

conn=connect('test.db')
c=conn.cursor()

c.execute('CREATE TABLE tablica(x,y);')
c.execute('INSERT INTO tablica VALUES("Ala",2);')
c.execute('INSERT INTO tablica VALUES("żółw",3);')
c.execute('SELECT * FROM tablica;')
for i in c:
  print(i)
c.execute('SELECT * FROM tablica;')
print(c.fetchall())
c.execute('SELECT * FROM tablica;')
while True:
  i=c.fetchone()
  if i==None:
    break
  print(i)
try:
  conn.commit()
except:
  conn.rollback()
finally:
  conn.close()
