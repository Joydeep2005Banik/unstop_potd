from collections import defaultdict
from bisect import bisect_left

def user_logic(n,s,arr):
    positions=defaultdict(list)
    for i,val in enumerate(arr):
        positions[val].append(i+1)

    def next_occurrence(v,p):
        pos_list=positions[v]
        cycle=(p-1)//n
        offset=(p-1) % n + 1         

        idx=bisect_left(pos_list,offset)
        if idx < len(pos_list):
            return cycle * n + pos_list[idx]
        else:                          
            return (cycle+1) * n + pos_list[0]

    dp=[0]*(s+1)

    for i in range(1,s+1):
        best=0
        for v in range(1,i+1):
            if v in positions:
                pos=next_occurrence(v,dp[i-v]+1)
                if pos > best:
                    best=pos
        dp[i]=best

    return dp[s]


def main():
    import sys
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    s = int(data[1])
    arr = list(map(int, data[2:]))
    print(user_logic(n, s, arr))

if __name__ == "__main__":
    main()