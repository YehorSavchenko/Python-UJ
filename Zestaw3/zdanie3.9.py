sek = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
result = list(map(sum, sek))
print(result)
assert result == [0, 4, 3, 7, 18]
