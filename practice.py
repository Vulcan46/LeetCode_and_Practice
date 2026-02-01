from collections import Counter, defaultdict, deque

#count the occurances of letters in a string or seq
counts=Counter("mississipi")
print(counts)


# creates a dict  in which any new key as a value of an empty list.
# very useful for adjacency lists for representing graphs.

adj_list = defaultdict(list)

#edge between 1 and 2.
u,v = 1,2
adj_list[u].append(v)
#if grahp is directed we stop on above line , else we also add u to v's list
adj_list[v].append(u)


def bfs(root):
    if not root:
        return []
    queue = deque([root])

    maxd = rdepth = ldepth = 1
    while queue:
        lv_size = len(root)
        for _ in range(lv_size):
            node = queue.popleft()
            visited.append(node)
            if node.left:
                queue.append(node.left)
                ldepth +=1
            if node.right:
                queue.append(node.right)
                rdepth+=1
            if ldepth>=rdepth:
                maxd = ldepth
            else:
                maxd = rdepth
    return maxd




