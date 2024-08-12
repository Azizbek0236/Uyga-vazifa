from os import system
system("cls")

def cls(son):
    son = str(son)
    natija = {}

    for i in son:
        if i in natija:
            natija[i] += 1
        else:
            natija[i] = 1

    for i in sorted(natija):
        print(f"{i} - {natija[i]}")

son = int(input("Son kiriting: "))
cls(son)