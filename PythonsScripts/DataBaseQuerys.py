import sqlite3 as dataBase

path = "../Database/Options.db"

def dataBaseConn():

    dbConn = dataBase.connect(path)
    cursor = dbConn.cursor()

    return dbConn, cursor

def createDataBase():
    cmd = """CREATE TABLE IF NOT EXISTS Preloads(
    preloadID integer primary key,
    Local text,
    finalLocal text,
    type text
    )"""

    dbcursor.execute(cmd)
    dbConn.commit()

    cmd = """INSERT INTO Preloads VALUES(
    '3',
    'Desktop',
    'Documents',
    '.py'
    )"""

    dbcursor.execute(cmd)
    dbConn.commit()

    temp = dbcursor.execute("""SELECT * from Preloads""")
    print(temp.fetchall())

dbConn, dbcursor = dataBaseConn()