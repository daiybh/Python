# -*- coding: cp936 -*-
import xml.dom.minidom
import codecs
import os
fileName='d:/test.xml'
def t(value):
    dom = xml.dom.minidom.parse(fileName)
    root = dom.documentElement
    root.setAttribute('len',value)
    root.toxml()
    f = file(fileName,'w')
    writer = codecs.lookup('utf-8')[3](f)
    dom.writexml(writer,encoding='utf-8')
    writer.close()
    


def makeAttrib(dom,attribName,value):
    attrib = dom.createAttribute(attribName)
    attrib.appendChild(value)
    return attrib
                                 
                                 
def write():
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None,'catalog',None)
    root = dom.documentElement
    text=unicode('汉字','cp936')
    item=makeEasyTag(dom,'item',text)
    root.appendChild(item)
    #xx = makeAttrib(dom,'len','xd')
    #.appendChild(xx)
    root.setAttribute('len','x')
    root.toxml()
    f=file('d:/test.xml','w')
    
    writer = codecs.lookup('utf-8')[3](f)
    dom.writexml(writer,encoding='utf-8')
    writer.close()

import string
import datetime
class Save2xml():
    '''save conversation to xml'''

    def __init__(self):
        pass
    def OpenFile(self,_xmlFileName):
        self.xmlFileName = _xmlFileName
        if os.path.exists(self.xmlFileName)==False:
            self.logFilexml = open(self.xmlFileName,'w')
            self.logFilexml.write('<?xml version="1.0"?>\n')
            self.logFilexml.write("<?xml-stylesheet type='text/xsl' href='MessageLog.xsl'?>\n<Log FirstSessionID='1' LastSessionID='0'></Log>")
            self.logFilexml.flush()
            self.logFilexml.close()
        self.dom = xml.dom.minidom.parse(self.xmlFileName)
        self.root = self.dom.documentElement
        self.LastSessionID = self.root.getAttribute('LastSessionID')
        self.CurrentSessionID=str(string.atoi(self.LastSessionID)+1)
        self.root.setAttribute('LastSessionID',self.CurrentSessionID)
    def WriteContent(self,content):
        #root = self.dom.documentElement
        item= makeEasyTag(self.dom,"Message","")
        item.setAttribute('SessionID',self.CurrentSessionID)
        curDateTuple=self.GetCurDate()
        item.setAttribute('Date',curDateTuple[0])
        item.setAttribute('Time',curDateTuple[1])
        item.setAttribute('DateTime',curDateTuple[2])
        
        itemFrom = makeEasyTag(self.dom,"From","")
        itemUser = makeEasyTag(self.dom,"User","")
        itemUser.setAttribute('FriendlyName','From')
        itemFrom.appendChild(itemUser)
        item.appendChild(itemFrom)
        itemTo = makeEasyTag(self.dom,"To","")
        itemUser = makeEasyTag(self.dom,"User","")
        itemUser.setAttribute('FriendlyName','Send')
        
        itemTo.appendChild(itemUser)
        item.appendChild(itemTo)
        itemText = makeEasyTag(self.dom,"Text",content)
        #itemText.setAttribute("Style",'font-family:Sans; color:#000000;')
        item.appendChild(itemText)
        self.root.appendChild(item)
        self.root.toxml()
        
    def CloseFile(self):
        f = file(self.xmlFileName,'w')
        import codecs
        writer=codecs.lookup('utf-8')[3](f)
        self.dom.writexml(writer,encoding='utf-8')
        writer.close()
        
        
    def GetCurDate(self):
        dt = datetime.datetime.today()
        return dt.date().isoformat(),dt.strftime("%H:%M:%S"),dt.isoformat()
    
    def __makeEasyTag(self,dom,tagname,value,type='text'):
        tag = dom.createElement(tagname)
        if value:
            if value.find(']]>')>-1:
                type='text'
            if type=='text':
                value=value.replace('&','&amp;')
                value=value.replace('<','&lt;')
                text = dom.createTextNode(value)
            elif type=='cdata':
                text = dom.createCDATASection(value)
            tag.appendChild(text)        
        return tag
    
xx = Save2xml()
xx.OpenFile(fileName)
x = 0
while x<10:
    xx.WriteContent("shit"+str(x))
    x=x+1
xx.CloseFile()
                            
