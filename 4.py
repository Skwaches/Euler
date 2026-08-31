"""
A palindromic number reads the same both ways.
The largest palindrome,
Made from the product of two,
2-digit numbers is:
    9009 = 91 x 99
Find the largest palindrome made from the product of 
two 3-digit numbers.
"""

def isPalindrome(forward):
    if not isinstance(forward,str):
        forward = str(forward);
    return forward[::-1] == forward 

if __name__ == "__main__":
    groups = []
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            number = i * j
            if isPalindrome(number):
                groups.append(number)
                print(f"{i} * {j} = {number}");
    groups.sort(reverse = True);

    print(groups[0])
