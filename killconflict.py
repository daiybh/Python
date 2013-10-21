#-------------------------------------------------------------------------------
# Name:        Killconflict
# Purpose:     解决快盘同步目录中出现冲突的情况，产生冲突文件后执行此脚本，则比
#              较冲突文件与同名的其他对应文件，保留其中最新修改的，并删掉其他
# Author:      mumoo
# Created:     29/01/2011
# Rev:         0.1
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import os
import sys

def main():
    #处理此脚本所在的目录和他的子目录
    findf(os.path.split(sys.argv[0])[0])

def findf(target):
    """target为要操作的目录

    此函数遍历该目录下的文件,并操作文件名中包含特定字符的文件
    """
    for name in os.listdir(target):
        aname=os.path.join(target,name)
        if os.path.isfile(aname):
            print(aname)
            if '(冲突' in name:
                print(name)
                try:
                    nametocompare=name[:name.find('(冲突')]+\
                        name[name.rindex('.'):]
                    anametocompare=os.path.join(target,nametocompare)
                except ValueError:
                    nametocompare=name[:name.find('(冲突')]
                    anametocompare=os.path.join(target,nametocompare)
                comparef_delete_later(aname,anametocompare)
        else:
            findf(aname)

def comparef_delete_later(f1,f2):
    """比较两个文件修改时间的不同,两个参数f1和f2分别为两个文件的名(含路径)

    比较后保留较新修改的文件(如f1),删掉较早的(如f2),并将f1名字改为f2
    """
    if (False==os.path.exists(f1)) or (False ==os.path.exists(f2)):
        return
    if os.stat(f1).st_mtime>os.stat(f2).st_mtime:
        os.remove(f2)
        os.rename(f1,f2)
    else:
        os.remove(f1)

if __name__ == '__main__':
    main()
