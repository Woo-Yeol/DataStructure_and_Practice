#Fibonacci (순환)
def fib(n) :
    if n == 0 : return 0
    elif n == 1 : return 1
    else :
        return fib(n - 1) + fib(n - 2)

# Fibonacci (반복)
def fib_iter(n) :
    if (n < 2): return n
    last = 0
    current = 1
    for i in range(2, n+1):
        tmp = current
        current += last
        last = tmp
    return current

import time

print('Fibonacci_반복_(5) = ', str(fib_iter(5)))
print('Fibonacci_순환_(5) = ', str(fib(5)))

for i in range (1, 40):
    # 피보나치_반복 함수의 시작 시간과 종료 시간
    start_iter = time.time()
    fib_iter(i)
    end_iter = time.time()

    # 피보나치_순환 함수의 시작 시간과 종료 시간
    start = time.time()
    fib(i)
    end = time.time()

    # n번째 / 피보나치_반복 함수의 처리시간 계산 / 피보나치_순환의 처리시간 계산
    print('n= ', i, '반복: ', int(end_iter-start_iter)*10 / 10, '순환: ', end-start)
    # 피보나치 함수의 값 반환
    print('fib_iter: ', fib_iter(i), 'fib: ', fib(i))