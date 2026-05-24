def user_logic(s):
    # Write your logic here.
    # Parameters:
    #   s (str): The chat message string
    # Returns:
    #   int: The maximum number of balanced smiley pairs that can be formed
    happy=0
    sad=0
    i=0
    while i < len(s)-1:
        if s[i] == ':':
            if s[i+1] == ')':
                happy=happy+1
                i=i+2
                continue
            elif s[i+1] == '(':
                sad=sad+1
                i=i+2
                continue
        i=i+1
    return min(happy,sad)*2  # Placeholder return value

if __name__ == '__main__':
    s = input().strip()  # Read the entire line as input
    result = user_logic(s)
    print(result)