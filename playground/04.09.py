imie = "Jan"
wiek = 23
# usercorrect= imie=="Jan10" and wiek==23
usercorrect = imie == "Jan10" or wiek == 23

if usercorrect:
    print("jest ok")
    print("jest very ok")
else:
    print("nok")
    print("zle100")

print("cd")

imie = "Robert"
imiona = ["Jan", "Zbigu"]
zapasowe_imiona = ["normanów", "mistrzow"]
if imie in imiona:
    print("jest w pierwszej tablicy")
elif imie in zapasowe_imiona:
    print("jest w zapasowej tablicy")
else:
    print("nie ma go")

# imiona.append("Robert")
if imie in imiona:
    print("git")
else:
    print("jak to")

if imie not in imiona:
    print("nie ma roberta")
