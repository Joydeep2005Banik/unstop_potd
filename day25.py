class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.count=n

    def find(self,i):
        if self.parent[i] == i:
            return i
        self.parent[i]=self.find(self.parent[i])
        return self.parent[i]

    def union(self,i,j):
        root_i=self.find(i)
        root_j=self.find(j)
        if root_i != root_j:
            self.parent[root_i]=root_j
            self.count=self.count-1

def get_anagram_groups(strs):

    if not strs:
        return 0

    n=len(strs)
    uf=UnionFind(n)
    
    def is_similar(s1, s2):
        if s1 == s2:
            return True
        
        diff=0
        for c1,c2 in zip(s1,s2):
            if c1 != c2:
                diff=diff+1
                if diff > 4:
                    return False
                    
        return diff == 4

    for i in range(n):
        for j in range(i+1,n):
            if is_similar(strs[i],strs[j]):
                uf.union(i,j)
                
    return uf.count

if __name__ == "__main__":
    n = int(input())

    if n == 0:
        print(0)
    else:
        arr = input().split(' ')
        if not arr[0]:
            arr = input().split(' ')

        groups = get_anagram_groups(arr)
        print(groups)