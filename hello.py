
class TestFun():


	def __init__(self):
		self._common_handlers = None
		self.Fun()
	def Fun(self):
		comman_handers={}
		comman_handers["INIT"]=self._On_Init
		comman_handers["CLOSE"]=self._On_Close
		self._common_handlers = comman_handers



	def _On_Close(self,msg):
		print "On_CLose"

	def _On_Init(self,msg):
		print "OnInit"

	def Process(self,msg):
		handler = self._common_handlers.get(msg.command,None)
		if handler:
			handler(msg)

class MSG():
	def __init__(self):
		self.command=None
	def SetCmd(self,cmd):
		self.command = cmd
cc = TestFun()
msg = MSG()
msg.command = "INIT"
cc.Process(msg)
