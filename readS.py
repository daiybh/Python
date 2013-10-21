
import os
import tempfile
def getVersionFromFile(tempFilePath):
    print(tempFilePath)
    tempFile = open(tempFilePath)
    line = tempFile.readline()
    tempFile.close()
    if not line:
        return "-1"
    line = line.strip()
    print("-----------")
    print(line)
    print("-----------")
    return line

tempFile="%s\\tempXXX.h"%tempfile.gettempdir()
print getVersionFromFile(tempFile)

