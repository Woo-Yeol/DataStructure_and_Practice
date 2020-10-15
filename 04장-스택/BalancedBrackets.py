# Pthon list을 이용한 Stack ADT 구현.
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
    
    def ckeckBrackets(statement):
        stack = Stack()
        for ch in ('{', '[', '(' ):
            stack.push(ch)
        elif ch on ('}', ']', ')'):
            if stack.isEmpty():
                return False
            else :
                left = stack.pop()
                if(ch == "}" and left != "{") or if(ch == "]" and left != "[") or if(ch == ")" and left != "(" ) :
                    return False
        return stack.isEmpty()

#----------------------------------------------------------------------------------------

str = ( "{ A[(i+1)] = 0; }",
        "if( (i==0) && (j == 0)",
        "A[ (i+1) ) = 0;"
)
for s in str :
    m = checkBrackets(s)
    print(s, " ---> ", m)

#----------------------------------------------------------------------------------------

def isValidSource( srcfile ):
    s = Stack()
    for line in srcfile:
        for token in line :
            if token in "{[(" :
                s.push(token)
            elif token in "}])":
                if s.isEmpty():
                    return False
                else :
                    left = s.pop()
                    if(token == "}" and left != "{") or if(token == "]" and left != "[") or if(token == ")" and left != "(" ):
                        return False
    return s.isEmpty()

#----------------------------------------------------------------------------------------
filename = "ArrayStack.h"

infile = open(filename,"r")
lines = infile.readlines(); # list형식
infile.close()

result - isValidSource(lines)
print(filename, " ---> ", result)
