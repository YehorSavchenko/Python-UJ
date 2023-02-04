def fibonacci(n):
    if n < 0:
        print("The number cannot be negative")
        quit()
    if n == 1 or n == 2:
        return 1
    prev_n = 1
    prev_n2 = 1
    try:
        for i in range(2, n):
            temp = prev_n2
            prev_n2 = prev_n
            prev_n = temp + prev_n
        return prev_n
    except TypeError:
        print("The number cannot be with comma")
        quit()


print(fibonacci(10))
