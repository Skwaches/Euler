"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then  a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""

def divisors(n):
    divisors = []
    for i in range(1,int(n/2) + 1):
        if n%i == 0:
            divisors.append(i)
    return divisors

def d(n):
    return sum(divisors(n))

if __name__=="__main__":
    total = 0;
    marked = []
    for i in range(int(10000)):
        if i in marked:
            continue
        a = d(i)
        if a in marked:
            continue
        if d(a) == i:
            marked.append(a)
            marked.append(i)
            if a == i:
                continue
            total += i + a

    print(total)
