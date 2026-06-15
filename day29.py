def user_logic(n, s):
    """
    Write your logic here.
    Parameters:
        n (int): Length of the string
        s (str): String consisting of lowercase Latin alphabets
    Returns:
        str: Sorted string based on the given conditions
    """
    def sort_key(c):
        pos=ord(c)-ord('a')+1 
        difficulty=pos%5

        return (difficulty, -ord(c))
    
    return ''.join(sorted(s, key=sort_key))

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    s = data[1]  # Second input is the string
    
    # Call user logic function and print the output
    result = user_logic(n, s)
    print(result)

if __name__ == "__main__":
    main()