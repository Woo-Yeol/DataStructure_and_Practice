from math import sqrt   # dist함수를 구현하기 위한 sqrt import

MAX_QSIZE = 30  # 큐의 사이즈를 30으로 설정한다.
MAZE_SIZE = 10  # 미로의 넓이는 10 * 10으로 설정한다.

# Python list을 이용한 Stack ADT 구현.
class Stack :
    def __init__(self):                 # 생성자
        self.top = []

    def isEmpty(self):
        return len(self.top ) == 0
    
    def push(self, item) :
        self.top.append(item)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        
    def size(self):
        return len(self.top)
    
    def clear(self):
        self.top = []

# Python list를 이용한 Queue ADT 구현.
class CircularQueue:
    def __init__(self):    # 생성자
        self.front = 0     # 큐의 전단 위치
        self.rear = 0      # 큐의 후단 위치
        self.items = [None] * MAX_QSIZE
 
    def isEmpty(self) : return self.front == self.rear
    def isFull(self) : return self.front == (self.rear+1)%MAX_QSIZE
    def clear(self) : self.front = self.rear
 
    def enqueue(self, item):
        if not self.isFull():           # 원형 큐가 다 차이지 않는다면
            self.rear = (self.rear+1)%MAX_QSIZE # rear 회전
            self.items[self.rear] = item        # 해당 위치에 항목 삽입
 
    def dequeue(self):
        if not self.isEmpty():          # 원형 큐가 비어있지 않다면
            self.front = (self.front+1)%MAX_QSIZE       # front 회전
            return self.items[self.front]               # 해당 위치의 항목 반환
 
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
 
    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE
 
    def display(self):
        out = []
        if self.front < self.rear :
            out = self.items[self.front+1:self.rear+1]  # 슬라이싱
        else:
            out = self.items[self.front+1:MAX_QSIZE] \
                + self.items[0:self.rear+1]             # 슬라이싱
        print("[f = %s, r = %d] ==> "%(self.front, self.rear), out)

# Python list를 이용한 PriorityQueue ADT 구현.
class PriorityQueue():
    def __init__(self): # 생성자
        self.items = []
 
    def isEmpty(self) : return len(self.items) == 0
    def size(self): return len(self.items)
    def clear(self): self.items = []
 
    def enqueue(self, item):    # 삽입 연산
        self.items.append(item)
 
    def findMaxIndex(self):             # 최대 우선순위 항목의 인덱스 반환
        if self.isEmpty(): return None
        else:
            highest = 0                 # 0번을 최대라고 하고
            for i in range(1, self.size()): # 모든 항목에 대해서
                if self.items[i][2] > self.items[highest][2]:   # 거리를 나타내는 인덱스를 확인하여 거리를 비교한다.
                    highest = i         # 인덱스 갱신
            return highest
 
    def dequeue(self):          # 삭제 연산
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)
 
    def peek(self):             # peek 연산
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items[highest]

    def dist(self, x, y):       # 거리계산 연산
        (ox, oy) = (9,8)        # 출구 위치
        (dx, dy) = (ox - x, oy - y)
        return sqrt(dx*dx + dy*dy)

# 각각의 미로
map = [[ '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['e', '0', '0', '0', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '1', '0', '0', '1', '1', '1', '1', '1'],
        ['1', '0', '1', '1', '0', '0', '1', '1', '1', '1'],
        ['1', '0', '1', '1', '1', '0', '0', '1', '1', '1'],
        ['1', '0', '1', '1', '1', '1', '0', '0', '0', '1'],
        ['1', '0', '1', '1', '1', '1', '1', '1', '0', '1'],
        ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', 'x'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
]
q_map = [[ '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['e', '0', '0', '0', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '1', '0', '0', '1', '1', '1', '1', '1'],
        ['1', '0', '1', '1', '0', '0', '1', '1', '1', '1'],
        ['1', '0', '1', '1', '1', '0', '0', '1', '1', '1'],
        ['1', '0', '1', '1', '1', '1', '0', '0', '0', '1'],
        ['1', '0', '1', '1', '1', '1', '1', '1', '0', '1'],
        ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', 'x'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
]
pq_map = [[ '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['e', '0', '0', '0', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '1', '0', '0', '1', '1', '1', '1', '1'],
        ['1', '0', '1', '1', '0', '0', '1', '1', '1', '1'],
        ['1', '0', '1', '1', '1', '0', '0', '1', '1', '1'],
        ['1', '0', '1', '1', '1', '1', '0', '0', '0', '1'],
        ['1', '0', '1', '1', '1', '1', '1', '1', '0', '1'],
        ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', 'x'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
]

# 각자의 미로의 유효성을 검사하는 함수
def isValidPos(x,y) :                                           # (x,y)가 갈 수 있는 방인지 검사하는 함수
        if x < 0 or y <0 or x >= MAZE_SIZE or y >= MAZE_SIZE :  
                return False                                    # (x,y)가 미로 밖이면 -> 갈 수 없음을 반환
        else :
                return map[y][x] == '0' or map[y][x] == 'x'

def isValidPos_q(x,y) :                                           # (x,y)가 갈 수 있는 방인지 검사하는 함수
        if x < 0 or y <0 or x >= MAZE_SIZE or y >= MAZE_SIZE :  
                return False                                    # (x,y)가 미로 밖이면 -> 갈 수 없음을 반환
        else :
                return q_map[y][x] == '0' or q_map[y][x] == 'x'

def isValidPos_pq(x,y) :                                           # (x,y)가 갈 수 있는 방인지 검사하는 함수
        if x < 0 or y <0 or x >= MAZE_SIZE or y >= MAZE_SIZE :  
                return False                                    # (x,y)가 미로 밖이면 -> 갈 수 없음을 반환
        else :
                return pq_map[y][x] == '0' or pq_map[y][x] == 'x'


# 깊이우선탐색 함수
def DFS() :
        stack = Stack()         # 스택 객체 생성
        stack.push((0,1))       # 사용할 스택 객체를 준비
        print('DFS: ')

        while not stack.isEmpty(): # 공백이 아닐 동안
                here = stack.pop() # pop()연산으로 항목을 꺼냄
                print(here, end = ' -> ')
                (x,y) = here

                if(map[y][x] == 'x'): # 출구이면 탐색 성공. True 반환
                        return True
                else :
                        map[y][x] = '.'# 현재위치를 지나왔다고 '.'표시
                        if isValidPos(x , y-1) : stack.push((x, y-1)) # 상
                        if isValidPos(x , y+1) : stack.push((x, y+1)) # 하
                        if isValidPos(x-1 , y) : stack.push((x-1, y)) # 좌
                        if isValidPos(x+1 , y) : stack.push((x+1, y)) # 우
        return False    # 탐색 실패. False 반환

# 너비우선탐색 함수
def BFS() :
        que = CircularQueue()   # 원형 큐 객체 생성
        que.enqueue((0,1))
        print('BFS: ')

        while not que.isEmpty():
                here = que.dequeue()
                print(here, end = ' -> ')
                x,y = here

                if (q_map[y][x] == 'x') : 
                        return True
                else :
                        q_map[y][x] = '.'
                        if isValidPos_q(x , y-1) : que.enqueue((x, y-1)) # 상
                        if isValidPos_q(x , y+1) : que.enqueue((x, y+1)) # 하
                        if isValidPos_q(x-1 , y) : que.enqueue((x-1, y)) # 좌
                        if isValidPos_q(x+1 , y) : que.enqueue((x+1, y)) # 우
        return False

# 최소거리 전략의 미로탐색
def MySmartSearch() :
        prq = PriorityQueue()                   # 우선순위 큐 객체 생성
        prq.enqueue((0, 1, -prq.dist(0,1)))     # 튜플에 거리정보 추가하기
        print("Priority_Queue: ")

        while not prq.isEmpty():
                here = prq.dequeue()
                print(here[0:2], end=' -> ')    # (x,y,-d)에서 (x,y)만 출력
                x,y,_ = here                    # (x,y,-d)에서 (x,y,_)
                if(pq_map[y][x] == 'x') : return True
                else :
                        pq_map[y][x] = '.'
                        if isValidPos_pq(x, y-1) : prq.enqueue((x,y-1, -prq.dist(x,y-1)))
                        if isValidPos_pq(x, y+1) : prq.enqueue((x,y+1, -prq.dist(x,y+1)))
                        if isValidPos_pq(x-1, y) : prq.enqueue((x-1,y, -prq.dist(x-1,y)))
                        if isValidPos_pq(x+1, y) : prq.enqueue((x+1,y, -prq.dist(x+1,y)))
                print('우선순위큐: ',prq.items)
        return False
    
if __name__ == "__main__":
# 깊이우선탐색
        result = DFS()
        if result : print(' ---> 미로탐색 성공')
        else : print(' ---> 미로탐색 실패')

# 너비우선탐색
        result_que =BFS()
        if result_que : print(' ---> 미로탐색 성공')
        else : print(' ---> 미로탐색 실패')

# 최소거리 전략의 미로탐색
        result_pque = MySmartSearch()
        if result_pque : print(' ---> 미로탐색 성공')
        else : print(' ---> 미로탐색 실패')