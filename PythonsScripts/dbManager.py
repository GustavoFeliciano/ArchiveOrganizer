import json
import os

#Guardar configurações, como:
#Pasta base
#Pasta alvo
#Tipos de arquivo para organização
#Produzir requisições para o software do tipo:
#Nome do arquivo - Local de onde está - Local para onde vai

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

#Função de carregamento de Preload
def LoadPreloadData(preloadName):
    with open("../Json/saveDB.json", "r") as readJson:
        jsonArchiveDict = json.load(readJson)
        readJson.close()

    return jsonArchiveDict[preloadName]

#função de retorno do preloadTemp
def LoadTempData():
    with open("../Json/tempDB.json", "r") as readJson:
        jsonArchiveDict = json.load(readJson)
        readJson.close()

    return jsonArchiveDict


#Função de sobrescrição dos dados do preloadTemp 
def editPreloadData(jsonArchiveDict, preloadName, keyId, Data):
    jsonArchiveDict[preloadName][keyId] = Data
    with open("../Json/tempDB.json", "w") as writeJson:
        json.dump(jsonArchiveDict, writeJson)
        writeJson.close()

#Função de adição de dados de Preload
def addPreloadData(jsonArchiveDict, data):
    jsonArchiveDict["Preload"+str(len(jsonArchiveDict)-1)] = data
    with open("../Json/tempDB.json", "w") as writeJson:
        json.dump(jsonArchiveDict, writeJson)
        writeJson.close()

#função de criação de um novo preload
def createPreloadData():
    tempArchive = LoadTempData()
    jsonArchiveDict = {
        "local": "",
        "finalLocal":"",
        "type":"",
    } 
    tempArchive["Preload" + str(len(tempArchive)+1)] = jsonArchiveDict
    with open("../Json/tempDB.json", "w") as writeJson:
        json.dump(tempArchive, writeJson)
        writeJson.close()

    return tempArchive

#Função de delete de um preload
def deletePreloadData(preloadIndex):
    
    tempArchive = LoadTempData()
    tempArchive.pop("Preload" + str(preloadIndex))

    with open("../Json/tempDB.json", "w") as writeJson:
        json.dump(tempArchive, writeJson)
        writeJson.close()


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