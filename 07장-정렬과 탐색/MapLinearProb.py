# LinearProbMap
# map은 entry의 집합
class Entry:                                        # Entry class 및 연산자 중복 함수
    def __init__(self, key, value):                 # 생성자
        self.key = key
        self.value = value
    
    def __str__(self):                              # 객체를 필요시 문장열로 변환한다.
        return str("%s:%s"%(self.key, self.value))

class LinearProbMap:                                # 선형조사법 class
    def __init__(self, M):                          # 생성자
        self.table = [None] * M                     # table에 입력받은 크기를 곱하여 table의 크기 선언
        self.M = M                                  # 입력받은 테이블의 크기
    
    def hashFn(self,key):                           # 해싱 함수
        sum = 0
        for c in key :                              # key의 문자 코드들을 값을 더한다.
            sum = sum + ord(c)
        return sum % self.M                         # 더한 결과 값을 테이블의 크기로 나눈 나머지 값을 반환한다.

    def insert(self, key, value):                   # 삽입 연산
        idx = self.hashFn(key)                      # 해싱 메소드로 주소값을 구한다.
        while (self.table[idx] != None) and (self.table[idx] != False):              # 해당 주소의 Table값이 None값 혹은 False값이 아니라면
            idx = (idx + 1) % 13                    # 옆의 주소 값으로 이동한다. (끝까지 도달하면 맨 앞으로 이동한다.)
        self.table[idx] = Entry(key,value)          # table에 Entry 객체를 저장한다.    

    def search(self, key):                          # 탐색 연산
        cnt = 0
        idx = self.hashFn(key)                      # 해싱 메소드로 주소값을 구한다.
        while (self.table[idx] != None):            # 해당 주소의 Table의 값이 None값이 아닌 경우만 탐색
            if str(type(self.table[idx])) != "<class 'bool'>":  # False의 값일 경우가 있어 key 값이 존재하지 않을 수 있으므로 자료형을 검사하여 False가 입력받으면 다음 인덱스로 이동한다.
                if self.table[idx].key == key:      # 해당 주소의 값의 Key 값이 주어진 값과 같은지 검사한다.
                    return self.table[idx]          # 같다면 해당 테이블 반환
                else:
                    idx = (idx + 1) % self.M            # 다르다면 다음 주소를 검사
            else:
                idx = (idx + 1) % self.M            # 다르다면 다음 주소를 검사
            cnt += 1                                # 반복문이 시행한 횟수를 cnt에 계산
            if cnt == self.M: break                 # 테이블의 크기만큼 반복을 시행했을 때 탐색이 끝나지 않았다면 탐색 실패
        return None                                 # 탐색에 실패하면 None

    def delete(self, key):                          # 삭제 연산
        cnt = 0
        idx = self.hashFn(key)                      # 해싱 메소드로 주소값을 구한다.
        while (self.table[idx] != None) and (self.table[idx] != False) :              # 해당 주소의 Table의 값이 None값 혹은 False값이 아니라면
            if self.table[idx].key == key:          # 해당 주소의 값의 key 값이 같다면
                self.table[idx] = False  # 해당 주소의 값을 Entry값에 key, value값을 False를 준다.
            else:                                   # 아니라면 다음 주소를 검사
                idx = (idx + 1) % self.M
            cnt += 1
            if cnt == self.M:                       # Table의 크기만큼 검사해도 없을 경우 break
                break

    def display(self, msg):                         # map을 출력하는 메소드
        print(msg)
        for idx in range(len(self.table)):          # 모든 Table 값을 확인하여
            table = self.table[idx]                 # 검사를 위한 변수 저장
            if (table != None) and (table != False):                   # 만약 None값 혹은 False값이 아니라면 출력
                print("[%2d] -> " %idx, self.table[idx])

# =============================================================
map = LinearProbMap(13)
map.insert('data', '자료')
map.insert('structure', '구조')
map.insert('sequential search', '선형 탐섹')
map.insert('game', '게임')
map.insert('binary search', '이진 탐색')
map.display("나의 단어장 : ")

print(" 탐색:game - - > ", map.search('game'))
print(" 탐색:over - - > ", map.search('over'))
print(" 탐색:data - - > ", map.search('data'))

map.delete('game')
map.display("나의 단어장: ")
print(" 탐색:game - - > ", map.search('game'))
