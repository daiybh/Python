# -*- coding: cp936 -*-


rText="e:/workspace\python/android_Fliter.txt"
wText="e:/workspace\python/android_Fliter_w.txt"
find_Mark='　　String'
def DoWork():
    
    fR = open(rText,'r')

    fW = open(wText,'w')

    for line in fR:
        startpos=-1
        totalLen =len(line)
        print('totalLen %d----%s'%(totalLen,line[:10]))
        sSplitV = line.split(find_Mark)
        startpos = line.find(find_Mark)
        print('startpos %d---splitv %d'%(startpos,len(sSplitV)))

        lastpos=0      
        while startpos>-1 and startpos <totalLen:
            #print('startpos %d lastpos %d--%s'%(startpos,lastpos,line[lastpos:startpos]))
            fW.write(line[lastpos:startpos]+"\n")
            lastpos= startpos
            startpos = line.find(find_Mark,startpos+1)
print('---'+find_Mark)
DoWork()
