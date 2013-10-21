# -*- coding: cp936 -*-
import os,win32api

filePath= r"E:\workspace\MSV\msv1010_s2(4211p)_Debug版本\收录中层\binU"
fileName = r"MSVMainAppU.exe"

def get_version_number(fileName):
    if os.path.exists(fileName):
        info = win32api.GetFileVersionInfo(fileName,"\\")
        ms = info["FileVersionMS"]
        ls = info["FileVersionLS"]
        return win32api.HIWORD(ms),win32api.LOWORD(ms),win32api.HIWORD(ls),win32api.LOWORD(ls),


def PrintVer(fileName):
    #print fileName
    name =  fileName[fileName.rindex("\\")+1:]
    pos = fileName.find(filePath)
    folder = fileName[pos+len(filePath)+1:]
    #print folder
    pos = folder.rfind("\\")
    if pos >0:
        folder = folder[:pos]
    else:
        folder =""
    ver = ".".join([str(i) for i in get_version_number(fileName)])
    print("%20s  %25s          %s"%(folder,name,ver))

p=[ '.exe','.dll','.plug']
def fileFilter(fileExt):
    return fileExt in p

def GetExeFile(filePath):
    if not os.path.exists(filePath):
        print "no",filePath
        return False
    list = os.listdir(filePath)
    for line in list:
        fileName = os.path.join(filePath,line)
        if os.path.isfile(fileName) :
            ext = os.path.splitext(fileName)
            #print fileName
            if fileFilter(ext[1]):
                PrintVer(fileName)
        else:
            #print("递归 %s"%fileName)
            GetExeFile(fileName)
    

GetExeFile(filePath)
file = filePath +"\\"+ fileName
#PrintVer(file)
    
