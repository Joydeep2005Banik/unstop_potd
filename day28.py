def can_partition_k_subsets(arr, k):
    """
    Write your logic here.
    Parameters:
        arr (list): List of integers
        k (int): Number of subsets to partition the array into
    Returns:
        bool: True if it is possible to partition the array into k non-empty subsets with equal sum, otherwise False
    """
    total=sum(arr)
    
    if total % k != 0:
        return False
    
    target=total // k
    
    if max(arr) > target:
        return False
    
    arr.sort(reverse=True)
    
    buckt=[0]*k
    
    def backtrack(index):
        if index == len(arr):
            return all(b == target for b in buckt)
        
        seen=set() 
        
        for i in range(k):
            if buckt[i]+arr[index] > target:
                continue
            
            if buckt[i] in seen:
                continue
            
            seen.add(buckt[i])
            buckt[i]=buckt[i]+arr[index]
            
            if backtrack(index + 1):
                return True
            
            buckt[i]=buckt[i]-arr[index]
        
        return False
    
    return backtrack(0)

import sys
input = sys.stdin.read

data = input().strip().split()

arr = list(map(int, data[:-1]))  # All inputs except the last one are part of the array
k = int(data[-1])  # The last input is the integer k

result = can_partition_k_subsets(arr, k)
print("true" if result else "false")