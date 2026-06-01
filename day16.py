import heapq
def starlight_jumps(N, M, K, bits, edges):
    # User will implement the logic here
    # Parameters:
    # N: number of nodes
    # M: number of jumps (edges)
    # K: number of 1s in the starting bit configuration
    # bits: positions of bits set in the starting bit configuration
    # edges: list of edges with (u, v, cost, bm, flip_mask)
    # Returns:
    # int: minimum energy cost or -1 if no path exists
    init_config=0
    for b in bits:
        init_config |= (1 << b)

    adj=[[] for _ in range(N+1)]
    for u,v,cost,bm,flip_mask in edges:
        adj[u].append((v,cost,bm,flip_mask))

    INF=float('inf')
    dist=[[INF]*1024 for _ in range(N+1)]
    dist[1][init_config]=0
    heap = [(0,1,init_config)]

    while heap:
        cost,u,config=heapq.heappop(heap)

        if cost > dist[u][config]:
            continue

        for v, edge_cost, bm, flip_mask in adj[u]:
            if (config & bm)!=bm:
                continue

            new_config=config^flip_mask
            new_cost=cost+edge_cost

            if new_cost < dist[v][new_config]:
                dist[v][new_config]=new_cost
                heapq.heappush(heap,(new_cost,v,new_config))

    result=dist[N][init_config]
    if result!=INF:
        return result
    else:
        return -1
    

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    bits = list(map(int, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    
    # Call user logic function and print the output
    result = starlight_jumps(N, M, K, bits, edges)
    print(result)
