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
    print("5 -- Salvar configuração atual --")
    print("6 -- Carregar configuração --")
    print("7 -- Voltar ao Menu principal --")
    print("8 -- Sair --")
    return str('Options'), int(8)

#Função de interface de configurações atuais
def SOInterface():    
    time.sleep(0.5)
    os.system('clear')

    jsonArchiveDict = dbManager.LoadTempData()

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

    jsonArchiveDict = dbManager.LoadTempData()

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

    jsonArchiveDict = dbManager.LoadTempData()

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

    jsonArchiveDict = dbManager.LoadTempData()

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


