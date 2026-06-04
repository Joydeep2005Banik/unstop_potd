
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def user_logic(t, test_cases):
    """
    Write your logic here.
    Parameters:
        t (int): Number of test cases
        test_cases (list): List of tuples, each containing:
                           - N (int): Number of levels in the binary tree
                           - arr (list): List of integers representing the nodes of the binary tree in level order
    Returns:
        list: List of lists, where each inner list is the pre-order traversal of the pruned binary tree
    """
    results = []
    for N, arr in test_cases:
        # User will implement this part
        if not arr:
            results.append([])
            continue

        nodes=[TreeNode(v) for v in arr]
        for i in range(len(nodes)):
            left_idx=2*i+1
            right_idx=2*i +2
            if left_idx < len(nodes):
                nodes[i].left=nodes[left_idx]
            if right_idx < len(nodes):
                nodes[i].right=nodes[right_idx]

        root=nodes[0]

        def prune(node):
            if node is None:
                return
            node.right=None
            prune(node.left)

        prune(root)

        def preorder(node,acc):
            if node is None:
                return
            acc.append(node.val)
            preorder(node.left,acc)
            preorder(node.right,acc)  
        traversal=[]
        preorder(root,traversal)
        results.append(traversal)
        
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    test_cases = []
    for _ in range(t):
        N = int(data[index])
        index += 1
        number_of_nodes = 2**N - 1
        arr = list(map(int, data[index:index + number_of_nodes]))
        index += number_of_nodes
        test_cases.append((N, arr))
    
    # Call user logic function
    results = user_logic(t, test_cases)
    
    # Print the results
    for result in results:
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
