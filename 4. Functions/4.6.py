def sum_seq(sequence):
    result = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            result += sum_seq(i)
        else:
            result += i
    return result


sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]

print(sum_seq(sequence))
