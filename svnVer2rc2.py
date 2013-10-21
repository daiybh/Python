# -*- coding: cp936 -*-
''' ��ȡsvn �汾��

'''
import os
import string
import sys
import glob
def getdat(line):
        ''' �����ַ����е�����

        �����ַ����е�����'''
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

def getVersion(wcPath):
        ''' ��ȡwcPathĿ¼�� svn�汾

        ���� ����'''
        sNu = -1
        svnversionCMD = 'svnversion -n '+wcPath
        svnVersion =  os.popen(svnversionCMD).readlines()
        #print(svnversionCMD)
        print(svnVersion)
        if svnVersion =='' : return -1
        if svnVersion[0] in 'exported' :
                print("Can't get svnversion")
                return -1
        else:
                #print(svnVersion)
                dv = svnVersion[0].split(':')
                #����Ƿ��ǻ��ģʽ 1:22M
                if len(dv) <2 :
                        print('len(dv)<2')
                        sNu = getdat(svnVersion[0])
                else:
                        #print(dv)
                        #����Ƿ���m p s
                        sVersion = dv[1]
                        sNu =  getdat(sVersion)
        return sNu

def IsVersonLine(line,nVersion):
        '''����Ƿ���FILEVERSION ��,�����°汾�Ÿ�ֵ��ȥ

        '''
        newLine = line
        if 'FILEVERSION' in line:
                #print('fileversinon'+line)
                #find laest ','
                pos = newLine.rindex(',')
                newLine = newLine[:pos+1]
                strNu = '{0}\n'.format(nVersion)
                newLine +=strNu
                #print(newLine)
        elif 'FileVersion' in line:
                pos = newLine.rindex(',')
                newLine = newLine[:pos+1]
                strNu = 'r{0}\\0"\n'.format(nVersion)
                newLine = newLine + strNu
                #print(newLine)
        return newLine

def Read_Write_File(rcPath,nVersion):
        '''��д rc�ļ�

        '''
        rcPathBk = rcPath+'bak'
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
                for line in fR:
                      #  print(line)
                      newLine = IsVersonLine(line,nVersion)
                      fW.write(newLine)
                fR.close()
                fW.close()
        finally:
                fR.close()
                fW.close()
        #�����ļ�
        os.remove(rcPath)
        os.rename(rcPathBk,rcPath)

def findRcFile():
        '''����rc�ļ�

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
##        for root ,dirs,files in os.walk(path):
##                #print(root)
##                result = glob.glob(os.path.join(root,p))
##                for f in result :
##                        ##print(f)
##                        return f
def CommitRc2Svn(rcPath,curVersion):
        ''' �ύrc �ļ���svn

        rcPath:rc��·��  curVersion ��ǰ�汾��'''
        svnCMD = 'svn ci -m "Update version[{0}]"  '+rcPath
        svnCMD = str.format(svnCMD,curVersion)
        print(svnCMD)
        svnRet =  os.popen(svnCMD).readlines()
        #todo ��֤�Ƿ��ύ�ɹ�
        ## commit ���سɹ�����
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

def Usage():
    print("Usage")
    print('''version = 1.0
    Write SvnVersion to Rc File.
    ''')
def sucessInfo():
        print("write version sucess")
        sys.exit()

def faildInfo():
        print("write version faild")
        sys.exit()
def main():
        if __name__ != '__main__':
                return

        #bCommit �綨 �Ƿ��rc �ļ��ύ��svn
        bCommit = False
        if len(sys.argv) <2 :
                print('argv <2 .run by local rc file')
                #find local rc File
                rcPath = findRcFile()
        else:
                #rcPath = sys.argv[1]
        for i in range(1,len(sys.argv)):
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


        if rcPath=='' : faildInfo()
        if rcPath[1] !=':' :
                rcPath = os.getcwd()+'\\'+rcPath
        #split rcpath get WC path for svn
        print(rcPath)
        nPos = rcPath.rfind('\\')
        if nPos <0 : return
        wcPath = rcPath[:nPos+1]
        vv = getVersion(wcPath)
        print(vv)
        if vv==-1 :
                faildInfo()
        if bCommit == False :
                #�Ѱ汾��д��rc �ļ���
                Read_Write_File(rcPath,vv)
        else:
           #TODO ���԰�rc �ļ��ύ��svn
                vv+=1
                Read_Write_File(rcPath,vv)
                #�ύ��svn
                if CommitRc2Svn(rcPath,vv)==False :
                        print("Commit "+rcPath+" faild")
                        faildInfo()
        sucessInfo()

main()
