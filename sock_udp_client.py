import socket
import time
client = socket.socket( socket.AF_INET,socket.SOCK_DGRAM)
client.settimeout(1)
icnt=0
while True:
    strx = "Hell python %d"%(icnt)
    strx ="48 65 6C 6C 20 70 79 74 68 6F 6E 20 33 30 %d"%(icnt)
    strx="YH AN :15608891962 090506172220|0|0|0|0|0|80000000|00000000,00000000|0 E9D\r\n"
    strx="YH AP :15608891962 120223075300|5611A75|160B6ECA|775|31|0|00000000|00000000,00000000|0,1A 12C3\r\n"
    strx="YH AP :15608891961 120311094200|561F5E8|160B4FC8|3|0|0|00000000|00000000,00000000|0,1C 122E\r\n"
    strx="YH AP :15608891961 120315090923|561FDF8|160B52A4|5|0|33|00000000|00000000,00000000|0,1D 126A\r\n"
    #print strx
    strIp="127.0.0.1"
    nCnt = client.sendto(strx,(strIp,110))
    print "nCnt",nCnt,"---strx",strx
    time.sleep(10)
    icnt =icnt+1
    try:
        data,(addr,port) =client.recvfrom(1024)
        print "-recv-",data,addr,port
    except (socket.error,socket.timeout):
        print("socket.timeout")
    else:
        pass
    
client.close()
