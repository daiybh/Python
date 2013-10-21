import ConfigParser
import string,os,sys

def GetConfig(cfgPath):
    cf = ConfigParser.ConfigParser()
    cf.read(cfgPath)

    sections= cf.sections()
    #print 'section:',sections
    dic = dict()
    for subSection in sections:        
        items = cf.items(subSection)
        for subItem in items:
            sKey = subSection+"."+subItem[0]
            dic[sKey]=subItem[1]
    return dic

def main():
    if __name__ != '__main__':
                return
def ReadIni(fn):                
    f = open(fn)
    text = f.read()
    f.close()    
    
    lines = text.splitlines()
    for line in lines:
        line = line.strip()
        if(line == ""):
            continue
        if(line.startswith(";")):
            continue
        if(line.startswith("[")):
            line = line.replace("[","")
            line = line.replace("]","")
            print "section"+line
            continue
        arr = line.split("=")
        key = arr[0].strip()
        value = arr[1].strip()
        
main()
#dc = GetConfig("MgCaptureCfg.ini")
#for xd in dc.items():
#    print xd[0],"=",xd[1]



    

