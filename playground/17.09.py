# pierwsze = [2,3,5,7]
# for x in pierwsze:
#   print (x)

# for x in range(20):
#  print("iteration: %d" % x)
# if x % 2 !=0: #liczba nieparzysta
#    print("liczba nieparzysta - skippujemy")
#   break
#  print(x)

def dzielenie(dzielna, dzielnik):
    print("dzielmy")
    if (dzielnik == 0):
        return  # zakoncz funkcje nic nie zwracajac
    else:
        return dzielna / dzielnik


# x=dzielenie(12,2)
# print(x)

class Cat:
    type = "Cat"

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def sayHello(self):
        print("Hi! My name is %s" % self.name)

    def getColor(self):
        return self.color


c = Cat("brown", "Felix")


class Auto:
    marka = ""
    kolor = ""

    def wyswietlspecyfikacje(self):
        print("marka: %s kolor: %s" % (self.marka, self.kolor))


auto = Auto()
auto.kolor = "czerwony"
auto.marka = "Kia"

auto.wyswietlspecyfikacje()
