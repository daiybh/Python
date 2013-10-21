
import ctypes
def GetMsnUserID(msnLoginName):
    name = ""
    name = msnLoginName.split('@')[0]
    w=""
    result=0

    for s in msnLoginName:
        acc = ord(s)

        result = result*101
        result = result&0xffffffff
        result=result+acc
        #print "sub:__"+s+"__"+str(acc)+"___"+str(result)

    print "result:"+name+str(result)

arr=('long_gun@live.cn','daiybh@gmail.com','bardway@live.com')
for x in arr:
    GetMsnUserID(x)
