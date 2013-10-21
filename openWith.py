# -*- coding: cp936 -*-
import os
import sys
ExePathArr={"dsw":"'C:\Program Files (x86)\Microsoft Visual Studio\Common\MSDev98\Bin\MSDEV.EXE'"}
def DoOpen(cmdString):
    print(cmdString)
    os.popen(cmdString)


def SplitCmd(openStr):
    '''
        通过后缀名来分析通过哪个程序来打开
    '''
    strSplit = openStr.rsplit('.',1)
    print(strSplit)

    if(len(strSplit)<2):
        print("strExt <2")
        return ""
    cmdString=""
    strExt = strSplit[1]
    ExePath=""
    if strExt=="dsw":
        ExePath=ExePathArr[strExt]
    cmdString='"'+ExePath+" '"+openStr+"'"+'"'
    return cmdString


def main():
    if __name__!='__main__':
        return
    nLen = len(sys.argv)
    if nLen !=2:
        return
    print('arg'+sys.argv[1])
    cmdString = SplitCmd(sys.argv[1])

    DoOpen(cmdString)

main()

