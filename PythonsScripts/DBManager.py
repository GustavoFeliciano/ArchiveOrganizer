import json
import os
import _sqlite3 as dataBase
import DataBaseQuerys as dbQuery

#Guardar configurações, como:
#Pasta base
#Pasta alvo
#Tipos de arquivo para organização
#Produzir requisições para o software do tipo:
#Nome do arquivo - Local de onde está - Local para onde vai

dataBase



#Função de salvamento de Preload
#Mudar função de salvamento para a versão com o preload dos preloads
def SavePreloadData(Data):
    with open("../Json/saveDB.json", "r") as readJson:
        jsonArchiveDict = json.load(readJson)
        readJson.close()

    count = len(list(jsonArchiveDict)) - 1

    preloadData = {
            "Name": Data[0],
            "Type": Data[1],
            "Local": Data[2],
            "finalLocal": Data[3]
        }

    jsonArchiveDict["Preload"+str(count)] = preloadData

    with open("../Json/saveDB.json","w") as writeJson:
        json.dump(jsonArchiveDict, writeJson)
        writeJson.close()

def TestDB():

    dbQuery.createDataBase()

#Função de carregamento de Preload
def LoadPreloadData(preloadName):
    with open("../Json/saveDB.json", "r") as readJson:
        jsonArchiveDict = json.load(readJson)
        readJson.close()

    return jsonArchiveDict[preloadName]


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