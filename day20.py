def user_logic(n, nums):
    """
    Write your logic here.
    Parameters:
        n (int): Size of the integer array
        nums (list): List of integers
    Returns:
        int: Computed special sum based on the problem statement
    """
    unique=set(nums)
    return sum(2**x for x in unique)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    nums = list(map(int, data[1:]))  # Remaining input is the array of integers
    
    # Call user logic function and print the output
    result = user_logic(n, nums)
    print(result)

if __name__ == "__main__":
    main()