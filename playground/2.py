rzeczywista_1 = 7.34
rzeczywista_2 = 84.432
calkowita = 16

print(rzeczywista_1 + rzeczywista_2)

rzeczywista_1 = 4.34
rzeczywista_2 = 54.432
calkowita = 15555

print("rzeczywista_1 = %f" % rzeczywista_1)
print("rzeczywista_2 = %f" % rzeczywista_2)
print("rzeczywista_2 = %.1f" % rzeczywista_2)
print("W systemie szesnastkowym %d ma postac %X" % (calkowita, calkowita))

dane = ("Jacek", "Darek", 44.4)
formatowany_napis = "Czesc %s i %s.Temperatura na zewnątrz wynosi %.1f stopnie Celsjusza."
print(formatowany_napis % dane)

print("Nigdy nie czytalem \"Potopu\".")

print("%d %%" % 1)

a = 'dom'
print(len(a))

napis = "abcdeabcde"
print(napis.index("dea"))
print(napis.index("d"))

napis1 = "AAA BBB"
napis1.find("B")
print(napis1.find("B"))
print(len(napis1))

napis = "Witaj"
print(napis.upper())
print(napis.lower())

napis = "Ala ma nogi"
print(napis.split(" "))

print(len(napis))

wiek = input("podaj wiek:")
imie = input("podaj imie:")

if (wiek.isnumeric()):
    print("masz %s lat i na imię %s" % (wiek, imie))
else:
    print("źle!")

    tablica = []
    liczba = input("podaj pierwszą liczbę:")
    tablica.append(liczba)
    liczba = input("podaj drugą liczbę:")
    tablica.append(liczba)
    tablica.append(input("podaj trzecią liczbę:"))
    print("zawartość tablicy: %s" % tablica)
    index = input("którą liczbę pobrać?")
    liczba = tablica.pop(int(index))
    print("pobrano: %s" % liczba)
    print("zawartość tablicy: %s" % tablica)

    x = 2
    # print x == 2  # wypisze True
#  print x != 2  # wypisze False ! = to "różne od"
#  print x == 3  # wypisze False
# print x < 3  # wypisze True
