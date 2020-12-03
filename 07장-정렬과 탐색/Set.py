# Set 집합 클래스
class Set:
    def __init__(self):                                         # 생성자
        self.items = []                                         # 집합의 원소들을 저장하기 위한 빈 리스트 생성
    
    def size(self):                                             # 집합의 항의 갯수를 반환하는 메소드
        return len(self.items)
    
    def contains(self, item):                                   # 해당 원소가 리스트내에 존재하는지 여부 확인 메소드
        return item in self.items
    
    def insert(self, elem):                                     # 정렬된 리스트를 구현하기위한 원소 삽입 연산
        if elem in self.items : return                          # 집합 리스트에 존재하는 원소라면 insert 하지 않는다.
        for idx in range(len(self.items)):                      # 모든 인덱스에 대해서
            if elem < self.items[idx]:                          # 입력받은 원소가 해당 인덱스보다 작다면
                self.items.insert(idx, elem)                    # 리스트의 해당 인덱스에 값을 insert한다.
                return                                          # 이후 함수를 종료한다.
        self.items.append(elem)                                 # 가장 큰 원소라면 맨 뒤에 append한다.

    def delete(self,elem):                                      # 정렬된 리스트를 제거하는 메소드
        self.items.remove(elem)
    
    def __eq__(self, setB):                                     # 두 집합이 같은지 확인하는 메소드
        if self.size() != setB.size():                          # 두 집합의 크기가 다르다면 같지 않다.
            return False
        for idx in range(len(self.items)):                      # 모든 인덱스에 대해서
            if self.items[idx] != setB.items[idx]:              # 같은 인덱스에 대해서 값이 같지 않다면
                return False                                    # False를 반환
        return True                                             # 같다면 True를 반환
    
    def union(self, setB):                                      # 합집합 메소드
        unionSet = Set()                                        # 합집합을 저장할 집합 객체 생성
        a = 0 ; b = 0                                            
        while (a < len(self.items)) and (b < len(setB.items)):  # A와 B 집합의 모든 인덱스에 대해서
            valueA = self.items[a]; valueB = setB.items[b]      # 값 비교를 편리하게 하기위한 변수
            if valueA < valueB :                                # A의 값이 더 작다면
                unionSet.items.append(valueA)                   # 합집합에 A의 값을 append
                a+=1                                            # a의 다음 인덱스
            elif valueA > valueB :                              # A의 값이 더 크다면
                unionSet.items.append(valueB)                   # 합집합에 B의 값을 append
                b+=1                                            # B의 다음 인덱스
            elif valueA == valueB:                              # A와 B의 값이 같다면
                unionSet.items.append(valueA)                   # A혹은 B의 값 아무거나 선택하여 append
                a+=1; b+=1                                      # A와 B의 다음 인덱스
        while a < len(self.items):                              # A의 남은 모든 요소들을 합집합에 추가한다.
            unionSet.items.append(self.items[a])
            a+=1
        while b < len(setB.items):                              # B의 남은 모든 요소들을 합집합에 추가한다.
            unionSet.items.append(self.items[b])
            b+=1
        return unionSet
    
    # P7_3
    def intersect(self,setB):                                   # 교집합 메소드
        intersectSet = Set()                                    # 교집합을 저장할 집합 객체
        a=0;b=0
        while a < len(self.items) and b < len(setB.items):      # A와 B집합 모든 인덱스에 대해서
            valueA = self.items[a]; valueB = setB.items[b]      # 리스트의 요소들을 변수에 저장해 비교하기 편리하게 한다.
            if valueA < valueB : a+=1                           # 만약 A집합의 값이 더 작으면 A의 다음 인덱스
            elif valueA > valueB : b+=1                         # 만약 A집합의 값이 더 크다면 B의 다음 인덱스
            else:                                               # A집합의 값과 B 집합의 값이 같다면 교집합 리스트에 append한다.
                intersectSet.items.append(valueA)
                a+=1; b+=1
        return intersectSet

    # P7_4
    def difference(self,setB):                                  # 차집합 메소드
        differenceSet = Set()                                   # 차집합을 저장할 집합 객체
        differenceSet.items = self.items[:]                     # A의 집합의 값을 차집합에 슬라이싱 연산을 통한 얕은 복사 시행
        a=0; b=0
        while a < len(differenceSet.items) and b < len(setB.items): # 차집합 집합과 B 집합의 모든 인덱스에 대해서
            valueA = differenceSet.items[a] ; valueB = setB.items[b]# 리스트의 요소들을 변수에 저장해 비교하기 편리하게 한다.
            if valueA < valueB : a+=1                           # 차집합의 값이 더 작다면 차집합의 다음 인덱스
            elif valueA > valueB : b+=1                         # 차집합의 값이 더 크다면 B집합의 다음 인덱스
            else:                                               # 차집합의 값과 B집합의 값이 같다면 차집합의 원소를 삭제
                differenceSet.delete(valueA)
                a+=1; b+=1
        return differenceSet

    def display(self, msg):                                     # 리스트를 display하는 메소드
        print(msg, self.items)

# ==========================================================================

# 집합 A 생성 및 원소 추가
setA = Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('Set A : ')

# 집합 B 생성 및 원소 추가
setB = Set()
setB.insert('빗')
setB.insert('파이썬 자료구조')
setB.insert('야구공')
setB.insert('지갑')
setA.display('Set A : ')
setB.display('Set B : ')

# 집합의 원소 추가 및 삭제s
setB.insert('빗')
setA.delete('손수건')

# 현재 집합 값 출력
setA.display('Set A : ')
setB.display('Set B : ')

# A 와 B 집합의 합집합, 교집합, 차집합 연산
setA.union(setB).display('A U B : ')
setA.intersect(setB).display('A ^ B : ')
setA.difference(setB).display('A - B : ')