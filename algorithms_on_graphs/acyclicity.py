#Uses python3

import sys

def explore(adj, u, visited=[], path=[]):
    
    visited.append(u)
    path.append(u)

    for v in adj[u]:
        if v not in visited:
            if explore(adj, v, visited, path[:] ) == 0:
                return 0
        else:
            if v in path:
                return 0
            

            
    return 1

def acyclic(adj):

    visited=[]
    for u in range(len(adj)):
        if u not in visited:
            if explore(adj, u, visited  ) == 0:
                return 0

    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
