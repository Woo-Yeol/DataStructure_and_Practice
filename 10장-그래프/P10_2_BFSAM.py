# 파이썬의 queue 모듈의 Queue 클래스를 사용한다.
from queue import Queue

# 너비 우선 탐색
def bfs(adj,vtx,s):
    visited = [False] * len(vtx)                            # 방문한 정점 초기화
    queue = Queue(); queue.put(vtx[s]); visited[s] = True   # 첫 번재 정점을 큐에 넣고 해당 노드를 방문했다고 확인한다.
    while queue.qsize() != 0:                               # 공백이 아닐 때 까지
        vertex = queue.get()                                # 큐를 deque하여 해당 정점을 출력
        print(vertex, end=' ')
        s = vtx.index(vertex)                               # 출력한 정점의 인덱스를 확인하여 인접 정점 탐색할 때 사용한다.
        for i in range(len(vtx)):                           # 모든 정점에 대해서
            if adj[s][i] == 1:                              # 인접 정점이라면
                if visited[i] == False:                     # 방문 하지 않았다면
                    visited[i] = True                       # 방문했다고 하고
                    queue.put(vtx[i])                       # 해당 정점을 큐에 삽입


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

# 너비 우선 탐색 출력
print('BFS : ', end = "")

# 인접 행렬, 정점, 시작 노드의 인덱스
bfs(adjMat, vertex, 0)
print()