lista1 = [5, 3, 675, 12, 23, 54, 123123, 34, 56, 76, 324, 122, 3, 4, 63, 23, 5, 856, 12, 34, 54, 65, 12, 12, 54, 234]
lista2 = [2, 123, 675, 12, 23, 54, 3, 896, 908, 5423, 324, 122, 507, 6, 9, 34, 5, 45, 12, 11, 4, 65, 12, 33, 54, 543]
result = []

# a
for e1 in lista1:
    for e2 in lista2:
        if e1 in lista2 and e1 not in result:
            result.append(e1)
result.sort()
print("Zadanie a:", result)
assert result == [3, 4, 5, 12, 23, 34, 54, 65, 122, 324, 675]

# b
result = []
for item in lista1:
    if item not in result:
        result.append(item)
for item in lista2:
    if item not in result:
        result.append(item)
result.sort()
print("Zadanie b:", result)
assert result == [2, 3, 4, 5, 6, 9, 11, 12, 23, 33, 34, 45, 54, 56, 63, 65, 76, 122, 123, 234, 324, 507, 543, 675, 856, 896, 908, 5423, 123123]
