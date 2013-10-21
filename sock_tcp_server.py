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

logger = iniLog()
logger.info("do 2")

s=socket.socket()

#s.bind(('172.16.134.10',110))
s.bind(('localhost', 110))
s.listen(5)
icnt=0
while 1:
    cs,address=s.accept()
    #print("got connected from %s"%(address))
    #cs.send("welcome")
    ra = cs.recv(512)
    logger.info('icnt=%d,data=%s'%(icnt,ra))
    
                
    print(ra)
    cs.close()
