##kerület számló függvény, ami nem ad vissza értéket
##ennek pontos neve: eljárás (aminek nincs visszatérési értéke)
def kerulet(o1,o2):  
    print(f'A {teglalapE(o1,o2)} kerülete: {o1+o1+o2+o2}')
    
##terület számolás visszatérési értékkel
##függvény vagy metódus a neve, azoknak amelyeknek van visszatérési értéke (return)

def terulet(a,b):
    return a*b

def negyzetE(a,b):
    if a==b: return True
    else: return False
    
def teglalapE(a,b):
    if a!=b: return "téglalap"
    else: return "négyzet"


oldal1 = int(input("Add meg az egyik oldalt: "))
oldal2 = int(input("Add meg a másik oldalt: "))

##A kerület függvény meghívása, ami nem ad vissza értéket
kerulet(oldal1,oldal2)

##A terület kiszámolása és a visszatérési érték fogadása egy változóba
#t = terulet(oldal1,oldal2)
if negyzetE(oldal1,oldal2): tipus="négyzet"
else: tipus="téglalap"
print(f'A {tipus} területe: {terulet(oldal1,oldal2)}')