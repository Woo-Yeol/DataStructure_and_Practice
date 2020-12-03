def st_dfs_recur(adj, vtx, visited, id):

def st_dfs(adj,vtx,s):
    n = len(vtx)
    visited = [False]*n
    st_dfs_recur(adj,vtx,visited,s)

vertex =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjMat =[ [ 0,   1,   1,   0,   0,   0,   0,   0 ],
          [ 1,   0,   0,   1,   0,   0,   0,   0 ],
          [ 1,   0,   0,   1,   1,   0,   0,   0 ],
          [ 0,   1,   1,   0,   0,   1,   0,   0 ],
          [ 0,   0,   1,   0,   0,   0,   1,   1 ],
          [ 0,   0,   0,   1,   0,   0,   0,   0 ],
          [ 0,   0,   0,   0,   1,   0,   0,   1 ],
          [ 0,   0,   0,   0,   1,   0,   1,   0 ] 
]
print('Spanning Tree(DFS) : ', end = "")
st_dfs(adjMat, vertex, 0)
print()