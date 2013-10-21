# -*- coding: utf-8 -*-
import sys,os
import re
SECTCRE = re.compile(
        r'\['                                 # [
        r'(?P<header>[^]]+)'                  # very permissive!
        r'\]'                                 # ]
        )
OPTCRE = re.compile(
	r'(?P<option>[^:=\s][^:=]*)'          # very permissive!
	r'\s*(?P<vi>[:=])\s*'                 # any number of space/tab,
					      # followed by separator
					      # (either : or =), followed
					      # by any # space/tab
	r'(?P<value>.*)$'                     # everything up to eol
	)
def splitStr(line):
	dic = dict()
	ar = line.split(';')
	#print len(ar)
	if len(ar)>1:
		value = ar[1]
	else:
		value =""
	dic[ar[0]]=value
	return dic
#大概好像
def getContent(fn):
	f = open(fn)
	#text = f.read()
	#lines = text.splitlines()

	#for line in lines:
	
	dicMain = dict()
	lineno =0
	sections = dict()
	sections.clear()
	cursect = None
	optname = None
	while True:
		line = f.readline()
		if not line:
			break
		lineno = lineno+1

		if line.strip() =='' or line[0] in '#;':
			continue
		mo = SECTCRE.match(line)
		if mo:
			sectname = mo.group('header')
			#print "["+sectname+"]"
			if sectname in sections:
				cursect = sections[sectname]
			else:
				cursect = dict()
				cursect['__name__'] = sectname
				sections[sectname] = cursect
			optname = None
		else:
			mo = OPTCRE.match(line)
			#print str(lineno)+" "+line
			if mo:
				#find option vi value
				#value maybe had remstring
				optname, vi, optval = mo.group('option', 'vi', 'value')
				rem=None
				if ";" in optval:
					pos = optval.find(';')
					if pos!=-1 and optval[pos-1].isspace():
						rem = optval[pos+1:]
						optval = optval[:pos].strip()
#				print optname+"		"+vi+"  "+optval+"  "+rem
				#print rem
				#cursect[optname] = (optval,rem)
				sectname = cursect['__name__']
				dicMain[sectname+"."+optname]={"optname":optname,
							       "value":optval.strip(),
							       "rem":rem}
	

	f.close()
	return dicMain

#getContent("mgcapturecfg.ini")
dicMain =getContent("CDD_BCSDK.INI")
	
for s in dicMain:
	dic = dicMain.get(s)
	print s+" "+ dic["optname"]+" "+ dic["value"]+" "+ dic["rem"]
