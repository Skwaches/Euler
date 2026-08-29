"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:
    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9? 
"""

def arrangements(options:list, permutations:set, built:list = []):
    if not options:
        permutations.add("".join(built))
    for i in range(len(options)):
        remaining = options.copy()
        generated = built.copy()
        remaining.pop(i)
        generated.append(options[i])
        arrangements(remaining, permutations, generated)
    
if __name__ == "__main__":
    characters = [str(i) for i in range(10) ]
    permutations = set()
    arrangements(characters,permutations)
    permutations = sorted(list(permutations))
    print(permutations[1000000 - 1])
