tax = 0;    # 연산을 위한 tax 변수 초기화 및 정의
income_temp = 0;    # 연산을 위한 income_temp 변수 초기화 및 정의
income = eval(input("소득을 입력하세요 (만원) : "))
memory_income = income  # 연산을 위한 소득액을 변경하는 변수

if income > 15000 : # 소득이 1억 5000만원 초과일 경우
    income_temp = income - 15000 # 초과되는 금액을 계산하여
    tax += income_temp*0.38 # 소득세율에 해당되는 금액을 tax 변수에 저장
    income -= income_temp   # 이후 소득에서 소득세율이 적용된 범위의 금액을 제외한다.

if (income <= 15000) and (income > 8800) :
    income_temp = income - 8800
    tax += income_temp*0.35
    income -= income_temp

if (income <= 8800) and (income > 4600) :
    income_temp = income - 4600
    tax += income_temp*0.24
    income -= income_temp

if (income <= 4600) and (income > 1200) :
    income_temp = income - 1200
    tax += income_temp*0.15
    income -= income_temp

if (income <= 1200):
    tax += income*0.06

print(" 전체세금 = ",tax,"만원")
print(" 순수소득 = ",memory_income - tax,"만원")