


import mysql.connector

class UseDatabase:
    def __init__(self, config: dict) -> None:
        self.configuration = config
    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor
    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        print(cursor.statement)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


user2_dbconfig = {
'host': 'database-2.c9cuny3xk7pk.eu-west-1.rds.amazonaws.com',
'user': 'user2',
'password': 'password',
'database': 'vsearchlogDB', }



with UseDatabase(user2_dbconfig) as cursor:
        _SQL = """insert into log
            (phrase, letters, ip, browser_string, results)
            values
            (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (
        'phrase',
        'letters',
        '127.0.0.1',
        'wget',
        "anything", ))










