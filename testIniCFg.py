# -*- coding: cp936 -*-
import iniCfg
import getIniContent
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import dump
CN_string={'Version_Info':{'en':'Version_Info','cn':u'�汾��Ϣ'},
           'CHANNEL_INFO':{'en':'CHANNEL_INFO','cn':u'ͨ����Ϣ'},
           'CHANNEL_0':{'en':'CHANNEL_0','cn':u'ͨ����Ϣ'},
           'CDD_BCCARD':{'en':'CDD_BCCARD','cn':u'�������'},
           'LanguageSet':{'en':'LanguageSet','cn':u'��������'},
           'MFSTYPE':{'en':'MFSTYPE','cn':u'mfs����'}, 
            'channel_id':{'en':'channel_id','cn':u'ͨ����'},
            'language':{'en':'language','cn':u'����'},
            'synchorphase':{'en':'synchorphase','cn':u'����λ'},
            'windowpositon_y':{'en':'windowpositon_y','cn':u''},
            'cardoutmode0':{'en':'cardoutmode0','cn':u''},
            'versiontype':{'en':'versiontype','cn':u''},
            'windowpositon_x':{'en':'windowpositon_x','cn':u''},
            'enablelocpreview':{'en':'enablelocpreview','cn':u''},
            'extmode':{'en':'extmode','cn':u''},
            'usecard0':{'en':'usecard0','cn':u'��Ӧʹ�ÿ���'},
            'outaudiobit':{'en':'outaudiobit','cn':u'�����Ƶλ��'},
            'syncverphase':{'en':'syncverphase','cn':u'����λ'},
            'hdshowsize':{'en':'hdshowsize','cn':u'������ʾ����'},
            'bismsvmfs':{'en':'bismsvmfs','cn':u''},
            'usecard_num':{'en':'usecard_num','cn':u'��ͨ��ʹ�ÿ���'},
            'sdshowsize':{'en':'sdshowsize','cn':u'������ʾ����'},
            'comm_port':{'en':'comm_port','cn':u'���ƶ˿�'},
             }
def TransStr(str):
    cn = CN_string.get(str)
    if cn is None:
        return str
    cn = cn.get('cn')
    #cn = CN_string[str]['cn']
    if cn=='': return str
    return cn

def indent(elem,level=0):
    i = "\n"+level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text=i+" "
        for e in elem:
            indent(e,level+1)
        if not e.tail or not e.tail.strip():
            e.tail = i
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail  =i
    return elem
def Save2XML(appName,cfgName):

    dic = iniCfg.GetConfig(cfgName)
    
    eTree = ElementTree()
    
    root = Element(appName)
    eTree._setroot(root)
    for subDic in dic:
        pos = subDic.find('.')
        #print "'"+skey[pos+1:]+"':{'en':"+skey[pos+1:]+"','cn':''},"
        sec =subDic[:pos]
        skey=subDic[pos+1:]
        #print 'sec:'+TransStr(sec)
        #print "____key:"+TransStr(skey)+"="+dic[subDic]
        SubElement(root,subDic,{"text":TransStr(skey),"desc":subDic,"category":TransStr(sec)}).text=dic[subDic]
    dump(indent(root))    
    eTree.write(appName+".xml","utf-8")
def Save2XML2(appName,cfgName):

    dic = getIniContent.getContent(cfgName)
    
    eTree = ElementTree()
    
    root = Element(appName)
    eTree._setroot(root)
    for subDic in dic:
        pos = subDic.find('.')
        #print "'"+skey[pos+1:]+"':{'en':"+skey[pos+1:]+"','cn':''},"
        sec =subDic[:pos]
        skey=subDic[pos+1:]
        print 'sec:'+TransStr(sec)
        va = dic[subDic]
        #dic["optname"]+" "+ dic["value"]+" "+ dic["rem"]
        #print "____key:"+TransStr(skey)+"="+dic[subDic]
        print va.get("rem")
        SubElement(root,subDic,{"text":TransStr(skey),"desc":va.get("rem"),"category":TransStr(sec)}).text=va.get("value")
    #dump(indent(root))    
    eTree.write(appName+".xml","utf-8")
      
Save2XML('msvBoardCast','CDD_BCSDK.INI')
    
