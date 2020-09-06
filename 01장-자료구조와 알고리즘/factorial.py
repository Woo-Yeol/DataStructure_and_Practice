# 순환 구조로 구현한 Factorial 함수
def factorial(n) :
    if n == 1 : return 1
    else : return n * factorial(n-1)

# 반복 구조로 구현한 Factorial 함수
def factorial_iter(n) :
    result = 1
    for k in range(n, 0, -1) :  # n이하 0 초과 -1일씩 감소
        result = result * k
    return result

print('Factorial 순환 (3) = ', str(factorial(3)))
print('Factorial 반복 (3) = ', str(factorial_iter(3)))