def flatten(sequence):
    result = []
    if isinstance(sequence, (list, tuple)):
        for item in sequence:
            if isinstance(item, (list, tuple)):
                for tp in flatten(item):
                    result.append(tp)
            else:
                result.append(item)
        return result
    else:
        result.append(sequence)
        return result


seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(flatten(seq))
