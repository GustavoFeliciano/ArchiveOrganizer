""""if char == '' or char == None or char == ' ':
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
                    JsonArchiveDict[x][f"File{fileCount}"] = fileNameTemp
                    fileCount += 1
                    sequenceChar = ''
                    sequenceCharCount = 0
                    fileNameTemp = ''
                    """

#Código de separação de string