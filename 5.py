"""
2520 is the smallest number that can be divided
by each of the numbers from 1 to 10
without any remainder.

What is the smallest positive number
that is evenly divisible by all of the numbers from
to 20?
"""

unique = [i for i in range(1,21)]
def accurate(number):
    for digit in unique:
        if number % digit != 0:
            return False
    return True

if __name__ == "__main__":
    for i in range(20,400000000,20):
        if accurate(i):
            print(i)
            break
