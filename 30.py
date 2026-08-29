"""
Surprisingly there are only three numbers
that can be written as the sum of fourth powers of their digits:
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4
is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def appropriate(number,power):
    items = list(str(number))
    items = [(int(item))**power for item in items]
    total = sum(items)
    return total == number

# For a k digit number:
# Largest sum of powers of 5: 9^5 * k = 59049k
# Smallest k-digit number:  10^(k-1)
# 10^(k-1) > 59049k for k >= 7: Thus k <= 6
# so f(n) <= 59049 * 6 = 354294 for this range of k
# And because f(n) = n; n is also capped at 354294
if __name__ == "__main__":
    total = 0
    for i in range(2,354294+1):
        if appropriate(i,5):
            total += i
    print(total)

