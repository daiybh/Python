# -*- coding:utf-8 -*-
import os
filePath = "e:\\ireader\\2066\\"

def read_split():
    fR = open("e:\\ireader\\2066.txt",'r')

    findStr ="正文 第"
    iCnt =0

    findStrLen=len(findStr)
    print findStrLen
    #os.makedirs(filePath)
    filePath = filePath.decode('utf-8')
    filename= u'd:\\1.txt'
    fW = open(filename,'w')

    for line in fR:

        pos = line.find(findStr)
        
        if pos < 0:
            fW.write(line)
            continue
        if iCnt < 226:
            continue

        #属于章节开始
        
        pos1 = line.find('章')
        title = line[findStrLen:pos1]
        title = title.decode('utf-8')
        #filename="{0}{1:05}__{2}{3}".format( filePath,str(iCnt),title,".txt")
        #filename.format("{0}{1:05}__{2}{3}", filePath,str(iCnt),title,".txt")
        #filename="{0}{1:05}__{2}{3}"%( filePath,str(iCnt),title,".txt")
        filename="{0}{1:05}__.txt".format( filePath,(iCnt))
        
        iCnt = iCnt+1
        fW = open(filename,'w')
        fW.write(line)
fliters=['鲨鱼文学网 www.512SY.com 小说更新最快网站',
        '鲨鱼文学网 www.512Sy.com',
        '百度 鲨鱼文学 www.512sy.com',
        '鲨鱼文学网',
        'www.512Sy.com']
def delFliter(line):
    for fliter in fliters:
        line = line.replace(fliter,'')
    line = line.replace('\n','')
    line = line.replace('\r','')
    return line

def display(iCnt):
    filename ="{0}{1:05}__.txt".format( filePath,(iCnt))
    #print filename
    if os.access(filename,os.R_OK)==False:
        return 0
    fR = open(filename,'r')
    iDisplayCnt=0
    for line in fR:
        print delFliter(line)
        if iDisplayCnt > 10:
            print "---------------------------------------"
            raw_input()
            iDisplayCnt =0
        iDisplayCnt = iDisplayCnt+1

    fR.close()
    os.remove(filename)
    return 1

i_C_Cnt = 826

for i in range(0,i_C_Cnt):    
    filename ="{0}{1:05}__.txt".format( filePath,(i))
    if os.access(filename,os.R_OK):
        os.remove(filename)

while True:
    if 0==display(i_C_Cnt):
        i_C_Cnt=i_C_Cnt+1
        continue
    iNext = raw_input("Exit??")
    if iNext!="e":
        i_C_Cnt=i_C_Cnt+1
    else:
        break
        
        
    
    
