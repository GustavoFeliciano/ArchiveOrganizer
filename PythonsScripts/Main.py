import FrontEnd
import platform
import FunctionsManager

class main:

    screenCode, command = FunctionsManager.InputCommands(FrontEnd.MainInterface)
    FunctionsManager.ChangeScreenProcess(screenCode, command)    
    