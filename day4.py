def user_logic(N):
    MOD=10**9 + 7

    if N==0:
        return "1"


    successor={
        'a': ['e', 'u'],
        'e': ['i', 'a'],
        'i': ['o', 'e'],
        'o': ['u', 'i'],
        'u': ['a', 'o'],
    }

    vowels=['a', 'e', 'i', 'o', 'u']

    dp = {v: 1 for v in vowels}

    for _ in range(N - 1):
        new_dp = {v: 0 for v in vowels}
        for v in vowels:
            for nxt in successor[v]:
                new_dp[nxt]=(new_dp[nxt]+dp[v]) % MOD
        dp=new_dp

    total=sum(dp.values()) % MOD

    if total==0:
        return "1"

    return oct(total)[2:]  


def main():
    import sys
    data = sys.stdin.read().strip()
    N = int(data)
    result = user_logic(N)
    print(result)


if __name__ == "__main__":
    main()