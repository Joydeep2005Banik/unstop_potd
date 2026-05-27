def compute_max_intensity_after_k_hours(N, intensities, K, queries):
    """
    Write your logic here to compute the maximum intensity within the specified range after K hours.
    Parameters:
        N (int): Number of cities
        intensities (list): Initial sandstorm intensities for each city
        K (int): Number of hours
        queries (list): List of tuples, each containing two integers l and r indicating the range of cities
    Returns:
        list: List of maximum intensities for each query after K hours
    """
    
    s=intensities[:]
 
    for _ in range(K):
        ns=[0]*N
        for i in range(N):
            if N == 1:
                ns[i]=s[i]
            elif i == 0:
                ns[i]=s[1]
            elif i == N-1:
                ns[i]=s[N-2]
            else:
                ns[i]=(s[i-1]+s[i+1]) // 2
        s=ns
 
    res=[]
    for l, r in queries:
        res.append(max(s[l - 1 : r]))
    return res






def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    index = 0
    N = int(data[index])
    index += 1
    
    intensities = []
    for _ in range(N):
        intensities.append(int(data[index]))
        index += 1
    
    K = int(data[index])
    index += 1
    
    Q = int(data[index])
    index += 1
    
    queries = []
    for _ in range(Q):
        l = int(data[index])
        r = int(data[index + 1])
        queries.append((l, r))
        index += 2
    
    # Call the function with the input parameters
    results = compute_max_intensity_after_k_hours(N, intensities, K, queries)
    
    # Print each result on a new line
    for result in results:
        print(result)

if __name__ == "__main__":
    main()