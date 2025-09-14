## Failed I had no idea about reservoir sampling but I learnt something new, so now I am going to try build the solution based on my understanding
## Success on creating the solution based upon what I learnt

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

import random
from collections import defaultdict


def problem(stream):
    reservoir = 0

    for i, val in enumerate(stream):
        if i == 0:
            reservoir = val
        else:
            if random.randint(0, i) == 0:
                reservoir = val

    return reservoir

if __name__ == "__main__":
    sample = 1000000
    test = defaultdict(int)

    for _ in range(sample):
        test[problem([1,2,3,4,5,6,7,8,9,10])] += 1

    print(test)