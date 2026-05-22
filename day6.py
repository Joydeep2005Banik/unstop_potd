def is_game_winnable(N,s,q,controllers):
    p=s.count('+')
    m=N-p

    res=[]
    for A,B in controllers:
        if A == B:
            res.append("YES" if p == m else "NO")
        else:
            num=(m-p)*B
            den=A-B

            if num%den == 0:
                d=num//den
                res.append("YES" if -m <= d <= p else "NO")
            else:
                res.append("NO")
    return res

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    index = 0
    N = int(data[index])  # Read N
    index += 1
    s = data[index]  # Read string s
    index += 1
    q = int(data[index])  # Read q
    index += 1
    controllers = []
    for _ in range(q):
        A = int(data[index])
        B = int(data[index + 1])
        controllers.append((A, B))
        index += 2
    results = is_game_winnable(N, s, q, controllers)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()