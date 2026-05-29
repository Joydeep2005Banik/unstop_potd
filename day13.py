from collections import defaultdict
def largest_scc(N, edges):
    # User logic goes here
    # Parameters:
    # N: number of nodes
    # edges: list of edges where each edge is represented as a tuple (A, B)
    # Return:
    # int: size of the largest strongly connected component


    graph=defaultdict(list)
    rev_graph=defaultdict(list)

    for A, B in edges:
        graph[A].append(B)
        rev_graph[B].append(A)

    visited=[False]*(N+1)
    finish_order = []

    for start in range(1, N + 1):
        if not visited[start]:
            stack=[(start,0)]
            visited[start]=True
            while stack:
                node,idx=stack[-1]
                if idx < len(graph[node]):
                    stack[-1]=(node,idx+1)
                    nbr=graph[node][idx]
                    if not visited[nbr]:
                        visited[nbr]=True
                        stack.append((nbr,0))
                else:
                    stack.pop()
                    finish_order.append(node)  
    visited=[False]*(N+1)
    max_scc=0

    for start in reversed(finish_order):
        if not visited[start]:
            size=0
            stack=[start]
            visited[start]=True
            while stack:
                node=stack.pop()
                size=size+1
                for nbr in rev_graph[node]:
                    if not visited[nbr]:
                        visited[nbr]=True
                        stack.append(nbr)
            max_scc=max(max_scc,size)

    return max_scc



if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    edges = []
    index = 2
    for _ in range(M):
        A = int(data[index])
        B = int(data[index+1])
        edges.append((A, B))
        index += 2
    
    result = largest_scc(N, edges)
    print(result)
