import FrontEnd
import platform
import FunctionsManager


#Funções pra gerar um frontEnd para o sistema, deve importar e criar uma classe com as funções
#necessárias pra produzir o front end no terminal

#Classe para a criação do DB temporário

#Desenvolver as funções necessárias para a manipulação dos arquivos, recebendo os inputs:
#Local desejados para remanejar os arquivos, sendo limitados a alguns paths (Para não quebrar o OS)
#Local para onde os arquivos devem ser organizados
#Tipo de organização: Por tipo de arquivos, ou pastas com nomes personalizados
#Funções de manipulação dos arquivos e finalização mostrando no frontend

class main:
    
    osUsable = platform.system()

    if osUsable == 'Linux':
        filesLocation = 'Desktop'
    elif osUsable == 'Windows':
        filesLocation = 'Desktop'
    elif osUsable == 'Mac':
        filesLocation = 'Desktop'
    else:
        print('Sistema não foi reconhecido, por favor,' +
            'digitar o caminho até o seu Desktop...')
        pathToDesktop = input('Usuario:')

    screenCode, command = FunctionsManager.InputCommands(FrontEnd.MainInterface)
    FunctionsManager.ChangeScreenProcess(screenCode, command)    
    