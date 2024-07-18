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
        case 'AOInterface':
            AOInit(Command)
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

            if jsonIsValid == True:
                fileIsValid =asyncio.run(FileValidator_CORROUTINE())

            fileIsValid =asyncio.run(FileValidator_CORROUTINE())

            #if fileIsValid == True:
            
            screenCode, command = InputCommands(FrontEnd.MainInterface)
            ChangeScreenProcess(screenCode, command)
            

            
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

async def JsonValidator_CORROUTINE():
    Front_End_jsonValidator_Task = asyncio.create_task(FrontEnd.JsonValidatorInterface())
    Json_Validator_Task = asyncio.create_task(DBManager.jsonValidator())

    jsonIsValid = await Json_Validator_Task, Front_End_jsonValidator_Task
    
    return jsonIsValid
        
async def FileValidator_CORROUTINE():
    #Vai dar comandos ao sistema, procurando arquivos de cada tipo nas pastas indicadas
    #Sistema vai guardar o nome dos arquivos e seus lugares num arquivo json temporário (Dumps)
    #Se houver alguma pesquisa sem arquivos, informar os dados de configuração
    # que não conseguiu encontrar arquivos
    #Após disso, rodar próxima etapa

    Front_End_filesValidator_Task = asyncio.create_task(FrontEnd.FileValidatorInterface())
    Files_Validator_Task = asyncio.create_task(FileValidator())

    filesIsValid = await Files_Validator_Task, Front_End_filesValidator_Task

    return filesIsValid

    

async def FileValidator():

    JsonArchiveDict = DBManager.loadTempData()
    fileList = []
    fileNameTemp = ''
    sequenceCharCount = 0
    sequenceChar = ''
    for x in JsonArchiveDict.keys():
        folderPath = JsonArchiveDict[x]["local"]
        fileType = JsonArchiveDict[x]["type"]
        match folderPath:
            case str(DESKTOP_VAR):
                str(SEARCH_FILES+"'*"+fileType+"'")
                stringFileList = Shell(f"{SEARCH_FILES}'*{fileType}'", "/home/gwdcks/GitProjects/ArchiveOrganizer/Json")
            case str(DOCUMENTS_VAR):
                Shell(f"{SEARCH_FILES}'*{fileType}'", DOCUMENTS_PATH)
            case str(VIDEOS_VAR):
                Shell(f"{SEARCH_FILES}'*{fileType}'", VIDEOS_PATH)
            case str(IMAGE_VAR):
                Shell(f"{SEARCH_FILES}'*{fileType}'", IMAGE_PATH)
                
            #atrela essa lista ao arquivo json 'De alguma forma', pra mostrar se tem
            #algum arquivo que o usuário não queira mexer e poder tirar da lista final
        if stringFileList == None or stringFileList == '':
            FrontEnd.JsonINVInterface(folderPath)
            return False

        for char in stringFileList:

            if char == '' or None:
                continue
            
            fileNameTemp += char
            if char != fileType[sequenceCharCount:int(sequenceCharCount+1)]:
                sequenceChar = ''
                sequenceCharCount = 0
                continue
            
            sequenceChar += char
            sequenceCharCount += 1
            if sequenceChar == fileType:
                if sequenceChar == fileType:
                    fileList.append(fileNameTemp)
                    sequenceChar = ''
                    sequenceCharCount = 0
                    fileNameTemp = ''
                
    #Implementação da lista de arquivos em algum lugar
            

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
    
    stdout = shellCommand.stdout.read().decode()
    return stdout