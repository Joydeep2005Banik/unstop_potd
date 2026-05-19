import sys

MOD=10**9+ 7

def mod_fact(k):
    res=1
    for i in range(2,k+1):
        res=res*i % MOD
    return res

def numPrimeArrangements(n):
    if n < 2:
        primes=0
    else:
        sieve=bytearray([1])*(n+1)
        sieve[0]=sieve[1]=0
        for i in range(2,int(n**0.5)+1):
            if sieve[i]:
                sieve[i*i::i]=bytearray(len(sieve[i*i::i]))
        primes=sum(sieve)

    non_primes=n-primes
    return (mod_fact(primes)*mod_fact(non_primes))% MOD

def main():
    n = int(sys.stdin.read().strip())
    print(numPrimeArrangements(n))

if __name__ == "__main__":
    main()