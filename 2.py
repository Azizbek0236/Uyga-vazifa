from os import system
system("cls")

def cls(son, mahsulotlar):
    saralangan = sorted(mahsulotlar, key=lambda x: x['price'], reverse=True)
    return saralangan[:son]

mahsulotlar = [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]

son = int(input("Miqdorni kiriting: "))
natija = cls(son, mahsulotlar)
print(natija)