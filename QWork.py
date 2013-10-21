import os
import glob
import svnVer2rc
allresult=list()
def GetDirPath(filePath):
    pos = filePath.rfind('\\')
    if pos<0:return filePath
    return filePath[:pos]
def FindRcFiles(path):
    global allresult
    p =  '*.rc'
    for root, dirs, files in os.walk(path):
        result = glob.glob(os.path.join(root, p))
        for f in result:
            #print f
            allresult.append(f)
            svnVer2rc.getVersion(GetDirPath(f))
path ="E:\\workspace\\MSV\\msv1010_s2(4211p)_Debug版本"
#path =@'E:\\workspace\\MSV\\Ingest_3.1.1\\'
FindRcFiles(path)
allresult
