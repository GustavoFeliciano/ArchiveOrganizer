import json
import os
import _sqlite3 as dataBase
import DataBaseQuerys as dbQuery
import asyncio

#Função de salvamento de Preload
def SavePreloadData():
    dbQuery.savePreloadDB(loadTempData())

#função de carregamento do preloadPreview para o front end
def loadPreloadPreviewData():
    
    jsonPreviewDict = dbQuery.loadPreloadPreviewDB()

    return jsonPreviewDict

#Função de carregamento de Preload
def LoadPreloadData(preloadID):

    #dbQuery.test()
    jsonTempPreload = dbQuery.loadPreloadDB(preloadID)
    writeTempData(jsonTempPreload)

#Função de sobrescrição dos dados do preloadTemp 
def editPreloadData(jsonArchiveDict, preloadName, keyId, Data):
    jsonArchiveDict[preloadName][keyId] = Data
    writeTempData(jsonArchiveDict)

#Função de adição de dados de Preload
def addPreloadData(jsonArchiveDict, data):
    jsonArchiveDict["Preload"+str(len(jsonArchiveDict)-1)] = data
    writeTempData(jsonArchiveDict)

#função de criação de um novo preload
def createPreloadData():
    tempArchive = loadTempData()
    jsonArchiveDict = {
        "local": "",
        "finalLocal":"",
        "type":"",
    } 
    tempArchive["Preload" + str(len(tempArchive)+1)] = jsonArchiveDict
    writeTempData(tempArchive)

    return tempArchive

#Função de delete de um preload
def deletePreloadData(preloadIndex):
    
    tempArchive = loadTempData()
    tempArchive.pop("Preload" + str(preloadIndex))

    writeTempData(tempArchive)

def deleteTempData():

    tempArchive = loadTempData()
    tempArchive.clear()

    writeTempData(tempArchive)


#função de retorno do preloadTemp
def loadTempData():
    with open("../Json/tempDB.json", "r") as readJson:
        jsonArchiveDict = json.load(readJson)
        readJson.close()

    return jsonArchiveDict

#função de escrita do preloadTemp
def writeTempData(tempArchive):

    try:
        with open("../Json/tempDB.json", "w") as writeJson:
            json.dump(tempArchive, writeJson)
            writeJson.close()
    except:
        os.system('clear')
        print("Não foi possível acessar o documento base do programa")

#Função assíncrona para validar arquivo json
async def jsonValidator():
    
    jsonArchiveDict = loadTempData()
    await asyncio.sleep(2)
    for x in jsonArchiveDict.keys():
            for y in jsonArchiveDict[x].keys():
                if jsonArchiveDict[x][y] == None or jsonArchiveDict[x]["local"] == '':
                    return False
    return True









tempArchive = {
    "Preload1": {
        "Local": "",
        "finalLocal":"",
        "Type":"",

        "tempArchive01": {
            "Name": "",
        },
        "tempArchive02": {
            "Name": "",
        }
    }    
}