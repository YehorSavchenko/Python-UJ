while True:
    try:
        x = input()
        if x == "stop":
            break
        print("Result:", float(x), pow(float(x), 3))
    except ValueError:
        print("Value error")
