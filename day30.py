class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def user_logic(head):
    """
    Write your logic here.
    Parameters:
        head (ListNode): Head node of the singly linked list
    Returns:
        str: "even" if the final number is an even number, otherwise "odd"
    """
    digits=[]
    curr=head
    while curr:
        digits.append(str(curr.val))
        curr=curr.next
    
    concatenated=int("".join(digits))
    
    reverse_num=int(str(concatenated)[::-1])
    
    digit_sum=sum(int(d) for d in str(reverse_num))
    res=reverse_num-digit_sum
    if res%2==0:
        return "even"
    else:
        return "odd"


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # Read the size of the linked list
    nodes = list(map(int, data[1:N+1]))  # Read the linked list nodes
    
    # Create the linked list from input
    head = None
    tail = None
    
    for digit in nodes:
        newNode = ListNode(digit)
        if not head:
            head = newNode  # Initialize the head if the list is empty
        else:
            tail.next = newNode  # Link the new node to the list
        tail = newNode  # Update the tail to the new node
    
    # Call user logic function and print the output
    result = user_logic(head)
    print(result)

if __name__ == "__main__":
    main()