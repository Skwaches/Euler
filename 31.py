"""
In the United Kingdom the currency is made up of pound (£)
and pence (p).
There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
# Sort denominations
# Mappings
cache:dict[int,list[list[int]]] = {}
def compress(arrangement:list[int]):
    return ", ".join([str(k) for k in arrangement]);

# This returns a list of all the possible ways to make the given arrangement.
# It uses a list instead of a set because lists can't be saved in a set.
# It caches the retrieved list and retrieves it when required.
# Since we are only asked for the number of ways to make the amount,
# returning the entire list of ways is likely unoptimised
# It takes a shit ton of time to solve
def collect(denominations, amount) -> list[list[int]]:
    if amount in cache:
        return cache[amount]
    collected:list[list[int]] = []
    saved:list[str] = []
    built = [0 for _ in range(len(denominations))]

    for i in range(len(denominations)):
        remaining = amount - denominations[i]
        if remaining < 0:
            break

        generated  = built.copy()
        generated[i] += 1
        if remaining == 0:
            compressed = compress(generated)
            if compressed not in saved:
                saved.append(compressed)
                collected.append(generated)

        needed = collect(denominations,remaining)
        for possible in needed:
            coped = generated.copy()
            for i in range(len(generated)):
                coped[i] += possible[i]
            compressed = compress(coped)
            if compressed not in saved:
                saved.append(compressed)
                collected.append(coped)
    cache[amount] = collected
    return collected
            
        
if __name__ == "__main__":
    denominations = [1, 2, 5, 10, 20, 50, 100, 200]
    print(len(collect(denominations,200)))
