# -*- coding: cp936 -*-
'''��ȡsvn �汾��
'''
import os
import glob
import fnmatch

def textFinder(dir):
    txtList = glob.glob(os.path.join(dir,'*.rc'))
    return txtList
fileExt=['.exe','.dll']
def find_One_RcFile():
    '''����rc�ļ�

    '''
    path = os.getcwd()
    #print(path)
   # return textFinder(path)
    p='*.rc'
    listDir  = os.listdir(path)
    findlist=list()
    for line in listDir:
        filepath = os.path.join(path,line)
        if os.path.isfile(filepath):
               # if fnmatch.fnmatch(filepath,'*'+fileExt[0]):
                #    return filepath

                ext =  os.path.splitext(filepath)
                if ext[1] in fileExt:
                    #print filepath
                    findlist.append(filepath)
    if len(findlist) ==0:
        print("can't find rc file")

    return findlist

def main():
    if __name__ != '__main__':
            return
    #����ָ��Ŀ¼�µ� *.dll *.exe *.plug


    print find_One_RcFile()
main()