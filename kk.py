# -*- coding: cp936 -*-
import os,sys
def getdat(line):
        ''' 返回字符串中的整数

        返回字符串中的整数'''
        result =0
        flag = 0
        for i in range(0,len(line)):
                if line[i].isdigit():
                        result = result*10+int(line[i])
##                elif line[i].isspace():
##                        if flag==1:
##                                print(result)
##                        else:
##                                print(-result)
##                        print(i)
##                        result=0
        return result

def CommitRc2Svn(rcPath,curVersion):
        print(rcPath)
        print(curVersion)
        svnCMD = 'svn ci -m "Update version[{0}]"  '+rcPath
        svnCMD=str.format(svnCMD,curVersion)
        print(svnCMD)
        svnRet =  os.popen(svnCMD).readlines()
        print(svnRet)
        
        if len(svnRet) != 3:
                print("len <3")
                return False
        ver = svnRet[2].split(' ')
        print(len(ver))
        print(ver)
        nVer = getdat(ver[2])
        print("ver ={0}",nVer)
        return True
dd = str.format("1+2={0}",1+2)
print(dd)
CommitRc2Svn(os.getcwd()+'\\'+sys.argv[1],99)
