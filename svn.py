# -*- coding: cp936 -*-
import os
'''读取
'''
svnCmd = "svn info"
svnRet = os.popen(svnCmd).readlines()
print(svnRet)
