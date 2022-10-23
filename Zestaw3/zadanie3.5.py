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
print(string)
