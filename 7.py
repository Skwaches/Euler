"""
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the
6th prime is 13.
What is the
10001st prime number?
"""
import math
primes = [2,3,5,7,11,13]
def isPrime(number):
    if number in primes:
        return True
    if number <= 0:
        return False
    lowerBound = math.sqrt(number);
    for divisor in range(2,int(lowerBound) + 1):
        if number%divisor == 0:
            return False
    primes.append(number)
    return True

if __name__ == "__main__":
    i = 13
    while(len(primes) < 10001):
        isPrime(i)
        i += 1
    print(primes[10000])
