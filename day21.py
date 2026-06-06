from unittest import result


def decode_message(S):
    """
    Write your logic here.
    Parameters:
        S (str): Input string S
    Returns:
        str: Decoded message string
    """
    res=[]
    i=0
    n=len(S)
    while i < n:
        if (i+2) < n and S[i+2] == '#':
            num=int(S[i:i+2])
            res.append(chr(ord('a') + num - 1))
            i=i+3
        else:
            num=int(S[i])
            res.append(chr(ord('a') + num - 1))
            i=i+1
    return ''.join(res)

def main():
    import sys
    input = sys.stdin.read
    S = input().strip()
    
    # Call user logic function and print the output
    result = decode_message(S)
    print(result)

if __name__ == "__main__":
    main()