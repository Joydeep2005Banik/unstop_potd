def can_select_people(N, K, arr):
    """
    Write your logic here.
    Parameters:
        N (int): Number of people
        K (int): Village number
        arr (list): List of integers assigned to each person
    Returns:
        str: "YES" or "NO" based on the problem statement
    """
    b=[False]*(K + 1)
    b[0]=True

    for i in arr:
        for j in range(K,i-1,-1):
            if b[j-i]:
                b[j]=True

    if b[K]:
        return "YES"
    else:
        return "NO"



def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # First input is the number of people
    K = int(data[1])  # Second input is the village number
    arr = list(map(int, data[2:2 + N]))  # Next N inputs are the numbers assigned to each person
    
    # Call user logic function and print the output
    result = can_select_people(N, K, arr)
    print(result)

if __name__ == "__main__":
    main()