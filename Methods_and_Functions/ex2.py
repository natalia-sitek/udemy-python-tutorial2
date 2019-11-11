def animal_crackers(text):
    words = text.split()
    first = words[0]
    second = words[1]
    return first[0].lower() == second[0].lower()


print(animal_crackers("Leon ldon"))


def old_macdonald(name: str):
    return name[0:3].capitalize() + name[3:].capitalize()


def makes_twenty(n1, n2):
    return n1 == 20 or n2 == 20 or n1 + n2 == 20


def master_yoda(text):
    return " ".join(reversed(text.split()))
