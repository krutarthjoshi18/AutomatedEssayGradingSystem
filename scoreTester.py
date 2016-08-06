def getInput():
    fileName = raw_input("Enter file name")
    global essay
    print fileName
    print type(fileName)
    while 1:
        if (fileName[-4:] != '.txt'):
            print 'Invalid FileName'
            print 'Please Enter a valid FileName'
            break
        
        else:
            fileHandle = open ( fileName, 'r' )
            essay = fileHandle.read()
            fileHandle.close()
            break

    return essay

a = getInput()
