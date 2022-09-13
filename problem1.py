# Victer Phiathep
# RUID : 179005525

import math

def taylors_pi(n):
    pi = 2 * math.sqrt(3)

    # Case for a single term
    if n == 1:
        return pi * (1 - (1/(3*3)))
    else:
        # Variables to keep track of term powers
        terms = 0
        incr = 0

        # Using a for loop to increase our term values
        for x in range(1, n):
            terms += 1/(3**x * (3+incr))
            incr += 2
        return pi * (1 - terms)