from collections import deque
def max_collapsing_realities(N, M, K, unstable_realities, dependencies):
    # User should implement this function
    # Parameters:
    # N: Number of realities
    # M: Number of dependency edges
    # K: Number of initially unstable realities
    # unstable_realities: List of IDs of initially unstable realities
    # dependencies: List of dependency pairs (A, B) meaning Reality A depends on Reality B
    # Returns:
    # int: Maximum number of realities that can collapse in total

    dep_count=[0]*N
    rev_adj=[[] for _ in range(N)]

    for A, B in dependencies:
        dep_count[A]=dep_count[A]+1
        rev_adj[B].append(A)

    in_queue=[False]*N
    queue=deque()

    for node in unstable_realities:
        if dep_count[node] == 0 and not in_queue[node]:
            in_queue[node]=True
            queue.append(node)

    count=0
    while queue:
        node=queue.popleft()
        count=count+1
        for dependent in rev_adj[node]:
            dep_count[dependent]=dep_count[dependent]-1
            if dep_count[dependent] == 0 and not in_queue[dependent]:
                in_queue[dependent]=True
                queue.append(dependent)

    return count



def main():
    N, M = map(int, input().split())

    K = int(input())

    unstable_realities = list(map(int, input().split()))

    dependencies = [tuple(map(int, input().split())) for _ in range(M)]

    result = max_collapsing_realities(N, M, K, unstable_realities, dependencies)
    print(result)


if __name__ == "__main__":
    main()
