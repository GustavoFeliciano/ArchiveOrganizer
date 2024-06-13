#imports
import os
import FrontEnd
import dbManager
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
        case 'Main':
            MainChosenScreen(Command)

        #Options functions case
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
        case 'DTAInterface':
            DTACommand(Command)

#Inputs da função Main                
def MainChosenScreen(Command):
    match Command:
        case 1: 
            print("")
        case 2:
            screenCode, command = InputCommands(FrontEnd.OptionsInterface)
            ChangeScreenProcess(screenCode, command)
            #Mudandança de tela - receber o input - próxima função de options
        case 3:
            print('Actual Option')
            #Buscar as configurações setadas
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
            ExitSoftware()
            screenCode, command = InputCommands(FrontEnd.DTAInterface)
            ChangeScreenProcess(screenCode, command)
            screenCode, command = InputCommands(FrontEnd.OptionsInterface)
            ChangeScreenProcess(screenCode, command)

        case 8:
            ExitSoftware()
        case 9:
            ExitSoftware()
        case 10:
            ExitSoftware()    

#Funções de mudança de opções

def ShowOptionsCommand(Command):
    match Command:
        case 1: OptionChosenScreen(1)
        case 2 : pass


#Função de mudança de pasta base
def CBFolderCommand(index):
    jsonArchiveDict = dbManager.loadTempData()
    FrontEnd.CBFolderInput(jsonArchiveDict["Preload"+str(index)]["local"])
    input = InputReceive()
    dbManager.editPreloadData(jsonArchiveDict,"Preload"+str(index), "local", input)
    screenCode, command = InputCommands(FrontEnd.CBFolderRepeat)
    ChangeScreenProcess(screenCode, command)

def CBRepeatCommand(index):
    match index:
        case 1: OptionChosenScreen(3)
        case 2: pass
        
#Função de mudança de pasta final
def CFFolderCommand(index):
    jsonArchiveDict = dbManager.loadTempData()
    FrontEnd.CFFolderInput(jsonArchiveDict["Preload"+str(index)]["finalLocal"])
    input = InputReceive()
    dbManager.editPreloadData(jsonArchiveDict,"Preload"+str(index), "finalLocal", input)
    screenCode, command = InputCommands(FrontEnd.CFFolderRepeat)
    ChangeScreenProcess(screenCode, command)

def CFRepeatCommand(index):
    match index:
        case 1: OptionChosenScreen(2)
        case 2: pass  

#Função de mudança de tipo de arquivo
def CTypeCommand(index):
    jsonArchiveDict = dbManager.loadTempData()
    FrontEnd.CTypeInput(jsonArchiveDict["Preload"+str(index)]["type"])
    input = InputReceive()
    dbManager.editPreloadData(jsonArchiveDict,"Preload"+str(index), "type", input)
    screenCode, command = InputCommands(FrontEnd.CTypeRepeat)
    ChangeScreenProcess(screenCode, command)

def CTypeRepeatCommand(index):
    match index:
        case 1: OptionChosenScreen(4)
        case 2: pass  
    
#Funções de criação de preloads
def CreatPreloadCommand(index):
    jsondict = dbManager.createPreloadData()
    boolExit = True
    boolBF = False
    boolFF = False
    boolTP = False

    while boolExit:
        match index:
            case 1:
                FrontEnd.CPEditInterface()
                inputCommand = InputReceive()
                dbManager.editPreloadData(jsondict, "Preload" + str(len(jsondict)), "local", inputCommand)
                boolBF = True
            case 2: 
                FrontEnd.CPEditInterface()
                inputCommand = InputReceive()
                dbManager.editPreloadData(jsondict, "Preload" + str(len(jsondict)), "finalLocal", inputCommand)
                boolFF = True
            case 3: 
                FrontEnd.CPEditInterface()
                inputCommand = InputReceive()
                dbManager.editPreloadData(jsondict, "Preload" + str(len(jsondict)), "type", inputCommand)
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
        print(index)
        while index > 3 or index < 0:
                        FrontEnd.ErrorInputInterface()
                        index = int(InputReceive())
                        FrontEnd.CPInputInterface()

def DeletePreloadCommand(index):

    dbManager.deletePreloadData(index)
    screenCode, Command = InputCommands(FrontEnd.DPRepeatInterface)
    ChangeScreenProcess(screenCode, Command)

def DPRepeatCommand(Command):

    match Command:
        case 1:
            screenCode, command = InputCommands(FrontEnd.DPRepeatInterface)
            ChangeScreenProcess(screenCode, command)
        case 2:
            pass

def DTACommand(Command):

    match Command:
        case 1:
            dbManager.deleteTempData()
        case 2:
            pass    