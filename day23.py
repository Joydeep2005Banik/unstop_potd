import sys

# Function declaration
def peakIndexInMountainArray(A):
    # User logic here
    n=len(A)
    for i in range(n):
        left=(i == 0) or (A[i] >= A[i-1])
        right=(i == n-1) or (A[i] >= A[i+1])
        if left and right:
            return i
    return -1

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(peakIndexInMountainArray(arr))
