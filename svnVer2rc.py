# -*- coding: cp936 -*-
'''读取svn 版本号
'''
import os
import stat
import string
import sys
import glob
import distutils.file_util
import tempfile
from   xml.dom import minidom
verFilter = ['FILEVERSION','FileVersion','PRODUCTVERSION','ProductVersion']
#verFormatStr=['  FILEVERSION       %d,%d,%d,%d\n','                    VALUE "FileVersion",     "%d.%d.%d (r%d)\\0"\n',
#              '  PRODUCTVERSION    %d,%d,%d,%d\n','                    VALUE "ProductVersion",  "%d.%d.%d (r%d)\\0"\n']
verFormatStr=['  FILEVERSION       {0},{1},{2},{3}\n','            VALUE "FileVersion",     "{0}.{1}.{2}\\0"\n',
          '  PRODUCTVERSION    {0},{1},{2},{3}\n','            VALUE "ProductVersion",  "{0}.{1}.{2} (r{3})\\0"\n']
#major_Version=3
#minor_Version=1
#path_Version=2
verCompanyName="索贝数码科技股份有限公司"
strComments=""
verVC     ="vc9"
class CGetSvnVerion:
    def __init__(self):
        self.sNu=-1
    def getVersion(self,wcPath):
        sNu=self.getSVNVersion(wcPath)
        if sNu<0:
            #尝试乌龟svn取版本
            sNu = self.getTorSvnVersion(wcPath)
        return sNu
    def getTorSvnVersion(self,wcPath):
        
        svnversionCmd='subwcrev "%s"'%wcPath
        tempFile="%s\\tempXXX.h"%tempfile.gettempdir()
        #tempFile="d:\\tempXXX.h"
        svnversionCmd='subwcrev "%s" "%s\\tVer_temp.h" %s'%(wcPath,sys.path[0],tempFile)
        print(svnversionCmd)
        print("-------------")
        #return -1
        svnVersion =  os.popen(svnversionCmd).readlines()
        #print(svnVersion)
        snu = self.getVersionFromFile(tempFile)
        #print(svnversionCmd)
        return snu
        # 查找 'Updated to revision
        strMark = 'Updated to revision'
        sNu = -1
        for  s in strRet:
            if strMark in s:
                #print(s)
                dv = s.split(' ')
                #print(dv)
                sNu = self.getdat(dv[3])
        return sNu


    def getVersionFromFile(self,tempFilePath):
        tempFile = open(tempFilePath)
        line = tempFile.readline()
        tempFile.close()

        if not line:
            return "-1"
        return self.getdat(line.strip())

    def getSVNVersion(self,wcPath):
        ''' 获取wcPath目录的 svn版本

        返回 整数'''
        sNu = -1
        svnversionCMD = 'svnversion -n "%s"'%wcPath
        svnVersion =  os.popen(svnversionCMD).readlines()
        if (len(svnVersion)==0) or (svnVersion =='' ):
            return -1
        # print("version ",)
        #for s in svnVersion:
        #         print(s,)
        #print(']')
        if svnVersion[0] in 'exported' :
                print("Can't get svnversion")
                return -1
        else:
                #print(svnVersion)
                dv = svnVersion[0].split(':')
                #检测是否是混合模式 1:22M
                if len(dv) <2 :
                        #print('len(dv)<2')
                        sNu = self.getdat(svnVersion[0])
                else:
                        #print(dv)
                        #检查是否有m p s
                        sVersion = dv[1]
                        sNu =  self.getdat(sVersion)
        print('version:%d'%sNu)
        return sNu

    def getdat(self,line):
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
        ##                        result=0
        return result

class CWork:
    def __init__(self,major_Version=3,minor_Version=1,patch_Version=2,strComments="",outPutnewLine=""):
        global verCompanyName
        self.strComments=   strComments
        self.major_Version= major_Version
        self.minor_Version= minor_Version
        self.path_Version = patch_Version
        self.verFileDes = ""
        self.verCompanyName=verCompanyName.decode('gb2312')
        self.bOutPutnewLine = outPutnewLine
        #print(type(verCompanyName),verCompanyName)

        #.encode("utf-8")
        self.getVersionObj = CGetSvnVerion()
        self.getVersionInfo()
        #print("---"+verCompanyName)
        #print('getVersionInfo--: %d.%d.%d (%s)(%s)'%(self.major_Version,self.minor_Version,self.path_Version,verCompanyName,self.verFileDes))

    def isSvnControl(self,path):
        #print("isSvnControl--"+path)
        svnPath=path+"\\.svn\\"
        if os.path.exists(svnPath):
            return True
        return False
    def getVersionXmlPath(self):
        return self.getVersionXmlPath2()
        return self.getVersionXmlPath1()

    def getVersionXmlPath2(self):
        curPath = os.getcwd()
        xmlName="version.xml"
        xmlPath = os.path.join(curPath,xmlName)
        ssplit=curPath.split('\\')
        while len(curPath)>3:
            if not self.isSvnControl(curPath):
                return ""
            xmlPath= os.path.join(curPath,xmlName)
            if os.path.exists(xmlPath):
                #print("path2--:"+xmlPath)
                return xmlPath
            curPath = os.path.abspath(os.path.join(curPath,".."))
            #print(curPath)
        return ""
    def getVersionXmlPath1(self):
        '''获取路径：
            方案一：
                当前目录，.\
                上级目录，..\
                上级上级目录   ..\..\
                上级上级上级目录  ..\..\..\
            方案二：
                依次往上级目录找，并查看当前目录是否在svn控制下（存在 .svn 目录）
                如果没在svn控制下就停止查找，否则继续，直到根目录


                svnVer2rc.py 所在目录
        '''
        xmlName = "\\version.xml"
        curPath = os.getcwd()+"\\"
        xmlpath = curPath+xmlName
        if not os.path.exists(xmlpath):
            print("Find xml Faild:\n\t"+xmlpath)
            xmlpath=curPath+".."+xmlName
            if not os.path.exists(xmlpath):
                print("Find xml Faild:\n\t"+xmlpath)
                xmlpath = curPath+"..\.."+xmlName
                if not os.path.exists(xmlpath):
                    print("Find xml Faild:\n\t"+xmlpath)
                    xmlpath = curPath+"..\..\.."+xmlName
                    if not os.path.exists(xmlpath):

                        print("Find xml Faild:\n\t"+xmlpath)
                        curPath = sys.path[0]
                        if os.path.isfile(curPath):
                            curPath = os.path.dirname(curPath)

                        xmlpath = curPath+xmlName
                        if not os.path.exists(xmlpath):
                            print("Find xml Faild:\n\t"+xmlpath)
                            return ""
        return xmlpath


    def getVersionInfo(self):
        '''获取主版本号，子版本号，path_Version以及公司名称
            获取路径：
                当前目录，.\
                上级目录，..\
                上级上级目录   ..\..\
                上级上级上级目录  ..\..\..\
                svnVer2rc.py 所在目录
        '''
        xmlpath = self.getVersionXmlPath()
        if xmlpath=="":
            print("没有找到version.xml")
            return False
        print("xmlPath:"+xmlpath)

        xmldoc = minidom.parse(xmlpath)
        text = xmldoc.getElementsByTagName("major_Version")[0]
        for node in text.childNodes:
            self.major_Version=string.atoi(node.nodeValue)
        text = xmldoc.getElementsByTagName("minor_Version")[0]
        for node in text.childNodes:
            self.minor_Version=string.atoi(node.nodeValue)
        text = xmldoc.getElementsByTagName("path_Version")[0]
        for node in text.childNodes:
            self.path_Version=string.atoi(node.nodeValue)
        text = xmldoc.getElementsByTagName("verCompanyName")[0]
        for node in text.childNodes:
            self.verCompanyName=node.nodeValue
        text = xmldoc.getElementsByTagName("verFileDes")[0]
        for node in text.childNodes:
            s = node.nodeValue
            #strx =s.decode('utf-8','ignore').encode('gbk')
            #strx = s.encode('gb2312')
            self.verFileDes = s
            #print(str)

        return True




    def outPutnewLine(self,line):
        if self.bOutPutnewLine:
            print(line)

    def IsCompanyLine(self,line):
        '''检查是否是属于Company 行，

        '''
        if self.verCompanyName=="":
            return line
        newLine = line
        if 'CompanyName' in line:
            newLine='            VALUE "CompanyName",     "{0}\\0"\n'.format(self.verCompanyName.encode('gb2312'))
            self.outPutnewLine(newLine)
        return newLine
    def IsComments(self,line):
        if self.strComments=="":
            return (line,False)
        newLine = line
        bFind=False
        if 'Comments' in line:
                newLine='            VALUE "Comments",     "{0}\\0"\n'.format(self.strComments)
                bFind=True
        return (newLine,bFind)
    def IsFileDesLine(self,line):
        '''检查是否是文件描述行

        '''
        if self.verFileDes=="":
            return line
        newline = line
        global verVC
        if verVC == "vc9":
            if 'FileDescription' in line:
                newline='            VALUE "FileDescription", "%s"\n'%(self.verFileDes.encode('gb2312'))
                self.outPutnewLine(newline)
        else:
             if 'InternalName' in line:
                newline='            VALUE "InternalName","%s"\n'%(self.verFileDes.encode('gb2312'))
                self.outPutnewLine(newline)
        return newline

    def IsVersonLine(self,line,nVersion):
        '''检查是否是FILEVERSION 行,并把新版本号赋值进去

        '''
        newLine = line
        #print("isVersionLine",line,line in verFilter)
        for iLine in range(0,len(verFilter)):
            if verFilter[iLine] in line:
                #print("iLine in line",line,iLine)
                #strVersion='%d.%d.%d.%d'%(major_Version,minor_Version,path_Version,nVersion)
    #                newLine = verFormatStr[iLine]%(major_Version,minor_Version,path_Version,nVersion)
                newLine = verFormatStr[iLine].format(self.major_Version,self.minor_Version,self.path_Version,nVersion)
                self.outPutnewLine(newLine)
        return newLine
    def IsVersionBlock(self,line,bStart):
        '''
        判断是否在VS_VERSION_INFO 区域
        StringFileInfo
        VarFileInfo
        '''
        if bStart<>0 and "VS_VERSION_INFO" in line:
            self.outPutnewLine("VS_VERSION_INFO"+line)
            return 1
        elif bStart==0 and "END" in line:
            self.outPutnewLine("END" +line)
            return 2
        #elif bStart==0:
        #    print ">>>"+line
        return 0

    def Read_Write_File(self,rcPath,nVersion):
        '''读写 rc文件

        '''
        rcPathBk = rcPath+'bak'
        #先改变文件的只读属性
        os.chmod(rcPath,stat.S_IWRITE)
        try:
                fR = open(rcPath,'r')
                #print(fR)
        except IOError:
                print('Open file error.  ['+rcPath+']')
                faildInfo()
        try:
                fW = open(rcPathBk,'w')
                #print(fW)
        except IOError:
                print('Open bakfile error. ['+rcPathBk+']')
                faildInfo()
        try:
                bStart=-1
                bFindComments=False
                if self.strComments=="":
                    bFindComments=True
                for line in fR:
                      #  print(line)
                      ret =self.IsVersionBlock(line,bStart)
                      newLine =line
                      if ret==1:
                          bStart=0
                      elif ret ==2:
                          if False==bFindComments:
                              CommentLine='            VALUE "Comments",     "{0}\\0"\n'.format(self.strComments)
                              fW.write(CommentLine)
                          bStart=2
                          #break
                      #print("ret"+str(ret)+"__"+str(bStart))
                      if bStart==0:
                          newLine = self.IsVersonLine(line,nVersion)
                          newLine = self.IsCompanyLine(newLine)
                          newLine = self.IsFileDesLine(newLine)
                          if False==bFindComments:
                              newLine,bFindComments = self.IsComments(newLine)
                      fW.write(newLine)
                fR.close()
                fW.close()
        finally:
                fR.close()
                fW.close()
        #交换文件
        os.remove(rcPath)
        os.rename(rcPathBk,rcPath)



    ##            for root ,dirs,files in os.walk(path):
    ##                    result = glob.glob(os.path.join(root,p))
    ##                    for f in result :
    ##                            return f
    def CommitRc2Svn(self,rcPath,curVersion):
        ''' 提交rc 文件到svn

        rcPath:rc的路径  curVersion 当前版本号'''
        svnCMD = 'svn ci -m "Update version[{0}]"  '+rcPath
        svnCMD = str.format(svnCMD,curVersion)
        print(svnCMD)
        svnRet =  os.popen(svnCMD).readlines()
        #todo 验证是否提交成功
        ## commit 返回成功内容
        ##Sending        foo.rc
        ##Transmitting file data .
        ##Committed revision 5.
        if len(svnRet) != 3:
                print(svnRet)
                return False
        ver = svnRet[2].split(' ')
        nVer = getdat(ver[2])
        print("ver ={0}",nVer)
        if nVer != curVersion :
                strRet = "curVersion[{0}] != nVer[{1}]"
                strRet = str.format(strRet,curVersion,nVer)
                print(strRet)
                return False
        return True



    def DoWork(self,rcPath,bCommit):
        if rcPath=='' : faildInfo()
        if rcPath[1] !=':' :
             rcPath = os.getcwd()+'\\'+rcPath
            #split rcpath get WC path for svn
        print("----------------------------")
        print(rcPath)
        nPos = rcPath.rfind('\\')
        if nPos <0 : return
        wcPath = rcPath[:nPos]
        #print(wcPath)
        #vv = self.getVersion(wcPath)
        vv = self.getVersionObj.getVersion(wcPath)

        print('%d.%d.%d (r%d)'%(self.major_Version,self.minor_Version,self.path_Version,vv))
        if vv==-1 :
                faildInfo()
        #备份rc文件

        #distutils.file_util.copy_file(rcPath,rcPath+"cp")
        if bCommit == False :
            #把版本号写进rc 文件中
            self.Read_Write_File(rcPath,vv)
        else:
           #TODO 可以把rc 文件提交到svn
            vv+=1
            self.Read_Write_File(rcPath,vv)
            #提交到svn
            if self.CommitRc2Svn(rcPath,vv)==False :
                    print("Commit "+rcPath+" faild")
                    faildInfo()
        #distutils.file_util.copy_file(rcPath+"cp",rcPath)
        sucessInfo()
def Usage():
    print("Usage:")
    sUsage="-all   Update all '.rc' in curFloder and all subFloder\r"
    print sUsage
    sUsage="-f rcFilePath\r"
    print sUsage
    print "---------------------------"
    sUsage="-ci  after update rcFile,commit the rcfile to svn\r"
    print sUsage
def sucessInfo():
    print("write version sucess")
    #sys.exit()

def faildInfo():
    print("write version faild")
    sys.exit()
def FindRcFiles():
    path = os.getcwd()
    allresult=list()
    p =  '*.rc'
    for root, dirs, files in os.walk(path):
        result = glob.glob(os.path.join(root, p))
        for f in result:
            #print f
            allresult.append(f)
    return allresult

def find_One_RcFile():
    '''查找rc文件

    '''
    path = os.getcwd()
    #print(path)
    p='*.rc'
    list  = os.listdir(path)
    for line in list:
        filepath = os.path.join(path,line)
        if os.path.isfile(filepath):
                ext =  os.path.splitext(filepath)
                if ext[1] =='.rc':
                        #print(filepath)
                        return filepath
    print("can't find rc file")
    faildInfo()
    return ''

def main():
    if __name__ != '__main__':
            return
    #bCommit 界定 是否把rc 文件提交到svn
    print("svnver2rc")
    bCommit = False
    bAllRc = False
    rcPath = ""

    worker = CWork(patch_Version=2)

    for i in range(1,len(sys.argv)):
        print(str(i)+"___"+sys.argv[i])
        if sys.argv[i].startswith('-') :
            option = sys.argv[i][1:]
            #print(option)
            if option=="ci" :
                bCommit=True
            elif option=="f":
                rcPath =sys.argv[i+1]
            elif option=="h":
                Usage()
                sys.exit()
            elif option=="all":
                bAllRc = True
            elif option=="v":
                worker.strComments=sys.argv[i+1]
            elif option=="patch":
                worker.path_Version=int(sys.argv[i+1])

    if bAllRc==False:
        if rcPath=="":
            print('argv <2 .run by local rc file')
            #find local rc File
            rcPath=find_One_RcFile()
        if rcPath=="":
            print('Error:rcPath==""')
            return
        worker.DoWork(rcPath,bCommit)
    else:

            #递归遍历rc文件
           for rcPath in FindRcFiles():
                   #print(rcPath)
                   worker.DoWork(rcPath,bCommit)


print(__name__)
main()

