import mysql.connector

create = False
insert = False

try:
    # conection to database if args default can be skip host/user/passwd
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='', database='test')
    # co ask the database
    cursor = mydb.cursor()

    if create:
        query = 'create table tested (' \
                'id int(3) NOT NULL AUTO_INCREMENT, ' \
                'first_name varchar(14) NOT NULL, ' \
                'last_name varchar(14) NOT NULL, ' \
                'gender enum("M","F") NOT NULL, ' \
                'PRIMARY KEY (id)' \
                ')'
        # to ask database
        cursor.execute(query)

    if insert:
        query = 'insert into tested (first_name, last_name, gender) values ("%s", "%s", "%s");'
        some_people = ('anna', 'lars', 'F')
        cursor.execute(query % some_people)
        # this return add id
        print('last add id:', cursor.lastrowid)
        # this accept changes must have to insert and update
        mydb.commit()

    query = 'select first_name, last_name from tested;'
    # the return values is save in cursor
    cursor.execute(query)
    # show return cloumn names
    print(cursor.column_names)
    for i in cursor:
        # which row I am in
        print('row:', cursor.rowcount, ' -> ', i[0], ' ', i[1], sep='')

except mysql.connector.Error as err:
    print('error:', err)
finally:
    mydb.close()
