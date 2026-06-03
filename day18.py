def process_dashes(n, s):
    """
    Write your logic here.
    Parameters:
        n (int): Length of the string
        s (str): String containing lowercase English letters and dashes ('_')
    Returns:
        str: Resultant string after processing dashes, or "-1" if impossible
    """
    stack=[]
    for ch in s:
        if ch == '_':
            if not stack:
                return "-1"
            stack.pop()
        else:
            stack.append(ch)
    
    return "".join(stack) if stack else "-1"

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    s = data[1]  # Second input is the string of length n
    
    # Call user logic function and print the output
    result = process_dashes(n, s)
    print(result)

if __name__ == "__main__":
    main()