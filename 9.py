"""
A Pythagorean triplet is a set of three natural numbers,
a < b < c, for which:
    a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 5^2

There exists exactly one Pythagorean triplet for which.
a + b + c = 1000
Find the product abc.
"""
def threesome(m,n):
    return 2 * m * (m + n)

def triplets(m,n):
    return [m**2 - n ** 2, 2 *m *n, m**2 + n**2]

if __name__ == "__main__":
    seed = (0,0)
    for i in range(50):
        for j in range(25):
            if threesome(i,j) == 1000:
                seed = (i,j)
    babies = triplets(*seed)
    product = 1;
    for baby in babies:
        product *= baby
    print(product)
                

