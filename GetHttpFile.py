import httplib
#http://photography.nationalgeographic.com/photography/photo-of-the-day

def GetFile(host,url):
    conn = httplib.HTTPConnection(host)
    conn.request("GET", url)
   # conn.request('GET', url, headers = {"Host": host,
   #                                 "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
   #                                 "Accept": "text/plain"})
    r1 = conn.getresponse()
    print r1.status, r1.reason

    data1 = r1.read()
    print data1
    conn.close()
    return data1

webContent =GetFile("www.google.com.hk","/")
webContent =GetFile("photography.nationalgeographic.com","/photography/photo-of-the-day/")

print webContent.find("primary_photo")