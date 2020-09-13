# random module을 import해서 사용한다.
import random
min, max = 0, 99
# Random module의 randrange()함수를 사용하여 min~max의 임의의 숫자를 답으로 입력한다.
answer = random.randint(min,max)
# answer = random.randrange(min, max)

# try_n는 1부터 10까지 1씩 증가하며 반복한다.
for try_n in range(1,10,1) :
    guess = eval(input("숫자를 입력하세요(범위 :  %d~%d) : " % (min,max)))
    if answer == guess :
         print("정답입니다. %d번 만에 맞추셨습니다." % try_n)
         break;
    elif answer > guess :
        print("아닙니다. 더 큰 숫자입니다.")
        min = guess
    else :
        print("아닙니다. 더 작은 숫자입니다.")
        max = guess
print("게임이 끝났습니다.")