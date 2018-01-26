def genPrimes():
    x = 1
    primes = [2]
    while True:
        isprime = True
        x += 1
        for p in primes[:]:
            if x % p == 0 and x != p:
                isprime = False
                break
        if isprime == True:
            yield x
            primes.append(x)

a = genPrimes()