from os import system
system("cls")

chap = set('1QAZ2WSX3EDC4RFV5TGB')
ong = set('6YHN7UJM8IK,9OL.0P;/')

def cls(text):
    chap1 = 0
    ong1 = 0
    
    for i in text.upper():
        if i in chap:
            chap1 += 1
        elif i in ong:
            ong1 += 1
    return chap1, ong1

matn = "Salom hammaga 2006-yil Aziz"
chap2, ong2 = cls(matn)
print(f"Chap soni: {chap2}")
print(f"O'ng soni: {ong2}")
