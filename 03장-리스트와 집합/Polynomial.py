# 클래스 선언하기
class Polynomial:   # 클래스 선언

    def __init__(self): # 생성자
        self.coef=[]    # 리스트를 생성

    # 차수는 리스트 길이 - 1과 같다. (상수항을 제외)
    def degree(self) :  
        deg = len(self.coef) - 1 # len()함수로 리스트의 항의 갯수를 반환한다.
        return deg 

    # msg의 default 값을 "f(x) = "으로 주고 마지막 항이 아니라면 x의 차수와 계수를 입력하고 마지막 항이라면 상수만 print한다.
    def display(self, msg="f(x) = "):
        for i in range((self.degree()+1),0,-1): # 차수+1부터 0까지 1씩 빼주면서 반복.
            if i != 1 : # 차수가 마지막 항이 아니라면
                if(i == (self.degree()+1)): print(msg, end ='') # 첫 항이라면 msg와 함께 출력
                print(str(self.coef[i-1]) + "x^%d" % (i-1) , end = " + ")   # 리시트의 인덱스로 해당 차수와 계수를 출력
            else:   # 차수가 마지막 항이라면
                print(str(self.coef[i-1])) # 상수항만 출력
    
    # 다항식의 길이를 비교하여 더 차수가 작은 다항식의 항의 갯수만큼 반복하며 해당 인덱스의 값들을 더 해준다.
    def add(self, b):
        add_poly = Polynomial()  # 덧셈이 된 계수를 저장할 클래스
        if len(self.coef) > len(b.coef):     # 다항식의 길이를 비교하고 길이가 더 긴 list를 add_poly.coef의 다항식에 깊은 복사를 통해 복사한다.
            add_poly.coef = list(self.coef)
        else :
            add_poly.coef = list(b.coef)
        min_list = min(len(self.coef),len(b.coef)) # 두 리스트의 길이를 비교해서 더 크기가 작은 리스트의 길이를 반환
        for i in range(min_list): # 더 크기가 작은 리스트의 항의 갯수만큼 반복하며 인덱스에 접근한다.
            add_poly.coef[i] = (self.coef[i]+b.coef[i]) # 해당 계수를 더하고 덧셈된 값을 add_poly리스트에 추가한다.
        return(add_poly) # add_poly클래스를 반환한다.
        
    # x의 scar값을 대입하여 다항식을 계산
    def eval(self, x):
        value = 0   # 리스트의 인덱스 값들에 scar을 곱하여 더할 변수 value
        for i in range(len(self.coef)):
            value += self.coef[i] * (x**i) # 모든 값을 더하여 value에 반환
        return value
    
    # 다항식 리시트의 모든 계수에 -1을 곱할 함수
    def neg(self, b):
        neg_poly = Polynomial()
        neg_poly.coef = list(b.coef) # 깊은 복사를 통해 b.coef는 변하지 않고 새로운 리스트로 복사하여 변환
        for i in range(len(neg_poly.coef)) :
            neg_poly.coef[i] *= -1
        return neg_poly

    # 다항식의 뺄셈을 나타내는 함수
    def sub(self, b):
        return self.add(self.neg(b))

    # 다항식의 곱셈을 나타내는 함수
    def multiply(self, b):
        mul_poly = Polynomial()
        self_degree = len(self.coef) - 1; b_degree = len(b.coef) - 1 # degree 함수의 값을 받아오는 과정에서 오류가 생겨 새로 차수 값 설정
        mul_try = self_degree + b_degree
        
        # 다항식의 곱셈 결과 값을 저장할 리스트의 메모리 할당
        for n in range(mul_try + 1):
            mul_poly.coef.append(0)
        # 다항식의 곱셈 알고리즘
        for i in range(self_degree+1):
            for j in range(b_degree+1):
                mul_poly.coef[i+j] += b.coef[j] * a.coef[i]
        return mul_poly

    # 다항식을 입력받고 리스트에 저장하는 함수
    def read(self):
        self.coef = input("다항식을 입력하시오: ").split(' ')
        for n in range(self.degree()+1):
            self.coef[n] = float(self.coef[n])
        self.coef.reverse()

#======================================================================================================================================
# 객체 생성
a = Polynomial()
b = Polynomial()

# 다항식 입력
a.read()
b.read()

# 입력받은 다항식 출력
print('A : ', end = ''); a.display()
print('B : ', end = ''); b.display()

# A + B = C
c = a.add(b)
print('A + B : ', end= ''); c.display()

# C(2)
print("C(2) = ", c.eval(2))

# A - B = D
d = a.sub(b)
print('A - B : ', end = ''); d.display()

# A * B = E
e = a.multiply(b)
print('A * B : ',end =''); e.display()