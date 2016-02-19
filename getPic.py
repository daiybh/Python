import time
import urllib
import os

from PIL import Image

savePath='F://td//'

def gDownloadWithFilename(url,savePath,file):
    
    try:
        urlopen=urllib.URLopener()
        fp = urlopen.open(url)
        data = fp.read()
        fp.close()
        file=open(savePath + file,'w+b')
        file.write(data)
        print "down sucess"+ url
        file.close()
    except Exception as e:
        print "down failed"+ url
        print e
        
iCount =0
def getFileName(iCount):
    
    return str(iCount)+".gif"


def getFile():
    url ="http://rd2.zhaopin.com/s/loginmgr/picturetimestamp.asp"
    for i in range(0,100):
        filename= getFileName(i)
        gDownloadWithFilename(url,savePath,filename)
        
#getFile()

import pytesseract


def dotesseract_img(img):
    sret=(pytesseract.image_to_string(img))
    #print sret
    return sret

def dotesseract_file(path):
    print path,Image.open(path)
    return dotesseract_img(Image.open(path))

def writetoFile(sf,content):
    sf.write(content+'\n')
    
class doW(object):
        
    iC=0
    iI=0
    iSame=0
    def makeANewPic(self,org_filePath,dest_filePath):
        
        image = Image.open(org_filePath)
        c=Image.new("RGB",image.size,"white")
        
        for i in range(image.size[1]):
            for j in range(image.size[0]):
                if image.getpixel((j,i))<212:
                    c.putpixel([j,i],0)
        cS=c.resize((144,52))
        cS.save(dest_filePath)
        
    def getColor(self,saveFile,filePath):
        writetoFile(saveFile,filePath)
        
        image = Image.open(filePath)
        w,h = image.size
        c=Image.new("RGB",(w,h),"white")
        for i in range(0,h):
            outstr=""
            for j in range(0,w):
                if image.getpixel((j,i))<212:
                    outstr+="*"
                    c.putpixel([j,i],255)
                else:
                    outstr+=" "
            
            #print outstr
            #writetoFile(saveFile,outstr)
        #c.save("f:\\kkkk.jpg")
        sretImage=dotesseract_img(image)
        #writetoFile(saveFile,sretImage)
        sretC =dotesseract_img(c)
        writetoFile(saveFile,sretImage+"__"+sretC)
        if len(sretImage)==4:
            self.iC+=1
        if len(sretC)==4:
            self.iI+=1
        if sretC==sretImage:
            self.iSame+=1
        
    def getColors(self):
        sf = open("f:\\result.txt","w")
        for i in range(100):
            self.getColor(sf,"F:\\td\\"+str(i)+".jpg")
        sf.write("ic="+str(self.iC)+"   iI="+str(self.iI)+"   iSame="+str(self.iSame))
        sf.close()
    def makeNewPicS(self):
        if os.path.exists("F:\\td\\learingData_new\\")==False:
            os.makedirs("F:\\td\\learingData_new\\") 
        for i in range(100):
            self.makeANewPic("F:\\td\\learingData\\"+str(i)+".gif","F:\\td\\learingData_new\\"+str(i)+".gif")

dd = doW()
#dd.getColors()
dd.makeNewPicS()
def test_tesseract():
    iSucessCount=0
    for i in range(100):
        sret = dotesseract("f:\\td\\"+str(i)+".jpg")
        print i,sret
        if len(sret)==4:
            iSucessCount+=1
    print iSucessCount
 
#test_tesseract()

print "End"