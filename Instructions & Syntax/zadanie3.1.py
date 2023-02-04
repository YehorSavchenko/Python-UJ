# Zadanie 3.1
print("\nZadanie 3.1")
# Ten kod będzie działał, ale przydałoby usunąć średniki i klamry, bo w pythonie tego nie używamy
x = 2
y = 3
if x > y:
    result = x
else:
    result = y

# -----------------------------------------------------
# Tu musi być "enter" po dwukropku pętli
for i in "axby": if ord(i) < 100: print(i)

# -----------------------------------------------------
# Ten kod jest poprawny bo potem idzie polecenie, a nie nowy warunek lub pętlia
# więc można napisać to w jednej linii
for i in "axby": print(ord(i) if ord(i) < 100 else i)
