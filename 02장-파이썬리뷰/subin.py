temp = 0
tax = 0
print("소득: {} ".format(income), end="")
print("(만)원")
income = float(input("소득을 입력해주세요: ")
    
if (income <= 1200) :
    tax = income * 0.06
    temp += tax
    
else:
    temp = (1200*0.06)

if income > 1200 and income <=4600:
    tax = (income-1200)*0.15
    temp += tax 
else:
    temp += (4600*0.15) 
    # temp += (4600 - 1200) * 0.15
    # 이하의 내용도 동일하게 소득세율이 적용된 값들에 다른 소득세율이 중복이 됨.

if income > 4600 and income <= 8800:
    tax = (income-4600)*0.24
    temp += tax
else:
    temp += (8800*0.24)
    
if income >8800 and income <= 15000:
    tax = (income-8800)*0.35
    temp += tax
else:
    temp += (15000*0.35)
    
if income > 15000:
    tax = (income-15000)*0.38
    temp += tax

    print("세금:", temp, end="")
    print("(만)원")
    print("순수소득:", income-temp, end="")
    print("(만)원")

print("세금:", temp, end="")
print("(만)원")
#print("순수소득:", income-temp, end="")
print("(만)원")