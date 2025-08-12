import mysql.connector

__conn=None

def get_sql_connection():
    global __conn
    if __conn==None:
        __conn=mysql.connector.connect(user='root',password='Neelakanta@MySQL',
                                                                host='127.0.0.1',database='grocery_store')
        
    return __conn
