
board = [[0 for _ in range(8)] for _ in range(8)]  
korongok = [] 
    
print("Adja meg a korong pozícióját (sor, oszlop) 1-től 8-ig.")
print("Ha egy meglévő korong helyét adja meg, a korongot eltávolítjuk.")
print("Ha befejezte a műveleteket, nyomjon ENTER-t.")

while True:
        sor = input("Sor száma (ENTER a kilépéshez): ")
        if sor == "":
            break  
        if not sor.isdigit():
                print("Hiba: Kérjük, adjon meg egy számot 1 és 8 között!")
                continue

        sor = int(sor)
        if sor < 1 or sor > 8:
                print("Hiba: A sor értéke 1 és 8 között kell legyen!")
                continue

          
        oszlop = input("Oszlop száma: ")
        if not oszlop.isdigit():
                print("Hiba: Kérjük, adjon meg egy számot 1 és 8 között!")
                continue

        oszlop = int(oszlop)
        if oszlop < 1 or oszlop > 8:
                print("Hiba: Az oszlop értéke 1 és 8 között kell legyen!")
                continue


        if board[sor-1][oszlop-1] == 0: 
                board[sor-1][oszlop-1] = 1  
                korongok.append((sor, oszlop))
                print(f"A korongot sikeresen leraktuk a(z) {sor}. sor, {oszlop}. oszlop helyére.")
        else: 
                board[sor-1][oszlop-1] = 0  
                korongok.remove((sor, oszlop)) 
                print(f"A korongot eltávolítottuk a(z) {sor}. sor, {oszlop}. oszlop helyéről.")

print("\nLerakott korongok pozíciói:")
for korong in korongok:
        print(f"Sor: {korong[0]}, Oszlop: {korong[1]}")
