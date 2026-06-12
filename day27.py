def user_logic(N, T, room_data):
    """
    Write your logic here.
    Parameters:
        N (int): Number of rooms
        T (int): Total hours
        room_data (list of tuples): Each tuple contains (K, E, intervals) where
            K (int): Number of required intervals
            E (int): Energy limit for the room
            intervals (list of tuples): Each tuple contains (L, R) representing the interval
    Returns:
        list of list of int or str: A list where each element is either:
            - A list of T integers representing the AC mode for each hour if a schedule is possible.
            - The string "NOT POSSIBLE" if no schedule can be made for a room.
    """
    res=[]

    for (K,E,intervals) in room_data:
        req=[False]*T
        for (L, R) in intervals:
            for h in range(L - 1, R):
                req[h] = True

        req_count = sum(req)

        if req_count > E:
            res.append("NOT POSSIBLE")
            continue


        schd=[1 if req[h] else 0 for h in range(T)]
        res.append(schd)

    return res

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    index = 0
    N = int(data[index])
    index += 1
    T = int(data[index])
    index += 1

    room_data = []
    for _ in range(N):
        K = int(data[index])
        index += 1
        E = int(data[index])
        index += 1
        intervals = []
        for _ in range(K):
            L = int(data[index])
            index += 1
            R = int(data[index])
            index += 1
            intervals.append((L, R))
        room_data.append((K, E, intervals))
    
    # Call user logic function
    results = user_logic(N, T, room_data)
    
    # Print the output as per the problem statement
    for result in results:
        if isinstance(result, str):
            print(result)
        else:
            print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
