def collapse_chain(s):
    """
    Write your logic here.
    Parameters:
        s (str): Input string
    Returns:
        str: Final chain after all valid collapses have been applied or "-1" if the chain becomes empty
    """
    def energy(c):
        if c.isdigit():
            return int(c)*10
        return ord(c) - ord('a')+1

    stack=[]
    for c in s:
        e=energy(c)
        if stack and stack[-1][1] == e:
            stack.pop()
        else:
            stack.append((c,e))

    if not stack:
        return "-1"
    return "".join(c for c,_ in stack)

def main():
    import sys
    input = sys.stdin.read
    
    # Read the input string
    s = input().strip()
    
    # Call user logic function and print the output
    result = collapse_chain(s)
    print(result)

if __name__ == "__main__":
    main()