import os
import time

def ExeBatCmd(batcmd):
    #print batcmd
    return  os.popen(batcmd).readlines()
    
user=['tc\yangchuang']
user=['tc\hetao']
#user+=['tc\zhangshunhong']
#user+=['tc\yangjun01']
server=' /server:http://172.16.254.85:8080/'
login=' /noprompt /login:tc\yangjun01,Yangjun20107'
fileNameext=str(time.time())
saveResultPath='d:\\'
print fileNameext
class TFS:
    
    user=''
    workspace=''
    fileNameext=''
    
    
    def __init__(self, user='', workspace=''):
        
        self.user=user        
        self.workspace=' /workspace:'+workspace+';'+user
        self.fileNameext=fileNameext+'_'+self.user.replace('\\', '_')+'_'
        
        print("tfs init", user, workspace, self.user, self.workspace, self.fileNameext)
        
    def saveResult(self,result):
        filename=saveResultPath+'tfs_'+self.fileNameext+'.txt'
        #print "saveResult",filename,result
        fW = open(filename,'a')
        fW.write('========'+self.workspace+'=======\n')
        for r in result:
            fW.write(r)
        fW.close()
        
    def saveUndoResult(workspace,item,result):
        saveResult("undo",workspace+item,result)
        
    def doUndo(self,item,fW):
        if len(item)<2:
            return
        batcmd='tf undo '+self.workspace+' "'+item+'" '+server+' '+login
        
        result=ExeBatCmd(batcmd)
        fW.write(batcmd)
        fW.write('\n')
        for r in result:
            fW.write(r)
            fW.write('\n')
        #saveUndoResult(workspace,item,result)
            
    def findstatus(items):
        i=0
        for item in items:
            if item=='!':
                return items[i+1]
            i=i+1
                
    def doUndos(self,result):
        basePath=result[2]
        basePath=basePath[:-1]+'/'
        print 'base'+basePath
        
        filename=saveResultPath+'\\tfs_'+self.fileNameext+'undoed.txt'
        fW = open(filename,'a')
        fW.write('========'+self.workspace+'=======\n')
        
        i=0
        for itemarr in result[3:]:
            items = itemarr.split(' ')
            try:
                if len(items)<10:
                    continue
                
                status=findstatus(items)
                if status!='edit':
                    continue            
                #fW.write(itemarr)
                #fW.write('\n')
                self.doUndo(basePath+items[0],fW)
            except Exception as err:
                pass
                continue
                print err
                print itemarr,items
                print len(items)
        fW.close()
            
        
    def doStatus(self):
        batcmd='tf status'+server+self.workspace+login
        result=ExeBatCmd(batcmd)
        if len(result)>1:
            self.saveResult(result)
            self.doUndos(result)
    
def doGetWorkspaces(user):
    batcmd = 'tf workspaces /owner:'+user+server+login
    workspaces=ExeBatCmd(batcmd)            
    
    for ws in (workspaces[3:]):#no include frist 3line.
        print ws
        ws1= ws.split(' ')
        tfs = TFS(user,ws1[0])
        tfs.doStatus()
        
for u in(user):
    print u
    doGetWorkspaces(u)
print "\r\n******end******\r\n"
    
    




