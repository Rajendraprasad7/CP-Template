# Adjacency List [space O(V+E) might reduce to O(V^2) if vC2 edges]
# l = [[] for i in range(v+1)]
# for i in range(e):
#     x,y = inum()
#     l[x].append(y)
#     l[y].append(x)

# Adjacency matrix [space O(V^2)]
# l = [[0 for i in range(v+1)] for i in range(v+1)]
# for i in range(e):
#     x,y = inum()
#     l[x][y] = 1 
#     l[y][x] = 1

# Recursive DFS O(V) for tree, O(V+E) for graph
# vis = [0 for i in range(v+1)]
# traversed = []
# def dfs(vertex):
#     vis[vertex] = 1
#     traversed.append(vertex)
#     for child in l[vertex]:
#         if not vis[child]:
#             dfs(child)

#Iterative DFS 
# def dfs():
#     while len(stack):
#         if not vis[stack[-1]]:
#             vis[stack[-1]] = 1
#             traversed.append(stack[-1])
#         f = False
#         for child in l[stack[-1]]:
#             if not vis[child]:
#                 f = True 
#                 stack.append(child)
#         if not f:
#             stack.pop()

# HEIGHT AND DEPTH OF A NODE IN A TREE
# heights = [-1]*(v+1)
# depths = [-1]*(v+1)
# def dfs(vertex,dep = 0):
#     vis[vertex] = True 
#     depths[vertex] = dep
#     traversed.append(vertex)
#     f = False 
#     for child in l[vertex]:
#         if not vis[child]:
#             dfs(child,dep+1)
#             f = True 
#     if not f:
#         heights[vertex] = 0
#     else:
#         tmp = -1
#         for child in l[vertex]:
#             tmp = max(tmp,heights[child])
#         heights[vertex] = tmp+1

# LOWEST COMMON ANCESTOR(TREE) IN O(N). NOT EFFICIENT, CAN BE DONE IN O(1)
# def lowest_common_ancestor(v1,v2):
#     parent = [0 for i in range(v+1)]
#     def dfs(vertex,par):
#         parent[vertex] = par
#         for child in l[vertex]:
#             if child != par:
#                 dfs(child,vertex)
#     dfs(1,0)
#     path1,path2 = [],[]
#     cur = parent[v1]
#     while cur != 0:
#         path1.append(cur)
#         cur = parent[cur]
#     cur = parent[v2]
#     while cur != 0:
#         path2.append(cur)
#         cur = parent[cur]
#     path1 = path1[::-1]
#     path2 = path2[::-1]
#     lca = 1
#     for i in range(min(len(path1),len(path2))):
#         if path1[i] == path2[i]:
#             lca = path1[i]
#         else:
#             break
#     return lca

# BFS O(V+E)
# vis = [0 for i in range(v+1)]
# lev = [1]*(v+1)
# q = deque()
# q.append(1)
# traversed = [1]
# vis[1] = 1
# def bfs(queue):
#     while len(queue):
#         for child in l[queue[0]]:
#             if not vis[child]:
#                 lev[child] = lev[queue[0]]+1
#                 queue.append(child)
#                 traversed.append(child)
#                 vis[child] = 1
#         queue.popleft()
# bfs(q)
# print(traversed)

# DIJKSTRA'S ALGO FOR SHORTEST PATH
# vis = [0]*(n+1)
# dist = [float('inf')]*(n+1)
# prev = [-1]*(n+1)
# def dijkstra():
#     while len(h):
#         cur = heappop(h)[1]
#         if vis[cur]:
#             continue
#         vis[cur] = 1
#         for child in l[cur]:
#             ch,cwt = child 
#             if cwt+dist[cur] < dist[ch]:
#                 prev[ch] = cur
#                 dist[ch] = cwt+dist[cur]
#                 heappush(h,[cwt+dist[cur],ch])

# Increase stack size
# def bootstrap(f, stack=[]):
#     def wrappedfunc(*args, **kwargs):
#         if stack:
#             return f(*args, **kwargs)
#         to = f(*args, **kwargs)
#         while True:
#             if type(to) is GeneratorType:
#                 stack.append(to)
#                 to = next(to)
#             else:
#                 stack.pop()
#                 if not stack:
#                     break
#                 to = stack[-1].send(to)
#         return to
#     return wrappedfunc