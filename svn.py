# -*- coding: cp936 -*-
import os
'''��ȡ
'''
svnCmd = "svn info"
svnRet = os.popen(svnCmd).readlines()
print(svnRet)
