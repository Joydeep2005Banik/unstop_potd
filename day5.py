from collections import Counter



def shortest_substring_length(S, L):
    """
    Write your logic here.
    Parameters:
        S (str): The longer string
        L (str): The secret code
    Returns:
        int: Length of the shortest substring of S that contains all the characters of L in any order, or -1 if no such substring exists
    """
    l_count=Counter(L)
    req=len(l_count)
    
    left,right=0,0
    form=0
    window_count={}
    min_len=float('inf')
    
    while right < len(S):
        char=S[right]
        window_count[char]=window_count.get(char,0) + 1
        
        if char in l_count and window_count[char] == l_count[char]:
            form=form+1
        
        while left <= right and form == req:
            char=S[left]
            
            if right - left + 1 < min_len:
                min_len = right - left + 1
            
            window_count[char] -= 1
            if char in l_count and window_count[char] < l_count[char]:
                form=form-1
            
            left=left+1
        
        right=right+1
    
    return min_len if min_len != float('inf') else -1


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    S = data[0]  # First line is the longer string S
    L = data[1]  # Second line is the secret code L
    
    # Call user logic function and print the output
    result = shortest_substring_length(S, L)
    print(result)

if __name__ == "__main__":
    main()