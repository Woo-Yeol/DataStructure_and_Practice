# 데이터
items = []

    # O(n)
def insert(pos, elem):
    items.insert(pos.elem)

    # O(n)
    def delete(pos):
        items.pop(pos)

    # O(1)  
    def isEmpty():
        return size() == 0

    def getEntry(pos):
        return items[pos]

    def size():
        return len(items)

# items를 초기화
    def clear():
        # global items
        items = []

    def find(item):
        return items.index(item)

    def replace(pos, elem) :
        items[pos] = elem

    def sort():
        items.sort()

# 두 가지 리스트를 병합
    def merge(lst):
        items.extend(lst)

    def display(msg='ArrayList:'):
        print(msg, size(), items)

# __name__ : 파이썬이 내부적으로 사용하는 특별한 변수 이름.
# 이 파일(listArray.py) 실행 : _name_ == "__main__"
# 다른 파일에서 모듈을 import해서 사용해보는 경우
# 만약 다른 파일에서 이 모듈을 불러서 사용: __name__ == "listArrayFunc"

if __name__ == "__main__" :
    display('파이싼 리스트로 구현한 리스트 테스트')
    insert(0,10); insert(0,20); insert(1,30)
    insert(size(), 40); insert(2,50)
    display("파이썬 리스트로 구현한 List(삽입X5): ")
    sort()
    display("파이썬 리스트로 구현한 List(정렬후): ")
    replace(2,90)
    display("파이썬 리스트로 구현한 List(교체X1): ")
    delete(2); delete(size()-1); delete(0)
    display("파이썬 리스트로 구현한 List(삭제X3): ")
    lst = [1, 2, 3]
    if isEmpty():
        print("리스트가 비었습니다.")
    else:
        print("리스트가 비어있지 않습니다.")
    merge(lst)
    display("파이썬 리스트로 구현한 List(병합+3): ")
    clear()
    display("파이썬 리스트로 구현한 List(정리후): ")
