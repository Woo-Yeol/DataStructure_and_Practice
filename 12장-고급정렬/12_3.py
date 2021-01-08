def is_ascending_bubble_sort(A):            # 버블 정렬을 통한 오름차순 확인 함수
    n = len(A)                              # 리스트의 크기 저장
    count = 0                               # 오름차순을 확인하기 위한 연산의 갯수를 세는 count 변수
    for i in range(n-1, 0 , -1):            # 외부 루프 : n-1, n-2, ... , 2 , 1
        bChanged = False
        for j in range(i):                  # 내부 루프 : 0, 1 , ... i - 1
            if(A[j] > A[j+1]):              # 만약 오름차순이 아니라면 교환
                A[j], A[j+1] = A[j+1], A[j]
                bChanged = True             # 변화가 있다면 True 값으로 변경
                count += 1                  # 연산의 갯수를 측정
        
        if not bChanged: break;             # 변화가 없다면 break
    return count==0                         # 오름차순은 연산이 이뤄지지 않으므로 0인지 여부를 판단하여 반환
print()
A = input("수열을 입력해주세요: ").split(" ")    # 리스트 입력
ascending = is_ascending_bubble_sort(A)                  # 오름차순인지 검사
print("오름차순" if ascending else "오름차순 아님") # 삼항 연산자를 통해서 오름차순인지 아닌지를 출력
print()