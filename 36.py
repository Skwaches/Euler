"""
The decimal number, 585 = 1001001001
(binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10
and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

# Question 4 also had a palindrome question.
# No leading zero means last digit cannot be 0 meaning odd digits only.
# I kinda feel bad for not writing my own binary converter...
# Lol, no I don't
if __name__ == "__main__":
    q4 = __import__("4")
    total = 0
    for i in range(1, 1000000, 2):
        binary = bin(i)[2:] 
        if q4.isPalindrome(i) and q4.isPalindrome(binary):
            total += i;
    print(total)

        
