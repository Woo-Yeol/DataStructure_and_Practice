# Python list을 이용한 Stack ADT 구현.
class Stack :
    def __init__(self):
        self._Items = list()

    def isEmpty(self):
        return len(self._Items ) == 0
    
    def push(self, item) :
        self._Items.append(item)

    def peek(self):
        if not self.isEmpty():
            return self._Items[-1]
    
    def pop(self):
        if not self.isEmpty():
            return self._Items.pop()

#----------------------------------------------------------------------------------------

# 파일 내의 유효성 검사 함수
def isValidSource( srcfile ):
    s = Stack()
    lcnt = 0
    ccnt = 0
    for line in srcfile: # srcfile의 리스트 형식에서 문자열을 하나하나 검사한다.
        lcnt += 1 # 라인 수 세기
        for token in line : # 리스트의 문자열에서 하나의 문자를 검사한다.
            ccnt += 1 # 문자 수 세기
            if token in "{[(" : # 그 문자가 {,[,(중에 하나라면 s 객체의 리스트에 추가한다. (스택에 값을 추가한다.)
                s.push(token)  
            elif token in "}])": # 그 문자가 ),],}중에 하나일때 스택이 비어있다면 오류 코드 2와 현재 위치의 라인, 문자 수를 반환한다., 비어있지 않다면 스택의 내용물을 검사한다.
                if s.isEmpty():
                    return 2, lcnt, ccnt
                else :
                    left = s.pop() # 검사한 값이 각각의 괄호에 대응하지 않는다면 오류 코드 3과 현재 위치의 라인, 문자 수를 반환한다.
                    if (token == "}" and left != "{") or \
                       (token == "]" and left != "[") or \
                       (token == ")" and left != "(" ):
                       return 3, lcnt, ccnt
    if not s.isEmpty():
        return 1, lcnt, ccnt # 검사가 끝났는데 비어있지 않다면 오류 코드 1과 현재 위치의 라인, 문자 수를 반환한다.
    return 0, lcnt, ccnt

#----------------------------------------------------------------------------------------
# filename = "ArrayStack.h"
filename = "CheckBracketMain.cpp"

# file을 읽어서 readlines()로 문자열을 list형식으로 저장
infile = open(filename,"r")
lines = infile.readlines(); # list형식
infile.close() # 파일 닫기

eCode, lcnt, ccnt = isValidSource(lines)
print(filename, " ---> ", eCode)
print(" 라인 수 = " , lcnt)
print(" 문자 수 = ", ccnt)
