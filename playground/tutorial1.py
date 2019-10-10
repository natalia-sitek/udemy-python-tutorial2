a = "kurczaczek"
b = 10
c = float(20)

print('%s %d %.2f' % (a, b, c))

x = 10 / 3
print(x)

tablica = [7, 9, 99]
tablica.append(1)
tablica.append(2)
tablica.append(3)
print(tablica)

suma = 1 + 2 * 3 / 4.0
print(suma)

print(11 % 3)

kwadrat = 7 ** 2
szescian = 2 ** 3
print(kwadrat)
print(szescian)

witajswiecie = "witaj" + "swiecie"
print(witajswiecie)

wielewitaj = "witaj" * 10
print(wielewitaj)

print(['kokoszka'] * 3)

imię = "Marek"
nazwisko = "Stec"
# print("Witaj,%s %s" % (imię,nazwisko)) - #komentarz
print("Witaj,%s" % imię + " " + nazwisko)
# " " - spacja

imie2 = "Janusz"
wiek = 24
krotka = (imie2, wiek)
print("%s ma %d lata" % krotka)
wiek = 25
print("%s ma %d lata" % krotka)

tab = [1, 2]
print("%d - %d" % (tab[0], tab[1]))
tab[0] = 200
print("%d - %d" % (tab[0], tab[1]))
