import os
import platform
import time
import dbManager

os.system('clear')
print("--- Inicializando 'Organizador de Arquivos' aguarde um momento ---\n")
time.sleep(3)

def MainInterface():
    time.sleep(1)
    os.system('clear')
    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("     --- Menu Principal ---")
    print("1 -- Iniciar a organização --")
    print("2 -- Abrir configurações --")
    print("3 -- Mostrar configurações atuais --")
    print("4 -- Sair --")
    return str('Main'),int(4)





#Interfaces de Opções
def OptionsInterface():
    time.sleep(0.5)
    os.system('clear')

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("1 -- Mostrar configurações atuais --")
    print("2 -- Mudar pasta alvo --")
    print("3 -- Mudar pasta base --")
    print("4 -- Mudar configuração de tipo de arquivo --")
    print("5 -- Criar configuração de arquivo --")
    print("6 -- Deletar configuração de arquivo --")
    print("7 -- Salvar configuração atual --")
    print("8 -- Carregar configuração --")
    print("9 -- Voltar ao Menu principal --")
    print("10 -- Sair --")
    return str('Options'), int(10)

#Função de interface de configurações atuais
def SOInterface():    
    time.sleep(0.5)
    os.system('clear')

    jsonArchiveDict = dbManager.loadTempData()

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---\n")
    for x in jsonArchiveDict.keys():
        print("\n--" + x + ":\n")
        print(" -- Pasta Base: " + jsonArchiveDict[x]["local"])
        print(" -- Pasta Final: " + jsonArchiveDict[x]["finalLocal"])
        print(" -- Tipo de arquivo: " + jsonArchiveDict[x]["type"])

    print("\n1 -- Repetir")
    print("2 -- Voltar ao menu anterior")
    return str("SOInterface"), int(2)


#Funções de interface para mudar pastas

#função de interface de troca de basta base
def CBFolderInterface():
    count = 0
    time.sleep(0.5)
    os.system('clear')

    jsonArchiveDict = dbManager.loadTempData()

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Escolha uma opção pra fazer a mudança --\n")
    for x in jsonArchiveDict.keys():
        print("--" + x + "--" )
        print("-" + jsonArchiveDict[x]["local"] +"-")
        print("-" + jsonArchiveDict[x]["type"] +"-\n")
        count += 1

    return str('CBFolder'), int(count)

def CBFolderInput(baseFolder):
    time.sleep(0.5)
    os.system('clear')

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Pasta base atual é *" + baseFolder + "* --")
    print("-- Digite o novo local da pasta para organização --\n")

def CBFolderRepeat():
    time.sleep(0.5)
    os.system('clear')

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Deseja fazer mais alterações? --")
    print("1 -- Sim")
    print("2 -- Não")

    return str("CBRepeat"), int(2)

#função de interface de troca de arquivo final

def CFFolderInterface():
    count = 0
    time.sleep(0.5)
    os.system('clear')

    jsonArchiveDict = dbManager.loadTempData()

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Escolha uma opção pra fazer a mudança --\n")
    for x in jsonArchiveDict.keys():
        print("--" + x + "--" )
        print("-" + jsonArchiveDict[x]["finalLocal"] +"-")
        print("-" + jsonArchiveDict[x]["type"] +"-\n")
        count += 1

    return str('CFFolder'), int(count)

def CFFolderInput(finalFolder):
    time.sleep(0.5)
    os.system('clear')

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Pasta final atual é *" + finalFolder + "* --")
    print("-- Digite o novo local da pasta para organização --\n")

def CFFolderRepeat():
    time.sleep(0.5)
    os.system('clear')

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Deseja fazer mais alterações? --")
    print("1 -- Sim")
    print("2 -- Não")

    return str("CFRepeat"), int(2)

#Função de troca de tipo de arquivo

def CTypeInterface():
    count = 0
    time.sleep(0.5)
    os.system('clear')

    jsonArchiveDict = dbManager.loadTempData()

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Escolha uma opção pra fazer a mudança --\n")
    for x in jsonArchiveDict.keys():
        print("--" + x + "--" )
        print("-" + jsonArchiveDict[x]["type"] +"-\n")
        count += 1

    return str('CTypeInterface'), int(count)

def CTypeInput(Type):
    time.sleep(0.5)
    os.system('clear')

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Tipo de arquivo do preload é *" + Type + "* --")
    print("-- Digite o novo tipo de arquivo para organização --\n")
    print("-- Com a seguinte formatação, exemplo: '.py', '.DOCX' --")

def CTypeRepeat():
    time.sleep(0.5)
    os.system('clear')

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Deseja fazer mais alterações? --")
    print("1 -- Sim")
    print("2 -- Não")

    return str("CTypeRepeat"), int(2)

#Interface de criação de preloads
def CreatePInterface():
    time.sleep(0.5)
    os.system('clear')

    jsonArchiveDict = dbManager.loadTempData()

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Preload " + str(len(jsonArchiveDict) + 1) + " --")
    print("1 -- Pasta base: ")
    print("2 -- Pasta final: ")
    print("3 -- Tipo de arquivo: ")
    print("-- Qual item deseja manipular? --")

    return str("CPInterface"), int(3)

def CPEditInterface():
    time.sleep(0.5)
    os.system('clear')

    jsonArchiveDict = dbManager.loadTempData()

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Preload " + str(len(jsonArchiveDict)) + " --")
    print("1 -- Pasta base: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["local"])
    print("2 -- Pasta final: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["finalLocal"])
    print("3 -- Tipo de arquivo: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["type"])
    print("-- Digite o valor do campo selecionado --")

def CPInputInterface():
    time.sleep(0.5)
    os.system('clear')

    jsonArchiveDict = dbManager.loadTempData()

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Preload " + str(len(jsonArchiveDict)) + " --")
    print("1 -- Pasta base: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["local"])
    print("2 -- Pasta final: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["finalLocal"])
    print("3 -- Tipo de arquivo: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["type"])
    print("-- Qual item deseja manipular? --")

def CPRepeatInterface():
    time.sleep(0.5)
    os.system('clear')

    jsonArchiveDict = dbManager.loadTempData()

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Preload " + str(len(jsonArchiveDict)) + " --")
    print("1 -- Pasta base: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["local"])
    print("2 -- Pasta final: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["finalLocal"])
    print("3 -- Tipo de arquivo: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["type"])
    print("-- Deseja continuar editando? --")
    print("1 -- Sim")
    print("2 -- Não")

def DPInterface():
    time.sleep(0.5)
    os.system('clear')

    count = 0
    jsonArchiveDict = dbManager.loadTempData()

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print(" Selecione o Preload a ser excluído:\n")

    for x in jsonArchiveDict.keys():

        count+=1

        print("-- " + x + " --")
        print("-" + jsonArchiveDict[x]["local"] + "-")
        print("-" + jsonArchiveDict[x]["finalLocal"] + "-")
        print("-" + jsonArchiveDict[x]["type"] + "-\n")
    
    return(str("DPInterface"),int(count))

def DPRepeatInterface():
    time.sleep(0.5)
    os.system('clear')

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print(" Deseja excluir mais um item?\n")
    print("1 - Sim")
    print("2 - Não")

    return(str("DPRepeat"),int(2))   

#Interfaes de limpeza do documento tempDB.json

def DTAInterface():
    time.sleep(0.5)
    os.system('clear')

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print(" Realmente deseja excluir toda a configuração atual?")
    print("         (Não será possível reverter)")
    print("1 - Sim")
    print("2 - Não")

    return(str("DTAInterface"),int(2))

#Interfaces de erro e outras
def ErrorInputInterface():
    time.sleep(1)
    os.system('clear')
    print("Comando inválido, por favor insira novamente")
    time.sleep(1)
    os.system('clear')


def ProcessInterface():
    os.system('clear')
    return str('Process'),int(4)