"""
The sum of the primes below 10 is,
2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
if __name__ == "__main__":
    q7 = __import__("7")
    i = 2;
    while (i < 2e6):
        q7.isPrime(i);
        i+=1;
        print(i)
    print(sum(q7.primes))
    print(q7.primes)
