from os import system
system("cls")

def cls(son):
    count = 0
    for char in son:
        if char == '0':
            count += 1
        else:
            break
    return count

sonlar = ['100', '001', '100100', '001001', '012345679', '0000']
natija = [cls(i) for i in sonlar]
print(natija)
