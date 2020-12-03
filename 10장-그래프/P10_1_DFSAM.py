def dfs_recur(adj, vtx, visited, id):           # 깊이 우선 탐색 순환 함수
    if visited[id] == False:                    # 방문하지 않은 정점이라면
        visited[id] = True                      # 정점을 방문 표시를 해준다.
        print(vtx[id] , end=" ")                # 해당 정점 출력
        for i in range(len(vtx)):               # 모든 정점에 관하여
            if adj[id][i] == 1:                 # 인접 정점이라면
                dfs_recur(adj,vtx,visited,i)    # 그 정점을 기점으로 다시 깊이우선탐색
        

def dfs(adj,vtx,s):                             # 순환으로 구현하기 위한 초기화 함수
    n = len(vtx)                                
    visited = [False]*n                         # 방문한 정점 초기화
    dfs_recur(adj,vtx,visited,s)                # 깊이 우선 탐색 순환 함수 호출

# 정점
vertex =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# 인접 행렬
adjMat =[ [ 0,   1,   1,   0,   0,   0,   0,   0 ],
          [ 1,   0,   0,   1,   0,   0,   0,   0 ],
          [ 1,   0,   0,   1,   1,   0,   0,   0 ],
          [ 0,   1,   1,   0,   0,   1,   0,   0 ],
          [ 0,   0,   1,   0,   0,   0,   1,   1 ],
          [ 0,   0,   0,   1,   0,   0,   0,   0 ],
          [ 0,   0,   0,   0,   1,   0,   0,   1 ],
          [ 0,   0,   0,   0,   1,   0,   1,   0 ] 
]
print('DFS : ', end = "")
dfs(adjMat, vertex, 0)  # 인접행렬, 정점, 시작 정점의 인덱스
print()