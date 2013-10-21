import io

import os
import glob
fileExtList=['.obj','.pch','.idb','.ilk','.res']

dirPath='E:\workspace'

def CallBack_Fuc(filePath):
    print(filePath)
    os.remove(filePath)
    
def AnalyeFile(filePath):
    fileExt = os.path.splitext(filePath)[1]
    if fileExt in fileExtList:
        CallBack_Fuc(filePath)
def test():
    for root,dirs,files in os.walk(dirPath):
        for name in files:
             AnalyeFile(os.path.join(root,name))
 #        for name in dirs:
            #print("dir:-->"+os.path.join(root,name))
  #          print("dir:-->"+name)
test()
