from collections import deque
# for both O(V+E)
def dfs(g,v, visited=set()):
    stk = []
    if v not in g.keys():
        return
    if not visited or v not in visited:
        stk.append(v)
        visited.add(v)
    elif v in visited:
        return
    while stk:
        print(stk.pop())
        if len(g[v]):
            for x in g[v]:
                dfs(g,x,visited)
    return

def bfs(g,v,visited = set()):
    q = deque()

    if v not in g.keys():
        return
    if not visited or v not in visited:
        visited.add(v)
        q.append(v)
    while q:
        node = q.popleft()
        print(node)
        if len(g[node]):
            for x in g[node]:
                if x not in visited:
                    visited.add(x)
                    q.append(x)

def check_cycle(g,v):
    visited = set()
    q = deque()
    if v not in g.keys():
        return
    if not visited or v not in visited:
        visited.add(v)
        q.append(v)
    while q:
        node = q.popleft()
        if len(g[node]):
            for x in g[node]:
                if x in visited:
                    return True
                else:
                    visited.add(x)
                    q.append(x)
    return False


graph = {
    0:[1,3],
    1:[2],
    2:[],
    3:[4,6,7],
    4:[2,5,8],
    5:[2,4,8],
    6:[],
    7:[],
    8:[]
}
print("DFS Traversal")
dfs(graph,0)

print("BFS Traversal")
bfs(graph,0)

print("cycle?")
print(check_cycle(graph,0))