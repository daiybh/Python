# -*- coding: cp936 -*-
import urllib2
import urllib
import os
basePath = "e:/meon/"
#os.mkdir(basePath)
def image_down(image):
      #urllib.urlretrieve(image,image.split('/')[-1]
      arr = image.split('/')
      filename=arr[len(arr)-1]
                        
      try:
            urlopen=urllib.URLopener()
            fp = urlopen.open(image)
            data = fp.read()
            fp.close()
            file1 = open(basePath+filename,'w+b')
            file1.write(data)
            file1.close()
      except IOError:
            #print "download Error"+image
            i=0

path="http://www.manbolo.com/img/meon-level-80-83.png"
baseurl="http://www.manbolo.com/img/meon-level-"
'''0---120
每4关一个图片
0 1 2 3
4 5 6 7
8 9 10 11
12 13 14 15
16 17 18 19
'''
for i in range(0,120,4):
      iend=i+3
      imageurl=baseurl+str(i)+"-"+str(iend)+".png"
      if i>119:
            imageurl=baseurl+str(i)+".png"
      print i,imageurl
      
      image_down(imageurl)
