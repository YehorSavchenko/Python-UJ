import itertools
import random

# 1
iter_zeros3 = itertools.cycle([0, 1])

# 2
it = (random.choice(("N", "E", "S", "W")) for _ in iter(int, 1))

# 3
iter_zeros4 = itertools.cycle([0, 1, 2, 3, 4, 5, 6])
