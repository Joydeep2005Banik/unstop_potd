MOD = 10**9 + 7

def count_divisible_subarrays(n, k, arr):
    # User logic goes here
    freq={0:1}  
    prefix=0
    c=0

    for num in arr:
        prefix=prefix+num

        rem=prefix%k   


        
        if rem in freq:
            c=(c+freq[rem])%MOD
            freq[rem]=freq[rem]+1
        else:
            freq[rem]=1

    return c

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    result = count_divisible_subarrays(n, k, arr)
    print(result)