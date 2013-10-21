import sys
import hello
def readfile(filename):
    f = file(filename)
    f.close()
def uu():
    if len(sys.argv) <2:
        print 'no action specified'
        sys.exit()
    bCommit=False
    for i in range(1,len(sys.argv)):
        if sys.argv[i].startswith('-') :
            option = sys.argv[i][1:]
            #print(option)
            if option=="ci" :
                bCommit=True
            elif option=="f":
                print(sys.argv[i+1])

    print(i)

hello.Hello()
