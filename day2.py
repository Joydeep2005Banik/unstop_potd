def LongestConsecutiveCharacter(s):
    """
    Write your logic here.
    Parameters:
        s (str): The passcode string consisting of lowercase alphabets
    Returns:
        int: Length of the longest part of the passcode that contains only one unique character
    """


    max_len=1
    curr_length=1

    if not s:
        return 0

    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            curr_length+= 1
        else:
            max_len = max(max_len,curr_length)
            curr_length=1
    ans=max(max_len,curr_length)
    return ans


def main():
    import sys
    input = sys.stdin.read
    s = input().strip()  # Reading the input passcode string
    
    # Call user logic function and print the output
    result = LongestConsecutiveCharacter(s)
    print(result)

if __name__ == "__main__":
    main()