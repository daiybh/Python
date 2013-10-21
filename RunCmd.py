import os
import sys

def _RunCmd(cmd):
    ret =os.popen(cmd).readlines()
    return ret

def GetContent(content,feature):
    for line in content:
        if line.lower().find(feature)>=0:
            print(line)

def RunCmd(cmd,feature):
    ret = _RunCmd(cmd)
    #print(ret)
    GetContent(ret,feature.lower())

def main():
     ##if __name__ != '__main__':
     ##    return
    argLen=len(sys.argv)
    feature=""
    startArg=1
    if argLen <2 :
         print("argv<2")
         return
    if argLen==2:
         print("argv==2")
         feature="Error"
    elif argLen>2:
         print("argv>2")
         feature=sys.argv[1]
         startArg=2
    print("feature="+feature)
    for i in range(startArg,argLen):
         print(sys.argv[i])
         RunCmd(sys.argv[i],feature)

main()
