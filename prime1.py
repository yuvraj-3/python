#find prime no between a given range

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def findPrimes(left, right):

    primes=[]
    for n in range(left, right + 1):
        if isPrime(n):
            primes.append(n)
    return primes


print(findPrimes(10,19))