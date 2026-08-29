"""
Find the sum of the digits in the number 100!
"""
def split(text):
    return [char for char in text]

if __name__ == "__main__":
    import math
    number = math.factorial(100)
    text = split(str(number))
    digits = [int(digit) for digit in text]
    print(sum(digits))
