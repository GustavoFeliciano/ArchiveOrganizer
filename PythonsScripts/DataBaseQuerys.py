import sqlite3 as dataBase
from tkinter import *

Window = Tk()

Button(Window, text="Opa")

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
    
    countID = howManyIDs()
    countID+=1

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

def loadPreloadPreviewDB():
    
    jsonPreviewArchive = {}
    jsonTempPreviewArchive = {}

    countID = howManyIDs()
    print(countID)
    for x in range(1, countID):
        cmd = """SELECT preloadTempID, Local, finalLocal, Type FROM Preloads
    WHERE preloadID=?
    """
        dbcursor.execute(cmd,(x,))
        for y in dbcursor.fetchmany(3):
            jsonTempPreviewArchive["Preload"+str(y[0])] = {
                    "local": y[1],
                    "finalLocal": y[2],
                    "type": y[3]
                }

        jsonPreviewArchive["preloadID"+str(x)] = jsonTempPreviewArchive

    print(jsonPreviewArchive)       

    return jsonPreviewArchive

    

def howManyIDs():

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

    return countID

dbConn, dbcursor = dataBaseConn()