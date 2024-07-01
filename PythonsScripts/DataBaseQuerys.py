import sqlite3 as dataBase

path = "../Database/Options.db"

def dataBaseConn():

    dbConn = dataBase.connect(path)
    cursor = dbConn.cursor()

    return dbConn, cursor

def createDataBase():

    cmd = """CREATE TABLE IF NOT EXISTS Preloads(
    preloadID INTEGER NOT NULL,
    preloadTempID INTEGER,
    Local TEXT,
    finalLocal TEXT,
    Type text
    )"""

    dbcursor.execute(cmd)
    dbConn.commit()

def savePreloadDB(jsonArchiveTemp):

    dataList = []
    tempTuple = ()
    countID = 1

    while True:

        try:
            cmd = """SELECT preloadID FROM Preloads
            WHERE preloadID=?
            """
            dbcursor.execute(cmd, (countID,))
            if dbcursor.fetchone() == None:
                break
            else:
                countID += 1 
        except Exception as e:
            print("erro: "+str(e))

    cmd = """INSERT INTO Preloads(preloadID, preloadTempID, Local, finalLocal, Type)
    VALUES(?,?,?,?,?)
    """
    for x in jsonArchiveTemp.keys():

        tempTuple = (
            int(countID),
            int(str(x)[7:]),
            str(jsonArchiveTemp[x]['local']),
            str(jsonArchiveTemp[x]['finalLocal']),
            str(jsonArchiveTemp[x]['type'])
            )
        dataList.append(tempTuple)

    dbcursor.executemany(cmd,dataList)
    dbConn.commit()

def loadPreloadDB():

    cmd = """SELECT preloadID FROM Preloads
    WHERE 
    """

    dbcursor.execute(cmd)
    for x in dbcursor.fetchall():
        print(x)


dbConn, dbcursor = dataBaseConn()