import datetime
import time as _time

tStart = datetime.datetime.today()
tStart = tStart.replace(hour=9,minute=0,second=0)
def DoWork():
	xx= datetime.datetime.now()-tStart
	print xx

DoWork()