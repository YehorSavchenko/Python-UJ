dictonary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
dictonary2 = {}
dictonary2['I'] = 1
dictonary2['V'] = 5
dictonary2['X'] = 10
dictonary2['L'] = 50
dictonary2['C'] = 100
dictonary2['D'] = 500
dictonary2['M'] = 1000
rzym = input("Cyfra rzymska: ")
if rzym not in dictonary:
    print("Niepoprawna liczba")
    quit()
print("Ta cyfra w systemie arabskim: ", dictonary[rzym])
