import socket
import time
import binascii

#车辆id
strVehiceID='6120324362'
#每条消息的时间间隔 秒
nSleepTime=10
nRecordID=0

def getSendStr():
    ''' 生成需要发送的16进制报文
    '''
    strtime1='071756050413'
    strtime=time.strftime('%H%M%S%d%m%y',time.localtime(time.time()))
    strRet='24{0}{1}2504909000102440407e000312fffffbffff00{2:02x}'.format(strVehiceID,strtime,nRecordID)
    #
    return strRet
while True:
    sock2 = socket.socket()
    try:
        sock2.connect(('127.0.0.1',110))
    except Exception as ex:
        #print(Exception,":",ex)
        time.sleep(10)
        continue

    bClose=False   
    
    if True:
        print("start--send")
        try:
            #sock2.send("*HQ,6120108242,V1,092254,A,2500.0314,N,10246.4840,E,0.00,110,260312,FFFFFBFF#")
            #sock2.send("*HQ,6120108253,V1,235955,V,0000.0000,N,00000.0000,W,0.00,000,050180,FFFFFBFF#")
            sendStr=getSendStr()
            print(sendStr)
            sock2.send(binascii.a2b_hex(sendStr))
           # data = sock2.recv(512)
           # print('Recv'+":",data)
            time.sleep(10)
        except Exception as ex:
            print(Exception,":",ex)
            sock2.close()
            bClose=True
    if bClose==False:
        sock2.close()
    nRecordID=nRecordID+1

    time.sleep(10)
sock2.close()
s.close()
