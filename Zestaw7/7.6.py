import random


def iter1():
    while True:
        yield 0
        yield 1


def iter2():
    while True:
        yield random.choice(("N", "E", "S", "W"))


def iter3():
    while True:
        for i in range(7):
            yield i


# 1
# Old version
# iter_zeros3 = itertools.cycle([0, 1])

# New version
iter_1 = iter(iter1())
print(next(iter_1))
print(next(iter_1))

# 2
# Old version
# it = (random.choice(("N", "E", "S", "W")) for _ in iter(int, 1))

# New version
it = iter(iter2())
print(next(iter2()))
print(next(iter2()))

# 3
# Old version
# iter_zeros4 = itertools.cycle([0, 1, 2, 3, 4, 5, 6])

# New version
iter_3 = iter(iter3())
for i in range(9):
    print(next(iter_3))
