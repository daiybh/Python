# -*- coding: cp936 -*-

strHead='<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\
<gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1" creator="Oregon 400t" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd">\
  <metadata>\
    <link href="http://www.garmin.com">\
      <text>Garmin International</text>\
    </link>\
    <time>2009-10-17T22:58:43Z</time>\
  </metadata>\
  <trk>\
    <name>Example GPX Document</name>\
    <trkseg>'
strEnd=' </trkseg>  </trk></gpx>'
latPath="d:\\lat.txt"

fR = open(latPath,'r')

gpxPath="d:\\gpxpath.gpx"
fW = open(gpxPath,'w')

fW.write(strHead)
fW1 = open("d:\\cc.txt",'w')

s='   as asdas \r\nasda'
print ''.join(s.split())
for line in fR:

    if len(line)<3:
        continue
    lv = line.split("GpsServerAdmin    ")
    #print line
    
    if len(lv)==2:
        #lC = ''.join(lv[1].split())
        #lat=lC.split(',')
        lat =lv[1].split(',')
        #print "sim:",lat[0],"time:",lat[1],"lat:",lat[2],"lng:",lat[3]
        #print "sim:",lat[0],"time:",lat[1],"lat:",lat[2],"lng:",lat[3]
        strR ="%s,%s,%s,%s\r\n"%(lat[0],lat[1],lat[2],lat[3])
        print strR
        fW1.write(strR)
        strR='<trkpt lat="'+lat[2]+'" lon="'+lat[3]+'"><ele>4.46</ele> <time>'+lat[1].replace(' ','T')+'Z</time>   </trkpt>'
        #print strR
        fW.write(strR)

fW.write(strEnd)
    
