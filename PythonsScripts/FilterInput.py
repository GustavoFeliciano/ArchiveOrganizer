import DBManager
import time

def IntFilter(range, Msg):

    while True:
        try:
            index = int(input(f"{Msg}"))
            if index > 0 and index < int(range+1): return index
            return 0
        except Exception as e:
            return 0
        
def StrFilter(Msg):
    
    while True:
        try:
            index = str(input(f"{Msg}"))
            return index
        except Exception as e:
            return False


def PreFileDelFilter(range, Msg):

    jsonArchiveList = DBManager.loadFileListData()

    fileVar = '' 
    preloadVar = ''
    commaCheck = False

    try:
        index = str(input(f"{Msg}"))

        charCount = 0
        for char in index:
            if char == ",":
                preloadVar = tempCommand
                if preloadVar > str(range) or preloadVar < "1": return False
                charCount+=1
                tempCommand = ''
                commaCheck = True
                break
            
            tempCommand = char
            charCount+=1
        if commaCheck == False: return False

        try:
            range = int(len(jsonArchiveList[str('Preload'+preloadVar)].keys()) - 3)
            print(index[charCount:])
            time.sleep(5)
            fileVar = index[charCount:]
            print(fileVar)
            time.sleep(5)
            fileVarstr = str("File"+fileVar)
            print(fileVarstr)
            time.sleep(5)
        except Exception as e:
            print("Opa")
            time.sleep(5)
            return False

        if fileVarstr in jsonArchiveList[str("Preload"+preloadVar)]: return str(fileVar), str(preloadVar)
        return False
        
    except Exception as e:
        return False