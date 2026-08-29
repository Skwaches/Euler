"""
Euler discovered the remarkable quadratic formula:
    n^2 + n + 41
It turns out that the formula will produce 40
primes for the consecutive integer values 0 <= n <= 39.
However, when n = 40:
    40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41
and certainly when n = 41:
    41^2 + 41 + 41
is clearly divisible by 41

The incredible formula
    n^2 - 79n + 1601
was discovered, which produces 80
primes for the consecutive values 0 <= n <= 79.
The product of the coefficients, -79 and 1601,
is -126479.

Considering quadratics of the form:
    n^2 + an + b, where |a| < 1000 and |b| <= 1000 

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4
    and

Find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum
number of primes for consecutive values of n,
starting with n = 0
"""

q7 = __import__("7")
def primeRun(a, b):
    n = 0
    while q7.isPrime(n**2 + a*n + b):
        n+=1
    return n

if __name__=="__main__":
    parameters = (0,0)
    longest = 0
    for a in range(-999,1000):
        for b in range(-1000,1001):
            run = primeRun(a,b)
            if run > longest:
                parameters = (a,b)

    print(parameters[0] * parameters[1])




