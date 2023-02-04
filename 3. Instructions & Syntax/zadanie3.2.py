# Zadanie 3.2
print("\nZadanie 3.2")

# L będzie typu None i to już nie będzie dostępu do listy
L = [3, 5, 4]
L = L.sort()

# -----------------------------------------------------
# za dużo wartości do przypisania
x, y = 1, 2, 3

# -----------------------------------------------------
# Krotki(tuple) nie obsługuje przypisywania pozycji
X = 1, 2, 3
X[1] = 4

# -----------------------------------------------------
# Wychodzi za granicę listy
X = [1, 2, 3]
X[3] = 4

# -----------------------------------------------------
# Objekt str nie ma atrybutu 'append'
X = "abc"
X.append("d")

# -----------------------------------------------------
# Nie wystarczaje jeszcze parametru(potęgi) dla funkcji pow
L = list(map(pow, range(8)))
