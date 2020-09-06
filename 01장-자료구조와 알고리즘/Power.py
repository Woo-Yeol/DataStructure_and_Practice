import time

def power(x,n) :
    if n ==0 : return 1
    elif (n%2) == 0 :   # n이 짝수
        return power(x*x, n // 2)
    else :              # n이 홀수
        return x*power(x*x, (n-1)//2)

def slow_power(x,n):    # O(n)
    result = 1.0
    for i in range(n):
        result = result * x
    return result

def testPower():
    print("Fast Power(2,500)..." + str(power(2.0, 500)))
    print("Slow Power(2,500)..." + str(slow_power(2.0, 500)))

    t1 = time.time()
    for i in range(100000) :
        power(2.0, 500)
    t2 = time.time()
    print("Fast Power... "+ str(t2-t1))

    t1 = time.time()
    for i in range(100000) :
        slow_power(2.0, 500)
    t2 = time.time()
    print("Slow Power... " + str(t2-t1))

testPower()
