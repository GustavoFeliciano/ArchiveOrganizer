#Variáveis de comando para cada sistema operacional
import platform
import os
import time
import subprocess
import locale, ctypes

osUsable = platform.system()
USER_NAME = ''

shellCommand = subprocess.Popen("whoami", shell=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    
stdout = shellCommand.stdout.read() + shellCommand.stderr.read()
USER_NAME = stdout.decode()
USER_NAME = USER_NAME[:int(len(USER_NAME)-1)]

if osUsable == 'Linux':

    LANGUAGE_OS = os.getenv('LANG')

    THIS_DIRECTORY="pwd "
    CHANGE_DIRECTORY="cd "
    GO_TO_HOME=str("cd /home/"+ USER_NAME)
    LIST_ALL="ls "
    DELETE_DIRECTORY="rmdir "
    DELETE_FILES="rm "
    SEARCH_FILES="find -name "
    MOVE_FILES="mv "

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

elif osUsable == 'Windows':
    
    windll = ctypes.windll.kernel32
    LANGUAGE_OS = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

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

    filesLocation = 'Desktop'
    THIS_DIRECTORY="cd "
    CHANGE_DIRECTORY="cd "
    GO_TO_HOME="cd %homedrive%%homepath% "
    LIST_ALL="dir "
    DELETE_DIRECTORY="rmdir /s /q "
    DELETE_FILES="del "
    SEARCH_FILES="dir /b/s "

    #Paths padrões do sistema

    HOME_PATH="%homedrive%%homepath% "
    DESKTOP_PATH=str(HOME_PATH+'/'+DESKTOP_VAR)
    DOCUMENTS_PATH=str(HOME_PATH+'/'+DOCUMENTS_VAR)
    VIDEOS_PATH=str(HOME_PATH+'/'+VIDEOS_VAR)
    IMAGE_PATH=str(HOME_PATH+'/'+IMAGE_VAR)

    
elif osUsable == 'Mac':

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
