# -*- coding: cp936 -*-
'''���ҵ�ǰdsp �ļ��� �Ƿ���
        # Begin Special Build Tool
        SOURCE="$(InputPath)"
        PreLink_Cmds=svnVer2rc.py
        # End Special Build Tool
'''
'''
    ��ȡ # Begin Target

        # Name "TestSvn - Win32 Release"
        # Name "TestSvn - Win32 Debug"
        # Name "TestSvn - Win32 DebugU"
    �����м�������ѡ��

    �ٴ�ͷ��ʼ��ȡ ������ô�Ŀ�  !IF  !ELSEIF  !ENDIF
    ����������Ƿ��� FindFiter
    û�� �Ͱ�FindFiter��ӵ�β��
'''
import os
FindFiter = ['# Begin Special Build Tool\n',
            'SOURCE="$(InputPath)"\n',
            'PreLink_Cmds=svnVer2rc.py\n',
            '# End Special Build Tool\n']

def IsInLine(line):
    '''�жϵ�ǰ���Ƿ����� FindFiter

    '''
    sList=[]
    #print(line)
    for i in FindFiter:
        pos = cmp(i,line)
        if pos==0:
            print(pos,i,line)
            sList.append(line)
    return sList

def breakForTarget(lRet):
    if len(lRet)>0:
       return True    
    return False
def IsBeginTarget(line,f):
    nameList =[]
    
    pos = cmp(line,'# Begin Target\n')
    if pos ==0 :
       # print(line)
        #���� name
        for newLine in f:
            if cmp(newLine,'# Begin Group "Source Files"\n')==0 :
               break
            elif cmp(newLine,'# Name')>0:
                pos = newLine.index('"')
                pos2 = newLine.rindex('"')
                name = newLine[pos:pos2+1]
                #print('ffff',name,pos,pos2)
                nameList.append(name)
    return nameList
def Read_Write_File(rcPath,nVersion):
        '''��д �ļ�

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
                   #   newLine = IsVersonLine(line,nVersion)
                      #newLine = IsInLine(line)
                      newLine = IsBeginTarget(line,fR)
                      fW.write(newLine)
                fR.close()
                fW.close()
        finally:
                fR.close()
                fW.close()
        #�����ļ�
        os.remove(rcPath)
        os.rename(rcPathBk,rcPath)
        
def Read_File(rcPath,opCB,isBreakCB):
        '''���ļ�

        '''
        try:
                fR = open(rcPath,'r')                
                #print(fR)
        except IOError:
                print('Open file error.  ['+rcPath+']')
                faildInfo()
        try:
                for line in fR:
                    #  print(line)
                   #   newLine = IsVersonLine(line,nVersion)
                      #newLine = IsInLine(line)
                      lRet = opCB(line,fR)
                      if isBreakCB(lRet) :return lRet
                fR.close()
        finally:
                fR.close()
        #�����ļ�
filePath = 'testsvn.dsp'

def breakForFindFilter(lRet):
    
    if len(lRet) >0:
        print lRet
        return True
    return False
nameList= Read_File(filePath,IsBeginTarget,breakForTarget)
#print nameList
#def ReadHuge(filePath):
def FindABlockContent(line,f,fW):
    print("FindABlockContent",line)
    bReturn = False 
    for line in f:
        #�ж��Ƿ��˽���    
        if line[0] =='!':
            if line.find('!ELSEIF')==0:
                #�ҵ� ��������ж�ǰһ�������Ƿ��Ѿ�����������Ҫ���ֶ�
                #line = '!ELSEIF 1234567890\n'                
                bReturn = True
            elif line.find('!ENDIF')==0:
                #line += '!ENDIF 1234567890\n'
                bReturn = True
            #�������if
            #elif line.find('!IF')==0:
            #    line += '!IF 1234567890'
        fW.write(line)
        if bReturn :
            print("�滻",line)
            return
        #IsInLine(line)
        
def FindBlockHead(line,f,fW,total):
    fW.write(line)
    for iName in nameList:
        #print(line,iName)
        if line.find(iName) >0:
            if line[0] =='!':
               if line[1] =='M':
                    continue
               elif line[1] =='I': #!IFDEF
                   #���� !ELSEIF  !ENDIF
                   print('ifdef',line)
                   #һֱ�� ���� ��һ�� !
                   FindABlockContent(line,f,fW)                      
               elif line[1] =='E':#!ELSEIF
                   #��Ҫ���� !ENDIF
                   print('Elseif',line)
                   FindABlockContent(line,f,fW)
def ReadANameBlock(name):
    total=0
    fR = open(filePath,'r')
    fW = open(filePath+'bak','w')
    for line in fR:
        total = total+1
        FindBlockHead(line,fR,fW,total)
            
    fR.close()

ReadANameBlock('fl')
