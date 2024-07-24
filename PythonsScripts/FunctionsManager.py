#imports
import os
import FrontEnd
import DBManager
import subprocess
import asyncio
from ConstantVariables import *
#def de fechamento do programa
def ExitSoftware():
    os.system('clear')
    print('Finalizando programa...')
    os.system('exit')

#def de recepção de input de comando
def InputCommands(actualScreenFun):
    screenCode, Commandlimit = actualScreenFun()
    Comm = int(input("Insira aqui:"))
    while Comm > Commandlimit or Comm < 1:
        FrontEnd.ErrorInputInterface()
        screenCode, Commandlimit = actualScreenFun()
        Comm = int(input("Insira aqui:"))
    return screenCode, Comm

#def de recepção de input
def InputReceive():
    inputData = input("Insira aqui:")
    return str(inputData)

#Preciso construir o código de validação de argumentos para cada tipo de input que
#essa função pode receber, criando isso em outro arquivo e talvez um arquivo .txt
#de configuração que vai estar em binário

#defs de mudança de telas principais
def ChangeScreenProcess(screenCode, Command):
    match screenCode:
        case 'MainInterface':
            MainChosenScreen(Command)
        case 'SOInterface':
            ShowOptionsCommand(Command)

        #case do menu de funções
        case 'Options':
            OptionChosenScreen(Command)
        case 'SOInterface':
            ShowOptionsCommand(Command)
        case 'CBFolder':
            CBFolderCommand(Command)
        case 'CBRepeat':
            CBRepeatCommand(Command)
        case 'CFFolder':
            CFFolderCommand(Command)
        case 'CFRepeat':
            CFRepeatCommand(Command)
        case 'CTypeInterface':
            CTypeCommand(Command)
        case 'CTypeRepeat':
            CTypeRepeatCommand(Command)
        case 'CPInterface':
            CreatPreloadCommand(Command)
        case 'DPInterface':
            DeletePreloadCommand(Command)
        case 'DPRepeat':
            DPRepeatCommand(Command)
        
        #Funções do banco de dados (menu de opções)
        case 'DTAInterface':
            DTACommand(Command)
        case 'SaveDBInterface':
            SDBCommand(Command)
        case 'LPDBInterface':
            LDBCommand(Command)

#Inputs da função Main                
def MainChosenScreen(Command):
    match Command:
        case 1:
            jsonIsValid = asyncio.run(JsonValidator_CORROUTINE())

            if jsonIsValid[0] == True:
                fileIsValid =asyncio.run(FileValidator_CORROUTINE())
                if fileIsValid[0] == True:

                    userFileIsValid = UserValidation()
                    print("Passou da função")
                    if userFileIsValid: asyncio.run(MoveFiles_CORROUTINE())

                else:
                    FrontEnd.FileINVInterface()
            else:
                FrontEnd.JsonINVInterface()
            
            screenCode, command = InputCommands(FrontEnd.MainInterface)
            ChangeScreenProcess(screenCode, command)

        case 2:
            screenCode, command = InputCommands(FrontEnd.OptionsInterface)
            ChangeScreenProcess(screenCode, command)
            screenCode, command = InputCommands(FrontEnd.MainInterface)
            ChangeScreenProcess(screenCode, command)

        case 3:
            screenCode, command = InputCommands(FrontEnd.SOInterface)
            ChangeScreenProcess(screenCode, command)
            screenCode, command = InputCommands(FrontEnd.MainInterface)
            ChangeScreenProcess(screenCode, command)

        case 4:
            ExitSoftware()   

#Inputs da função de Opções
def OptionChosenScreen(Command):
    match Command:
        case 1:
            screenCode, command = InputCommands(FrontEnd.SOInterface)
            ChangeScreenProcess(screenCode, command)
            screenCode, command = InputCommands(FrontEnd.OptionsInterface)
            ChangeScreenProcess(screenCode, command)

        case 2:
            screenCode, command = InputCommands(FrontEnd.CFFolderInterface)
            ChangeScreenProcess(screenCode, command)
            screenCode, command = InputCommands(FrontEnd.OptionsInterface)
            ChangeScreenProcess(screenCode, command)

        case 3:
            screenCode, command = InputCommands(FrontEnd.CBFolderInterface)
            ChangeScreenProcess(screenCode, command)
            screenCode, command = InputCommands(FrontEnd.OptionsInterface)
            ChangeScreenProcess(screenCode, command)

        case 4:
            screenCode, command = InputCommands(FrontEnd.CTypeInterface)
            ChangeScreenProcess(screenCode, command)
            screenCode, command = InputCommands(FrontEnd.OptionsInterface)
            ChangeScreenProcess(screenCode, command)

        case 5:
            screenCode, command = InputCommands(FrontEnd.CreatePInterface)
            ChangeScreenProcess(screenCode, command)
            screenCode, command = InputCommands(FrontEnd.OptionsInterface)
            ChangeScreenProcess(screenCode, command)

        case 6:
            screenCode, command = InputCommands(FrontEnd.DPInterface)
            ChangeScreenProcess(screenCode, command)
            screenCode, command = InputCommands(FrontEnd.OptionsInterface)
            ChangeScreenProcess(screenCode, command)

        case 7:
            screenCode, command = InputCommands(FrontEnd.DTAInterface)
            ChangeScreenProcess(screenCode, command)
            screenCode, command = InputCommands(FrontEnd.OptionsInterface)
            ChangeScreenProcess(screenCode, command)

        case 8:
            screenCode, command = InputCommands(FrontEnd.SaveDBInterface)
            ChangeScreenProcess(screenCode, command)
            screenCode, command = InputCommands(FrontEnd.OptionsInterface)
            ChangeScreenProcess(screenCode, command)

        case 9:
            screenCode, command = InputCommands(FrontEnd.LPDBInterface)
            ChangeScreenProcess(screenCode, command)
            screenCode, command = InputCommands(FrontEnd.OptionsInterface)
            ChangeScreenProcess(screenCode, command)
        case 10:
            pass
            
        case 11:
            ExitSoftware()

#Funções de validação

def UserValidation():
    close = False
    con = False

    FrontEnd.UserValidationInterface()
    FrontEnd.UserValidationInputInterface()
    command = InputReceive()
    
    while True:

        match command:
            case 1:
                return True
            case 2:
                return False
            case 3:
                pass

        FrontEnd.UserValidationInterface()
        DBManager.DeleteFileData(InputReceive())

        
        while True:

            FrontEnd.UserValidationInterface()
            FrontEnd.UserValidationContinueInterface()
            command = int(InputReceive())

            match command:
                case 1:
                    return True
                case 2:
                    pass

            FrontEnd.UserValidationInterface()
            DBManager.DeleteFileData(InputReceive())

#Funções assíncronas

#CORROUTINES functions, reponsáveis para rodar animações com os validadores
async def JsonValidator_CORROUTINE():
    bodytext = 'Validando arquivo de configuração'
    Tittle = 'Iniciando Sistema'

    Front_End_jsonValidator_Task = asyncio.create_task(
        FrontEnd.LoadingAnimInterface(bodytext, Tittle))
    Json_Validator_Task = asyncio.create_task(jsonValidator())

    jsonIsValid = await Json_Validator_Task, Front_End_jsonValidator_Task
    
    return jsonIsValid
        
async def FileValidator_CORROUTINE():
    bodytext = 'Escaneando arquivos'
    Tittle = 'Iniciando Sistema'

    Front_End_FilesValidator_Task = asyncio.create_task(
        FrontEnd.LoadingAnimInterface(bodytext, Tittle))
    Files_Validator_Task = asyncio.create_task(FileValidator())

    filesIsValid = await Files_Validator_Task, Front_End_FilesValidator_Task

    return filesIsValid

async def MoveFiles_CORROUTINE():
    
    bodytext = 'Movendo arquivos'
    Tittle = 'Iniciando Sistema'

    FrontEnd_Movefiles_Task = asyncio.create_task(
        FrontEnd.LoadingAnimInterface(bodytext, Tittle))
    Move_Files_Task = asyncio.create_task(MoveFiles())

    isSuccess = await Move_Files_Task, FrontEnd_Movefiles_Task

#Função assíncrona para validar arquivo json
async def jsonValidator():
    
    jsonArchiveDict = DBManager.loadTempData()
    await asyncio.sleep(2)
    for x in jsonArchiveDict.keys():
            for y in jsonArchiveDict[x].keys():
                if jsonArchiveDict[x][y] == None or jsonArchiveDict[x][y] == '':
                    return False
    return True

#função assíncrona para validar arquivos no sistema
async def FileValidator():

    await asyncio.sleep(2)
    JsonArchiveDict = DBManager.loadTempData()

    for x in JsonArchiveDict.keys():
        fileCount = 1
        folderPath = JsonArchiveDict[x]["local"]
        fileType = JsonArchiveDict[x]["type"]
        if folderPath == DESKTOP_VAR:
            stringFileList = Shell(f"{SEARCH_FILES}'*{fileType}'", DESKTOP_PATH)
        elif folderPath == DOCUMENTS_VAR:
            stringFileList = Shell(f"{SEARCH_FILES}'*{fileType}'", DOCUMENTS_PATH)
        elif folderPath == VIDEOS_VAR:
            stringFileList = Shell(f"{SEARCH_FILES}'*{fileType}'", VIDEOS_PATH)
        elif folderPath == IMAGE_VAR:
            stringFileList = Shell(f"{SEARCH_FILES}'*{fileType}'", IMAGE_PATH)
        else:
            stringFileList = Shell(f"{SEARCH_FILES}'*{fileType}'", str(HOME_PATH+'/'+folderPath))
            
        if stringFileList == None or stringFileList == '':
            FrontEnd.JsonINVInterface(folderPath)
            return False

        for File in stringFileList:
            JsonArchiveDict[x][f"File{fileCount}"] = File
            fileCount+=1

    DBManager.writeFileListData(JsonArchiveDict)
    FrontEnd
    return True
            
async def MoveFiles():

    await asyncio.sleep(2)

    jsonArchiveDict = DBManager.loadFileListData()

    for x in jsonArchiveDict.keys():
        fileCount = 1
        count = 0
        finalFolderPath = jsonArchiveDict[x]["finalLocal"]
        localBasePath = jsonArchiveDict[x]["local"]

        if finalFolderPath != DESKTOP_VAR and finalFolderPath != DOCUMENTS_VAR and finalFolderPath != VIDEOS_VAR and finalFolderPath != IMAGE_VAR:
            Shell(f"{MAKE_DIRECTORY}{finalFolderPath}", HOME_PATH)

        for y in jsonArchiveDict[x].keys():

            if count < 3 : 
                count+=1
                continue

            if finalFolderPath == DESKTOP_VAR:
                Shell(f"{MOVE_FILES}{jsonArchiveDict[x][y]} {DESKTOP_PATH}", f"{HOME_PATH}/{localBasePath}")
            elif finalFolderPath == DOCUMENTS_VAR:
                Shell(f"{MOVE_FILES}{jsonArchiveDict[x][y]} {DOCUMENTS_PATH}", f"{HOME_PATH}/{localBasePath}")
            elif finalFolderPath == VIDEOS_VAR:
                Shell(f"{MOVE_FILES}{jsonArchiveDict[x][y]} {VIDEOS_PATH}", f"{HOME_PATH}/{localBasePath}")
            elif finalFolderPath == IMAGE_VAR:
                Shell(f"{MOVE_FILES}{jsonArchiveDict[x][y]} {IMAGE_PATH}", f"{HOME_PATH}/{localBasePath}")
            else:
                Shell(f"{MOVE_FILES}{jsonArchiveDict[x][y]} {HOME_PATH}/{finalFolderPath}", f"{HOME_PATH}/{localBasePath}")

#Funções de mudança de opções

def ShowOptionsCommand(Command):
    match Command:
        case 1: OptionChosenScreen(1)
        case 2 : pass


#Função de mudança de pasta base
def CBFolderCommand(index):
    jsonArchiveDict = DBManager.loadTempData()
    FrontEnd.CBFolderInput(jsonArchiveDict["Preload"+str(index)]["local"])
    input = InputReceive()
    DBManager.editPreloadData(jsonArchiveDict,"Preload"+str(index), "local", input)
    screenCode, command = InputCommands(FrontEnd.CBFolderRepeat)
    ChangeScreenProcess(screenCode, command)

def CBRepeatCommand(index):
    match index:
        case 1: OptionChosenScreen(3)
        case 2: pass
        
#Função de mudança de pasta final
def CFFolderCommand(index):
    jsonArchiveDict = DBManager.loadTempData()
    FrontEnd.CFFolderInput(jsonArchiveDict["Preload"+str(index)]["finalLocal"])
    input = InputReceive()
    DBManager.editPreloadData(jsonArchiveDict,"Preload"+str(index), "finalLocal", input)
    screenCode, command = InputCommands(FrontEnd.CFFolderRepeat)
    ChangeScreenProcess(screenCode, command)

def CFRepeatCommand(index):
    match index:
        case 1: OptionChosenScreen(2)
        case 2: pass  

#Função de mudança de tipo de arquivo
def CTypeCommand(index):
    jsonArchiveDict = DBManager.loadTempData()
    FrontEnd.CTypeInput(jsonArchiveDict["Preload"+str(index)]["type"])
    input = InputReceive()
    DBManager.editPreloadData(jsonArchiveDict,"Preload"+str(index), "type", input)
    screenCode, command = InputCommands(FrontEnd.CTypeRepeat)
    ChangeScreenProcess(screenCode, command)

def CTypeRepeatCommand(index):
    match index:
        case 1: OptionChosenScreen(4)
        case 2: pass  
    
#Funções de criação de preloads
def CreatPreloadCommand(index):
    jsondict = DBManager.createPreloadData()
    boolExit = True
    boolBF = False
    boolFF = False
    boolTP = False

    while boolExit:
        match index:
            case 1:
                FrontEnd.CPEditInterface()
                inputCommand = InputReceive()
                DBManager.editPreloadData(jsondict, "Preload" + str(len(jsondict)), "local", inputCommand)
                boolBF = True
            case 2: 
                FrontEnd.CPEditInterface()
                inputCommand = InputReceive()
                DBManager.editPreloadData(jsondict, "Preload" + str(len(jsondict)), "finalLocal", inputCommand)
                boolFF = True
            case 3: 
                FrontEnd.CPEditInterface()
                inputCommand = InputReceive()
                DBManager.editPreloadData(jsondict, "Preload" + str(len(jsondict)), "type", inputCommand)
                boolTP = True

        if(boolBF == True & boolFF == True & boolTP == True):
            FrontEnd.CPRepeatInterface()
            inputCommand = int(InputReceive())
            while inputCommand > 2 or inputCommand < 1:
                FrontEnd.ErrorInputInterface()
                inputCommand = int(InputReceive())
                FrontEnd.CPRepeatInterface()
            match inputCommand:
                case 1: pass
                case 2: 
                    boolExit = False
                    break
        
        FrontEnd.CPInputInterface()
        index = int(InputReceive())
        while index > 3 or index < 0:
                        FrontEnd.ErrorInputInterface()
                        index = int(InputReceive())
                        FrontEnd.CPInputInterface()

#Funções de exclusão de preloads temporários
def DeletePreloadCommand(index):

    DBManager.deletePreloadData(index)
    screenCode, Command = InputCommands(FrontEnd.DPRepeatInterface)
    ChangeScreenProcess(screenCode, Command)

def DPRepeatCommand(Command):

    match Command:
        case 1:
            screenCode, command = InputCommands(FrontEnd.DPRepeatInterface)
            ChangeScreenProcess(screenCode, command)
        case 2:
            pass

#Função de deleção dos preloads temporários (limpeza de arquivo)
def DTACommand(Command):

    match Command:
        case 1:
            DBManager.deleteTempData()
        case 2:
            pass    

#Função de salvamento de configuração no banco de dados
def SDBCommand(Command):

    match Command:
        case 1:
            DBManager.SavePreloadData()
        case 2:
            pass

#funções de carregamento de configuração no banco de dados
def LDBCommand(index):
    
    if index > 1:
        DBManager.LoadPreloadData(int(index-1))

def Shell(Command, dir):
    shellCommand = subprocess.Popen(Command, cwd=dir, shell=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    
    stdout = shellCommand.stdout.read().decode().split()
    return stdout