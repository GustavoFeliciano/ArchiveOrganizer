import os
import time
import DBManager
import asyncio
from ConstantVariables import SLASH_CHAR, CLEAR_TERMINAL

os.system(CLEAR_TERMINAL)
print("--- Inicializando 'Organizador de Arquivos' aguarde um momento ---\n")
time.sleep(0) #Voltar time sleep para 3

def MainInterface():
    time.sleep(0)
    os.system(CLEAR_TERMINAL)
    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("     --- Menu Principal ---")
    print("1 -- Iniciar a organização --")
    print("2 -- Abrir configurações --")
    print("3 -- Mostrar configurações atuais --")
    print("4 -- Sair --")
    return str('MainInterface'),int(4)

#Interfaces de Opções
def OptionsInterface():
    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("1 -- Mostrar configurações atuais --")
    print("2 -- Mudar pasta alvo --")
    print("3 -- Mudar pasta base --")
    print("4 -- Mudar configuração de tipo de arquivo --")
    print("5 -- Criar configuração de arquivo --")
    print("6 -- Deletar configuração de arquivo --")
    print("7 -- Deletar todos os preloads de configuração atual --")
    print("8 -- Salvar configuração --")
    print("9 -- Carregar configuração --")
    print("10 -- Voltar ao menu principal")
    print("11 -- Sair --")
    return str('Options'), int(11)

#Interfaces assíncronas para a funcionalidade do sistema

#Interface animada de loading
async def LoadingAnimInterface(bodyText, Tittle):
    await asyncio.sleep(0.5)
    os.system(CLEAR_TERMINAL)
    charLoading = [
        f" {bodyText}",
        f" {bodyText}.",
        f" {bodyText}..",
        f" {bodyText}...",
        f" {bodyText}....",
        f" {bodyText}....."
        ]
    
    while True:
        print("---- ORGANIZADOR DE ARQUIVOS ----")
        print(f"  --- {Tittle}  ---\n")
        for x in charLoading:
            print(x,end="\r")
            await asyncio.sleep(0.2)
        os.system(CLEAR_TERMINAL)

#Interface de Erro do validador Json
def JsonINVInterface(Error):
    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("  -- Erro de configuração --")
    print(" O arquivo de configuração é inválido, possuindo campos nulos de configuração")
    print(" Por favor, complete os campos com a função de edição de Preloads e repita o processo")    

    time.sleep(4)

#Interface de Erro do validador de arquivos
def INVInterface(Error):
    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("  -- Erro de configuração --")
    print(f"{Error}")   

    time.sleep(4)

#Interface de sucesso do programa
def MoveFileSuccessInterface():
    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print(" -- Arquivos movidos com sucesso --")
    print("\n Para acessar os arquivos, vá até as pastas finais definidas.")
    print("Obrigado por escolher nosso Software\n\n")
    print("\n © MemoryQI Softwares - 2024")

    time.sleep(4)


#Interface de validação do usuário
def UserValidationInterface():

    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)
    count = 1

    jsonArchiveDict = DBManager.loadFileListData()

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("  --- Validação do usuário --- ")
    print(" Os documentos abaixo foram encontrados de acordo com suas configurações")
    print(" Caso haja algum documento que não faz parte do desejado, por favor")
    print(" Informe ao programa com seus devidos códigos\n")

    for x in jsonArchiveDict.keys():
        print(f"{x}:\n")
        print(f"  Pasta base: {jsonArchiveDict[x]["local"]}")
        print(f"  Pasta final: {jsonArchiveDict[x]["finalLocal"]}\n")
        print(f"  Arquivos encontrados nesse Preload:\n")
        for y in jsonArchiveDict[x].keys():
            
            if y != "local" and y != "finalLocal" and y != "type":
                print(f"   {y[3:]}-{y[:4]}: {jsonArchiveDict[x][y]}\n")

            

    print("Exemplo de entrada: '2,5' -> Preload 2 e o arquivo 5")
    print("Não serão aceitas mais de uma entrada por vez\n")

#Complemento da interface de validação
def UserValidationInputInterface():

    print("1 -- Se deseja continuar o programa")
    print("2 -- Se deseja voltar ao menu principal")
    print("3 -- Se deseja deletar um arquivo")

#Complemento de continuação da interface de validação
def UserValidationContinueInterface():

    print("1 -- Se deseja continuar o programa")
    print("2 -- Se deseja continua apagando arquivos")

#Função de interface de configurações atuais
def SOInterface():    
    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)

    jsonArchiveDict = DBManager.loadTempData()

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
    os.system(CLEAR_TERMINAL)

    jsonArchiveDict = DBManager.loadTempData()

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
    os.system(CLEAR_TERMINAL)

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Pasta base atual é *" + baseFolder + "* --")
    print("-- Digite o novo local da pasta para organização --\n")

def CBFolderRepeat():
    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)

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
    os.system(CLEAR_TERMINAL)

    jsonArchiveDict = DBManager.loadTempData()

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
    os.system(CLEAR_TERMINAL)

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Pasta final atual é *" + finalFolder + "* --")
    print("-- Digite o novo local da pasta para organização --\n")

def CFFolderRepeat():
    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)

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
    os.system(CLEAR_TERMINAL)

    jsonArchiveDict = DBManager.loadTempData()

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
    os.system(CLEAR_TERMINAL)

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Tipo de arquivo do preload é *" + Type + "* --")
    print("-- Digite o novo tipo de arquivo para organização --\n")
    print("-- Com a seguinte formatação, exemplo: '.py', '.DOCX' --")

def CTypeRepeat():
    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("-- Deseja fazer mais alterações? --")
    print("1 -- Sim")
    print("2 -- Não")

    return str("CTypeRepeat"), int(2)

#Interface de criação de preloads
def CreatePInterface():
    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)

    jsonArchiveDict = DBManager.loadTempData()

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
    os.system(CLEAR_TERMINAL)

    jsonArchiveDict = DBManager.loadTempData()

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("Defina pastas base e final apartir da sua pasta home")
    print("Caso, área de trabalho, Documentos, Vídeos ou Imagens, apenas digite esses nomes")
    print("Caso, outras pastas, faça o caminho a partir da sua pasta home do seu computador")
    print(f"""Exmplo '{SLASH_CHAR}PastaAlvo' localizado na pasta 'C:{SLASH_CHAR}
          User{SLASH_CHAR}PastaAlvo'\n""")

    print("-- Preload " + str(len(jsonArchiveDict)) + " --")
    print("1 -- Pasta base: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["local"])
    print("2 -- Pasta final: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["finalLocal"])
    print("3 -- Tipo de arquivo: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["type"])
    print("-- Digite o valor do campo selecionado --")

def CPInputInterface():
    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)

    jsonArchiveDict = DBManager.loadTempData()

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("Caso, área de trabalho, Documentos, Vídeos ou Imagens, apenas digite esses nomes")
    print("Caso, outras pastas, faça o caminho a partir da sua pasta home do seu computador")
    print(F"""Exmplo '{SLASH_CHAR}PastaAlvo' localizado na pasta 'C:{SLASH_CHAR}
          User{SLASH_CHAR}PastaAlvo'\n""")

    print("-- Preload " + str(len(jsonArchiveDict)) + " --")
    print("1 -- Pasta base: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["local"])
    print("2 -- Pasta final: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["finalLocal"])
    print("3 -- Tipo de arquivo: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["type"])
    print("-- Qual item deseja manipular? --")

def CPRepeatInterface():
    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)

    jsonArchiveDict = DBManager.loadTempData()

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("Caso, área de trabalho, Documentos, Vídeos ou Imagens, apenas digite esses nomes")
    print("Caso, outras pastas, faça o caminho a partir da sua pasta home do seu computador")
    print(F"""Exmplo '{SLASH_CHAR}PastaAlvo' localizado na pasta 'C:{SLASH_CHAR}
          User{SLASH_CHAR}PastaAlvo'\n""")

    print("-- Preload " + str(len(jsonArchiveDict)) + " --")
    print("1 -- Pasta base: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["local"])
    print("2 -- Pasta final: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["finalLocal"])
    print("3 -- Tipo de arquivo: "+ jsonArchiveDict["Preload"+ str(len(jsonArchiveDict))]["type"])
    print("-- Deseja continuar editando? --")
    print("1 -- Sim")
    print("2 -- Não")

def DPInterface():
    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)

    count = 0
    jsonArchiveDict = DBManager.loadTempData()

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print(" Selecione o Preload a ser excluído:\n")

    for x in jsonArchiveDict.keys():

        print("-- " + x + " --")
        print("-" + jsonArchiveDict[x]["local"] + "-")
        print("-" + jsonArchiveDict[x]["finalLocal"] + "-")
        print("-" + jsonArchiveDict[x]["type"] + "-\n")

        preloadRange = x[7:]
        
    return(str("DPInterface"), int(preloadRange))

def DPRepeatInterface():
    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print(" Deseja excluir mais um item?\n")
    print("1 - Sim")
    print("2 - Não")

    return(str("DPRepeat"),int(2))   

#Interfaes de limpeza do documento tempDB.json

def DTAInterface():
    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print(" Realmente deseja excluir toda a configuração atual?")
    print("         (Não será possível reverter)")
    print("1 - Sim")
    print("2 - Não")

    return(str("DTAInterface"),int(2))

#Interface de salvamento do documento tempDB.json no banco de dados

def SaveDBInterface():
    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print(" Realmente deseja salvar toda a configuração atual?")
    print("         (Não será possível reverter)")
    print("1 - Sim")
    print("2 - Não")

    return(str("SaveDBInterface"), int(2))

#Interfaces de carregamento de preload de configuração do banco de dados
def LPDBInterface():
    time.sleep(0.5)
    os.system(CLEAR_TERMINAL)

    count = 1
    jsonPreviewDict = DBManager.loadPreloadPreviewData()

    print("---- ORGANIZADOR DE ARQUIVOS ----")
    print("         --- OPÇÕES ---")
    print("  --Preview dos dados salvos--\n")

    for x in jsonPreviewDict.keys():
        print(str(int(x[9:])+1)+" - Preload Salvo:\n")

        for y in jsonPreviewDict[x].keys():
            print("    -- Preload"+ str(y[7:])+" --")
            print("      - Pasta base: "+ jsonPreviewDict[x][y]["local"]+" -")
            print("      - Pasta final: "+ jsonPreviewDict[x][y]["finalLocal"]+" -")
            print("      - Tipo de arquivo: "+ jsonPreviewDict[x][y]["type"]+" -\n")
        count += 1
        print("\n")

    print(" Digite 1 caso queira cancelar a operação")

    return str("LPDBInterface"), int(count)

#Interfaces de erro e outras
def ErrorInputInterface():
    time.sleep(1)
    os.system(CLEAR_TERMINAL)
    print("Comando inválido, por favor insira novamente")
    time.sleep(1)
    os.system(CLEAR_TERMINAL)


def ProcessInterface():
    os.system(CLEAR_TERMINAL)
    return str('Process'),int(4)