# -*- coding: cp936 -*-
import os
import time


def ExeBatCmd(batcmd):
    print batcmd
    return  os.popen(batcmd).readlines()
user=['tc\yangchuang']
user=['tc\hetao']
#user+=['tc\zhangshunhong']
#user+=['tc\yangjun01']
user=['tc\huangrong']
user=['tc\zhangshunhong']
server=' /server:http://172.16.254.85:8080/'
login=' /noprompt /login:tc\yangjun01,Yangjun20107'
login=' /noprompt /login:tc\daili,Bssb21'
fileNameext=str(time.time())
fileNameext='0000'
saveResultPath='d:\\'
print fileNameext
s1 = "编码"
print s1
print unicode('汉字', 'cp936')
print unicode(s1, 'cp936')

#s1.decode('gbk', 'ignore')


class TFS:
    user=''
    workspace=''
    fileNameext=''

    def __init__(self, user='', workspace=''):
        self.user=user
        self.workspace = ' /workspace:%s;%s'%(workspace, user)
        self.fileNameext=fileNameext+'_'+self.user.replace('\\', '_')+'_'
        print("tfs init",
        user, workspace, self.user, self.workspace, self.fileNameext)

    def saveResult(self, result):
        filename=saveResultPath+'tfs_'+self.fileNameext+'.txt'
        #print "saveResult", filename, result
        fW = open(filename, 'a')
        fW.write('========'+self.workspace+'=======\n')
        for r in result:
            fW.write(r)
        fW.close()

    def saveUndoResult(self, workspace, item, result):
        self.saveResult("undo", workspace+item, result)

    def doUndo(self, item, fW):
        if len(item)<2:
            return
        batcmd='tf undo '+self.workspace+' "'+item+'" '+server+' '+login
        result=ExeBatCmd(batcmd)
        fW.write(batcmd)
        fW.write('\n')
        print result
        for r in result:
            fW.write(r)
            fW.write('\n')
        #saveUndoResult(workspace,item,result)
    def findstatus(self, items):
        i=0
        for item in items:
            if item=='!':
                return items[i+1]
            i=i+1

    def doUndos(self, result):
        basePath=result[2]
        basePath=basePath[:-1]+'/'
        print 'base'+basePath
        filename=saveResultPath+'\\tfs_'+self.fileNameext+'undoed.txt'
        fW = open(filename, 'a')
        fW.write('========'+self.workspace+'=======\n')
        i=0
        print "u--------n----d---o\r\n"
        for itemarr in result[3:]:
            items = itemarr.split(' ')
            try:

                if len(items)<5:
                    print len(items), "<<5 cotinue"
                    continue
                status=self.findstatus(items)
                if status!='edit' and status!='编辑':
                    continue
                print '---->', status
                #fW.write(itemarr)
                #fW.write('\n')
                self.doUndo(basePath+items[0], fW)
            except Exception as err:
                print "exception", err
                pass
                continue
                print err
                print itemarr, items
                print len(items)
        fW.close()

    def doStatus(self):
        batcmd='tf status'+server+self.workspace+login
        result=ExeBatCmd(batcmd)
        if len(result)>1:
            self.saveResult(result)
            self.doUndos(result)


def doUndo():
    cmd='tf status /server:http://172.16.254.85:8080/ /workspace:TEST-X1;tc\zhangshunhong /noprompt /login:tc\daili,Bssb21'
    re= ExeBatCmd(cmd)
    print re
    tfs=TFS("tc\zhangshunhong", "TEST-X1")
    tfs.doUndos(re)
#doUndo()
#user=''

def doGetWorkspaces(user):
    batcmd = 'tf workspaces /owner:'+user+server+login
    workspaces=ExeBatCmd(batcmd)
    print workspaces
    for ws in (workspaces[3:]):#no include frist 3line.
        print ws
        ws1= ws.split(' ')
        tfs = TFS(user, ws1[0])
        tfs.doStatus()

for u in(user):
    print u
    doGetWorkspaces(u)
print "\r\n******end******\r\n"
