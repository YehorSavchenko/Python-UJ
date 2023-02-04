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

print(square)
