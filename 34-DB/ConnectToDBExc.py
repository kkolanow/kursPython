import mysql.connector


user2_dbconfig = {
'host': 'database-2.c9cuny3xk7pk.eu-west-1.rds.amazonaws.com',
'user': 'user2',
'password': 'password',
'database': 'vsearchlogDB', }


conn = mysql.connector.connect(**user2_dbconfig)

cursor = conn.cursor()

_SQL = """show tables"""
cursor.execute(_SQL)


res = cursor.fetchall()
print(res)

# ##
_SQL = """describe log"""
cursor.execute(_SQL)
res = cursor.fetchall()
print(res)

for row in res:
    print(row)
#
#
# prosty insert
_SQL = """insert into log
(phrase, letters, ip, browser_string, results)
values
('REQ-1243343', 'aeiou', '127.0.0.1', 'Chrome', "{'e', 'i'}")"""

cursor.execute(_SQL)
#
# ## parametryzowany insert
_SQL = """insert into log
(phrase, letters, ip, browser_string, results)
values
(%s, %s, %s, %s, %s)"""
cursor.execute(_SQL, ('SANITIZED', 'xyz', '127.0.0.1', 'Safari', 'GET'))
#
# ## pobranie rekordów
conn.commit()
_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
       print(row)



# Zamkniecie polaczenia
cursor.close()
conn.close()
