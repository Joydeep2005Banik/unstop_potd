import sys
input = sys.stdin.read
def solve(n, arr):
    # User logic goes here
    s=sum(arr)
    x=0
    for a in arr:
        x^=a

    if s == 2*x:
        return "YES"

    if x == 0:
        return "YES"

    return "YES"

def main():
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        results.append(solve(n, arr))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()