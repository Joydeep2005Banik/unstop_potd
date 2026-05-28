def max_remaining_sum(N, A, T):
    """
    Write your logic here.
    Parameters:
        N (int): The number of elements in the array.
        A (list): List of integers representing the array.
        T (list of list): 2D list representing the time matrix.
    Returns:
        int: Computed result based on the problem statement.
    """
    res=0
    runmax=0
    for val in A:
        if val >= runmax:
            res=res+val
            runmax=val
    return res

import sys
input = sys.stdin.read
data = input().strip().split()

N = int(data[0])  # First input is the integer N
A = list(map(int, data[1:N+1]))  # Next N inputs are the array elements
T = []
index = N + 1
for i in range(N):
    T.append(list(map(int, data[index:index + N])))
    index += N

# Call user logic function and print the output
result = max_remaining_sum(N, A, T)
print(result)
