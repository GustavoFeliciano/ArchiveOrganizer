#Variáveis de comando para cada sistema operacional
import platform
import os
import time
import subprocess
import locale, ctypes

OS_PLATFORM = platform.system()
USER_NAME = ''

shellCommand = subprocess.Popen("whoami", shell=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    
stdout = shellCommand.stdout.read() + shellCommand.stderr.read()
USER_NAME = stdout.decode()
USER_NAME = USER_NAME[:int(len(USER_NAME)-1)]

if OS_PLATFORM == 'Linux':

    LANGUAGE_OS = os.getenv('LANG')

    CLEAR_TERMINAL="clear"
    MAKE_DIRECTORY="mkdir "
    SEARCH_FILES="find "
    MOVE_FILES="mv "
    SLASH_CHAR="/"

    #Variáveis de linguagem

    match LANGUAGE_OS[:5]:

        case "pt_BR":
            DESKTOP_VAR = "Área de trabalho"
            DOCUMENTS_VAR = "Documentos"
            VIDEOS_VAR = "Vídeos"
            IMAGE_VAR = "Imagens"

        case "en_EN":
            DESKTOP_VAR = "Desktop"
            DOCUMENTS_VAR = "Documents"
            VIDEOS_VAR = "Videos"
            IMAGE_VAR = "Images"

    #Paths padrões do sistema

    HOME_PATH=str("/home/"+ USER_NAME)
    DESKTOP_PATH=str(HOME_PATH+'/'+DESKTOP_VAR)
    DOCUMENTS_PATH=str(HOME_PATH+'/'+DOCUMENTS_VAR)
    VIDEOS_PATH=str(HOME_PATH+'/'+VIDEOS_VAR)
    IMAGE_PATH=str(HOME_PATH+'/'+IMAGE_VAR)

elif OS_PLATFORM == 'Windows':
    
    windll = ctypes.windll.kernel32
    LANGUAGE_OS = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

    shellCommand = subprocess.Popen(r"echo %homedrive%%homepath%", shell=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    
    HOME_PATH = shellCommand.stdout.read().decode()
    

    match LANGUAGE_OS:
        
        case "pt_BR":
            DESKTOP_VAR = "Área de trabalho"
            DOCUMENTS_VAR = "Documentos"
            VIDEOS_VAR = "Vídeos"
            IMAGE_VAR = "Imagens"

        case "en_EN":
            DESKTOP_VAR = "Desktop"
            DOCUMENTS_VAR = "Documents"
            VIDEOS_VAR = "Videos"
            IMAGE_VAR = "Images"

    CLEAR_TERMINAL="cls"
    MAKE_DIRECTORY="mkdir "
    SEARCH_FILES="dir /b/s "
    SLASH_CHAR="\\"
    MOVE_FILES="move "
    #comando de mover arquivos no win
    #Paths padrões do sistema
    
    DESKTOP_PATH=str(HOME_PATH+'\\'+DESKTOP_VAR)
    DOCUMENTS_PATH=str(HOME_PATH+'\\'+DOCUMENTS_VAR)
    VIDEOS_PATH=str(HOME_PATH+'\\'+VIDEOS_VAR)
    IMAGE_PATH=str(HOME_PATH+'\\'+IMAGE_VAR)

    
elif OS_PLATFORM == 'Mac':

    LANGUAGE_OS = os.getenv('LANG')
    
    THIS_DIRECTORY="pwd "
    CHANGE_DIRECTORY="cd "
    LIST_ALL="ls "
    DELETE_DIRECTORY="rm "

    #Paths padrões do sistema

else:
    print('Sistema não foi reconhecido, por favor,' +
        'digitar o caminho até o seu Desktop...')
    pathToDesktop = input('Usuario:')

