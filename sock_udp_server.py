import socket
import logging
fName1="logging2.txt"
fName2="logging2.txt"
def iniLog():
    logger = logging.getLogger()
    filehandler = logging.FileHandler(fName1)
    streamhandler = logging.StreamHandler()
    fmt = logging.Formatter('%(asctime)s,%(funcName)s,%(message)s')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(filehandler)
    logger.addHandler(streamhandler)
    return logger

#logging.basicConfig(filename=fName2,level=logging.INFO)
#logging.info("do 1")

logger = iniLog()

logger.info("do 2")

#===============================
asscii_string = lambda s: ' '.join(map(lambda c: "%02X"%ord(c),s))
print asscii_string('123st')

#===============================

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.bind(('',110))

print 'udpserver start'
icnt=0
dic =dict()
def processData(data,addr,port):
    nPos = data.find("YH AK ")
    if nPos>-1:
        server.sendto("YH CR :15608891961|K FF",(addr,port))

while True:
    data,(addr,port) = server.recvfrom(1024)
    #print icnt,data,addr,port
    logger.info('icnt=%d,data=%s,addr=%s,port=%d'%(icnt,data,addr,port))
    #logger.info('---xxx,data=[%s],addr=%s,port=%d'%(asscii_string(data),addr,port))
    icnt=icnt+1
    key="c_%s_%d"%(addr,port)
    dic[key] = (addr,port)
    processData(data,addr,port)
   # continue
    if icnt%5==0:
        print icnt
        i=0
        for k in dic.keys():
            print "dic-%d-%s__%s"%(i,k,dic[k])
            (addr1,port1) = dic[k]
            i=i+1
            server.sendto("server %d"%(icnt),(addr1,port1))
