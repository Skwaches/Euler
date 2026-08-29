"""
The Fibonacci sequence is defined by the recurrence relation:
    F(n) = F(n-1) + F(n-2)
Hence the first 12 terms will be:
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34
F(10) = 55
F(11) = 89
F(12) = 144

The 12th term, F(12), is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

current = 0
previous = 0

def f():
    global current, previous
    if current == 0:
        current = 1
        return
    temp = current
    current += previous
    previous = temp
    
if __name__=="__main__":
    index = 1
    while(int(current/10**(1000-1)) < 1):
        f()
        print(index)
        index += 1
