def prime():
    n = 100
    li = [False,False] + [True]*(n-1)
    primes = []
    for i in range(2,n+1):
        if li[i] :
            primes.append(i)
            for j in range(2*i, n+1, i):
                li[j] = False
    return primes
print(prime())