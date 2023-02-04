def factorial(b):
    try:
        int(b)
    except ValueError:
        print("Value error")
        quit()
    if b < 0:
        print("The number cannot be negative")
        quit()
    result = 1
    try:
        for i in range(1, b + 1):
            result *= i
        return result
    except TypeError:
        print("The number cannot be with comma")
        quit()


print(factorial(5))
