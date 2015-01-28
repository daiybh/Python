class Human:

    def __init__(self):
        self.__name =""
        self.__sex =""
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def setSex(self,sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex
    name = property(getName,setName)
    sex = property(getSex,setSex)

lilei = Human()
lilei.name="lilei"
lilei.sex="man"
print "%s %s out"%(lilei.name,lilei.sex)

def doPee(self,how):
    print "[%s] [%s] [%s] pee"%(self.name,self.sex,how)

Human.doPee = doPee

lilei.doPee("stand up")
