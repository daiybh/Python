# -*- coding: cp936 -*-
import os,sys
oldList =[]
AllList =[]
curFile=[]
def listDir(path):
    list  = os.listdir(path)
    for line in list:
        filepath = os.path.join(path,line)
        print(filepath)
#listDir("\\\\172.16.32.26\\h\\MSV版本提交\\Msv555&4211P\\MediaFileSystem\\")

bigfiles = {"filelist":[],
            'extensions':['.sys'],
            'size_limit':100000,
            }
def find(func,rootdir,arg=None):
    files = os.listdir(rootdir)
    files.sort(lambda a,b:cmp(a.lower(),b.lower()))
    for file in files:
        fullpath = os.path.join(rootdir,file)
        if os.path.islink(fullpath):
            pass
        elif os.path.isfile(fullpath):
            func(fullpath,arg)
        else:
            print 'find',fullpath
def checksize3(fullpath,arg):
    ext = os.path.splitext(fullpath)[1]
    import fnmatch
    for s in arg['extensions']:
        if s.lower()==ext.lower():
        #if fnmatch.fnmatch(ext,s):
            print 'checksize',fullpath,ext,s
            size=os.path.getsize(fullpath)
            arg['filelist'].append({'size':size,'name':fullpath})

        

find(checksize3 ,"c:\\",bigfiles)
