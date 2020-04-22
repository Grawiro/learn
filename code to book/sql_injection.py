from sqlite3 import connect


conn=connect('test.db')
c=conn.cursor()

user=input('Nazwa uzytkownika:')
pswd=input('Haslo:')
sql='SELECT user FROM users WHERE user="%s" AND passwd="%s";' % (user,pswd)
print(sql)
c.execute(sql)
u=c.fetchone()
if u==None:
  print('Niepoprawny login')
else:
  u=u[0]
  print('Zalogowano jako: ', u)

conn.close()
