# Python list를 이용한 Queue ADT 구현.
MAX_QSIZE = 30  # 큐의 사이즈를 30으로 설정한다.
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

# 이진트리를 위한 노드 클래스
class TNode:                                  
                                                # 생성자
    def __init__(self, data, left=None, right=None):      
        self.data = data                        # 노드의 데이터
        self.left = left                        # 왼쪽 자식 링크
        self.right = right                      # 오른쪽 자식 링크

def preorder(n):                                # 전위 순회(VLR)
    if n is not None:
        print(n.data, end=" ")                  # 먼저 루트노드 처리(화면 출력)
        preorder(n.left)                        # 왼쪽 서브트리 처리
        preorder(n.right)                       # 오른쪽 서브트리 처리

def inorder(n):                                 # 중위 순회 함수
    if n is not None:
        inorder(n.left)                         # 왼쪽 서브트리 처리    
        print(n.data, end = " ")                 # 루트 노드 처리
        inorder(n.right)                        # 오른쪽 서브트리 처리

def postorder(n):                               # 후위 순회 (LRV)
    if n is not None:                   
        postorder(n.left)                       # 왼쪽 서브트리 처리
        postorder(n.right)                      # 오른쪽 서브트리 처리
        print(n.data, end = " ")                # 루트 노드 처리

def levelorder(root):                           # level 순회
    queue = CircularQueue()                     # 큐 객체 초기화
    queue.enqueue(root)                         # 최초의 큐에는 루트 노드만 들어있음.
    while not queue.isEmpty():                  # 큐가 공백상태가 아닌 동안
        n = queue.dequeue()                     # 큐에서 맨 앞의 노드 n을 꺼냄
        if n is not None:
            print(n.data, end = " ")            # 먼저 노드의 정보를 출럭
            queue.enqueue(n.left)               # n의 왼쪽 자식 노드를 큐에 삽입
            queue.enqueue(n.right)              # n의 오른쪽 자식 노드를 큐에 삽입
    
def count_node(n):                              # 순환을 이용해 트리의 노드 수를 계산하는 함수.
    if n is  None:                              # n이 None이면 공백 트리 --> 0을 반환
        return 0                                
    else:                                       # 좌우 서브트리의 노드수의 합 +1을 반환(순환 이용)
        return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n):                              # 단말 노드 개수
    if n is None:                               # 공백 트리 --> 0을 반환
        return 0                                            
    elif n.left is None and n.right is None:    # 단말 노드 --> 1을 반환
        return 1    
    else:                                       # 비단말 노드: 좌우 서브트리의 결과 합을 반환
        return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):                             # 트리의 높이를 계산하는 함수
    if n is None:                               # 공백 트리 --> 0을 반환
        return 0
    hLeft = calc_height(n.left)                 # 좌우의 높이를 측정
    hRight = calc_height(n.right)
    if (hLeft > hRight):                        # 더 높은 높이를 출력
        return hLeft + 1
    else:
        return hRight + 1

# ================================== 8-2 =============================================
def is_complete_binary_tree(root):              # 완전이진트리인지 검사하는 함수
    # 공백 트리는 완전이진트리가 아니다
    if root is None:
        return False

    # 서브트리를 가지지 않는 노드를 만난다면 flag 값을 변환한다.
    flag = False

    que = CircularQueue()

    # root 노드를 삽입해준다.
    que.enqueue(root)

    # 큐가 비어있을때까지
    while(que.size() > 0):
        # 큐의 노드를 꺼내온다.
        tempNode = que.dequeue()
        # 왼쪽 서브트리가 존재한다면
        if(tempNode.left):
            # 서브트리를 가지지 않는 노드를 만났었다면
            if flag == True:
                # 완전이진트리가 아니다
                return False
            # 현재노드의 왼쪽 서브트리 enqueue
            que.enqueue(tempNode.left)
        # 왼쪽 서브트리가 존재하지 않는다면
        else:
            flag = True
        # 오른쪽 서브트리가 존재한다면
        if(tempNode.right):
            # 서브트리를 가지지 않는 노드를 만났었다면
            if flag == True:
                # 완전 이진트리가 아니다
                return False
            # 현재노드의 오른쪽 서브트리 enqueue
            que.enqueue(tempNode.right)
        # 오른쪽 서브트리가 없다면
        else:
            flag = True
    # 무사히 검사가 종료되었다면 완전이진트리
    return True

# ================================== 8-6 =============================================
def reverse(root):                              # 트리를 좌우 반전하는 함수
    # 트리가 비어있다면 None 반환
    if root is None:
        return None

    # 트리의 좌우 반전
    root.left , root.right = root.right, root.left

    # 서브트리도 좌우 반전해준다.
    reverse(root.left)
    reverse(root.right)

    return root 

# ================================== 테스트 프로그램 =============================================
def test1():
    d = TNode("D")
    g = TNode("G")
    h = TNode("H")
    f = TNode("F")
    b = TNode("B",d)
    e = TNode("E",g,h)
    c = TNode("C",e,f)
    root = TNode("A",b,c)

    node = count_node(root)
    leaf = count_leaf(root)
    height = calc_height(root)

    print(" 1번 트리 ")
    print("[트리의 노드의 개수] : ",node);      
    print("[트리의 단말 노드의 개수] : ",leaf);  
    print("[트리의 높이] : ",height);           

    print("[전위 순회]" ,end=" ");    preorder(root); print()
    print("[중위 순회]" ,end=" ");     inorder(root); print()
    print("[후위 순회]" ,end=" ");   postorder(root); print()
    print("[높이 순회]" ,end=" ");  levelorder(root); print()

def test2():
    a = TNode("A")
    b = TNode("B")
    c = TNode("C")
    d = TNode("D")
    e = TNode("E")
    sep = TNode("/",a,b)
    multi = TNode("*",sep,c)
    multi2 = TNode("*",multi,d)
    root = TNode('+',multi2,e) 

    node = count_node(root)
    leaf = count_leaf(root)
    height = calc_height(root)

    print(" 2번 트리 ")
    print("[트리의 노드의 개수] : ",node);      
    print("[트리의 단말 노드의 개수] : ",leaf);  
    print("[트리의 높이] : ",height);   

    print("[전위 순회]" ,end=" ");    preorder(root); print()
    print("[중위 순회]" ,end=" ");     inorder(root); print()
    print("[후위 순회]" ,end=" ");   postorder(root); print()
    print("[높이 순회]" ,end=" ");  levelorder(root); print()

def test3():
    c = TNode("C")
    d = TNode("D")
    f = TNode("F")
    # g = TNode("G")
    # e = TNode('E',g,f)
    b = TNode("B",c,d)
    e = TNode("E",None,f)
    root = TNode("A",b,e)

    if is_complete_binary_tree(root):
        print("완전이진트리가 맞습니다.")
    else:
        print("완전이진트리가 아닙니다.")

def test4():
    c = TNode("C")
    d = TNode("D")
    f = TNode("F")
    b = TNode("B",c,d)
    e = TNode("E",None,f)
    root = TNode("A",b,e)
    reverse(root)
    print("[높이 순회]" ,end=" ");  levelorder(root); print()
    

print("----------------------------------------------------------------------------------------")
test1()     # 8-1
print("----------------------------------------------------------------------------------------")
test2()     # 8-1
print("----------------------------------------------------------------------------------------")
test3()     # 8-2
print("----------------------------------------------------------------------------------------")
test4()     # 8-6