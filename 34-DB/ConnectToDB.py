import mysql.connector

admindbconfig = { 'host': 'database-2.c9cuny3xk7pk.eu-west-1.rds.amazonaws.com',
'user': 'admin',
'password': 'Python2022',
'database': 'vsearchlogDB', }


dbconfig = { 'host': 'database-2.c9cuny3xk7pk.eu-west-1.rds.amazonaws.com',
'user': 'user',
'password': 'password',
'database': 'vsearchlogDB', }



conn = mysql.connector.connect(**dbconfig)

cursor = conn.cursor()

_SQL = """show tables"""
cursor.execute(_SQL)


res = cursor.fetchall()
print(res)

##
_SQL = """describe log"""
cursor.execute(_SQL)
res = cursor.fetchall()
print(res)

for row in res:
    print(row)


# prosty insert
_SQL = """insert into log
(phrase, letters, ip, browser_string, results)
values
('hitch-hiker', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}")"""

cursor.execute(_SQL)

## parametryzowany insert
_SQL = """insert into log
(phrase, letters, ip, browser_string, results)
values
(%s, %s, %s, %s, %s)"""
cursor.execute(_SQL, ('hitch-hiker', 'xyz', '127.0.0.1', 'Safari', 'set()'))

## pobranie rekordów
conn.commit()
_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
       print(row)

# Zamkniecie polaczenia
cursor.close()
conn.close()
