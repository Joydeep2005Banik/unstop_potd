from collections import deque
import queue
def chrono_locked_upgrade(n, m, chrono_lock, edges):
    """
    Write your logic here.
    Parameters:
        n (int): Number of modules
        m (int): Number of dependencies
        chrono_lock (list): List of integers representing the minimum upgrade time for each module
        edges (list of tuples): List of dependencies, where each tuple (u, v) means module u must be upgraded before module v
    Returns:
        str or int: Return "CYCLE DETECTED" if a cycle exists, otherwise the maximum upgrade time as an integer
    """
    adj=[[] for _ in range(n+1)]
    in_deg=[0]*(n+1)

    for u, v in edges:
        adj[u].append(v)
        in_deg[v]=in_deg[v]+1

    upgrade=[0]*(n+1)
    q=deque()

    for i in range(1,n+1):
        if in_deg[i] == 0:
            upgrade[i]=max(1,chrono_lock[i-1])
            q.append(i)

    process=0

    while q:
        u=q.popleft()
        process=process+1

        for v in adj[u]:
            upgrade[v]=max(upgrade[v],upgrade[u]+1)
            in_deg[v]=in_deg[v]-1
            if in_deg[v] == 0:
                upgrade[v]=max(upgrade[v],chrono_lock[v-1])
                q.append(v)

    if process != n:
        return "CYCLE DETECTED"

    return max(upgrade[1:n+1])

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    m = int(data[1])
    chrono_lock = list(map(int, data[2:2 + n]))
    edges = []
    
    index = 2 + n
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2
    
    # Call user logic function
    result = chrono_locked_upgrade(n, m, chrono_lock, edges)
    
    # Print the output
    if isinstance(result, str):
        print(result)
    else:
        print(result)

if __name__ == "__main__":
    main()