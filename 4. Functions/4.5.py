def list_reverse_iterative(L, left, right):
    list_copy = L.copy()
    list_copy[left:right + 1] = list_copy[left:right + 1][::-1]
    return list_copy


print(list_reverse_iterative([0, 1, 2, 3, 4, 5], 1, 3))


def list_reverse_recursive(L, left, right):
    list_copy = L.copy()
    if right <= left:
        return list_copy
    else:
        list_copy[left], list_copy[right] = list_copy[right], list_copy[left]
        return list_reverse_iterative(list_copy, left + 1, right - 1)


print(list_reverse_recursive([0, 1, 2, 3, 4, 5], 1, 3))
