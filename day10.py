def count_balanced_subarrays(arr, k):
    """
    Write your logic here.
    Parameters:
        arr (list): List of integers representing the energy levels of each device.
        k (int): Integer representing the window size.
    Returns:
        int: Number of balanced subarrays of size k.
    """
    n=len(arr)
    half=k // 2
    
    prefix=[0]*(n+1)
    for i in range(n):
        prefix[i+1]=prefix[i]+arr[i]
    
    count=0
    for i in range(n-k+1):
        left=prefix[i+half]-prefix[i]
        right=prefix[i+k]-prefix[i+k-half]
        if left==right:
            count=count+1
    
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    k = int(data[1])  # Second input is the integer K
    
    arr = list(map(int, data[2:]))  # Remaining input is the array of integers
    
    # Call user logic function and print the output
    result = count_balanced_subarrays(arr, k)
    print(result)

if __name__ == "__main__":
    main()
