import time,datetime
import threading

def worker(a_tid,a_account):
    global g_mutex
    print "str ",a_tid,datetime.datetime.now(),"\r\n"
    for i in range(1000000):
        g_mutex.acquire()
        a_account.deposite(1)
        g_mutex.release()
    print "End ",a_tid,datetime.datetime.now(),"\r\n"


class Account:
    def __init__(self,a_base):
        self.m_amount=a_base
    def deposite(self,a_amount):
        self.m_amount+=a_amount;
    def withdraw(self,a_amount):
        self.m_amount -= a_amount

global g_mutex
count = 0
dstart = datetime.datetime.now()
print "Main thread Start At: ",dstart

thread_pool =[]
g_mutex = threading.Lock()
acc = Account(100)
for i in range(10):
    th = threading.Thread(target=worker,args=(i,acc))
    thread_pool.append(th)

for i in range(10):
    thread_pool[i].start()

for i in range(10):
    threading.Thread.join(thread_pool[i])

dend =  datetime.datetime.now()

print "count= ",acc.m_amount
print "main thread end at:",dend,"time span ",dend-dstart
        
