# Bag.

def contains(bag, e) :
    return e in bag  # True /False

def insert(bag, e) :
    bag.append(e)

def remove(bag,e) :
    bag.remove(e)

def count(bag):
    return len(bag)

def numOf(bag, item):
# bag 리스트에 특정 구분자를 추가하여 문자열로 변환하기    
    item_name = ','.join(bag)
# count() 함수를 사용하여 문자열의 item의 수 반환
    return item_name.count(item)    

#=================================================
myBag = [] # 데이터

insert(myBag, '휴대폰'); insert(myBag, '지갑')
insert(myBag, '아이패드'); insert(myBag, '에어팟')
insert(myBag, '립밤'); insert(myBag, '맥북')
insert(myBag, '신분증'); insert(myBag, '사자')
print('내 가방속의 물건:', myBag)
 
insert(myBag, '수표'); insert(myBag, '사자')
remove(myBag, '지갑')
print('내 가방속의 물건: ', myBag)
print('사자의 개수: ', numOf(myBag, '사자'))