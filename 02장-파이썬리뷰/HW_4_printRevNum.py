
def printNum(n):
    if(n != 1) : 
        printNum(n-1) 
    print("%d" % n, end=' ')

def printRevNum(n) :
    if(n != 0) :
        print("%d" % n, end=' ')
        printRevNum(n-1)


num = eval(input("n = "))

printNum(num)
print()

printRevNum(num)
print()