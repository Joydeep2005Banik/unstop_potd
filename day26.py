from itertools import combinations


def countValidCombos(N, K, L, R, deviceTypes, prices):
    # User needs to implement this function
    count=0
    for combo in combinations(range(N),K):
        total=sum(prices[i] for i in combo)
        if L <= total <= R:
            count=count+1
    return count


if __name__ == "__main__":
    N, K, L, R = map(int, input().split())
    deviceTypes = []
    prices = []
    for _ in range(N):
        line = input().split()
        deviceTypes.append(line[0])
        prices.append(int(line[1]))
    
    # Call the user logic function and print the result
    result = countValidCombos(N, K, L, R, deviceTypes, prices)
    print(result)
