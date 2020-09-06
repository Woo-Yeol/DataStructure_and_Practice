import random
import time

def find_max( A ):
    max = A[0]
    for item in A :
        if item > max :
            max = item
    return max

start = time.time()

for n in range(100) :
    #
    array = [random.randint(0 , 10000) for i in range(10000)]
    print(find_max(array), end =" ")
print()

end = time.time()
print("실행시간 = ", end-start)
