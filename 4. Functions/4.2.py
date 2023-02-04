# Zadanie 3.5
def func_miarka():
    dlugosc = int(input("Prosze podac dlugos(liczba int)= "))
    string = ""
    for item in range(dlugosc):
        string += "|...."
    string = string + '|\n'
    for e in range(dlugosc + 1):
        if e < 9:
            string += f"{e}    "
        elif e < 99:
            string += f"{e}   "
        else:
            string += f"{e}  "
    return string


print(func_miarka())


# Zadanie 3.6
def func_squares():
    height, length = int(input("Wysokosc: ")), int(input("Szerokosc: "))
    square = ""
    for h in range(height):
        for l in range(length):
            square += "+---"
        square += "+\n"
        for l in range(length + 1):
            if l == length:
                square += "|\n"
                continue
            square += "|   "
    for l in range(length + 1):
        if l == length:
            square += "+\n"
            break
        square += "+---"
    return square


print(func_squares())
