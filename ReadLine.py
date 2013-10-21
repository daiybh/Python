import os
import stat
import string
import sys
import glob
txtName="233"
txtName="244"
txtPath="d:/"+txtName+".txt"
txtPathBak="d:/"+txtName+"_bak.txt"
fR = open(txtPath,'r')
fW = open(txtPathBak,'w')
iGop=0
iGopCount=0
for line in fR:
    #print(line)
    if len(line)>5:
        if "nTypeV0=1" in line:
            line =str(iGop)+"__"+str(iGopCount)+"----"+line
            iGop+=1
            iGopCount=0
            fW.write(line)
            
        elif "postCount" in line:
            if "framtype=1" in line:
                line=str(iGop)+"__"+str(iGopCount)+"----"+line
                iGop+=1
                iGopCount=0
                fW.write(line)
            iGopCount+=1

fR.close()
fW.close()
