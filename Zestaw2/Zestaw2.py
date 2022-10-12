# Zadanie 2.10
print("\nZadanie 2.10")
line = "Lorem \t ipsumdolor sit \n amet GvR consectetur elit. \n Proinbibendum " \
       "egestas \t\n pellentesquemauris Integer \tfeugiatipsum " \
       "ut \t\tligula ullamcorper \nquisplaceratmetusvehicula."
print(line.split())
print("Liczba wyrazow =", len(line.split()))

# Zadanie 2.11
print("\nZadanie 2.11")
word = "word"
print("_".join(word))

# Zadanie 2.12
print("\nZadanie 2.12")
start = line[:9]
end = line[-1:-9:-1]
print("Pierwszy znaki: " + start)
print("Ostatni znaki: " + end)

# Zadanie 2.13
print("\nZadanie 2.13")
dlugosc = [len(l) for l in line.split()]
print(sum(dlugosc))

# Zadanie 2.14
print("\nZadanie 2.14")
max_wyraz = line.split()[dlugosc.index(max(dlugosc))]
print("a: " + max_wyraz)
print("b:", len(max_wyraz))

# Zadanie 2.15
print("\nZadanie 2.15")
L = [3, 6, 12, 667, 23, 12, 43, 32, 34]
S = ' '.join(str(e) for e in L)
print(type(S), S)

# Zadanie 2.16
print("\nZadanie 2.16")
print(line.replace("GvR", "Guido van Rossum"))

# Zadanie 2.17
print("\nZadanie 2.17")
print("Alfabetycznie:", sorted(line.lower().split()))
print("Dlugosci:", sorted(line.lower().split(), key=len))

# Zadanie 2.18
print("\nZadanie 2.18")
liczba = 120032302323023003204
print(liczba.__str__().count('0'))

# Zadanie 2.19
print("\nZadanie 2.19")
Lista = [3, 23, 543, 45, 123, 5, 6, 87, 674]
print(' '.join(str(e).zfill(3) for e in Lista))
