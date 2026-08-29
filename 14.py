"""

The following iterative sequence is defined for the set of positive integers:
    n -> n/2    (n is even)
    n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def next(n)->int:
    if n%2==0:
        return n/2
    else:
        return 3*n + 1

mappings: dict[int,int] = {} #Start, steps to 1
def generate():
    for i in range(1,1000000):
        value = i
        steps = 1
        while(value != 1):
            value = next(value)
            if (value in mappings):
                steps += mappings[value]
                break
            steps+=1
        mappings[i] = steps

if __name__ == "__main__":
    generate();
    pairs = list(zip(mappings.values(),mappings.keys()))
    pairs.sort()
    maximum = pairs[-1][1]
    print(maximum, mappings[maximum])
