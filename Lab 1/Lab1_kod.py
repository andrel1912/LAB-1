import matplotlib.pyplot as plt

# Huvudprogrammet (Man skriver in filen du vill ska läsas)

filnamn = input("Ange filnamn:")

# Läser in dna-filen 

with open(filnamn, encoding="utf-8") as f:
    rader = [rad.strip() for rad in f if rad.strip()] # Den här delen är till för att ta bort tomma rader
    sekvenser = [(rader[i][1:], rader[i+1].upper()) for i in range(0, len(rader), 2)]

    print ("\nResultat av DNA-analys\n")

    # Analyserar sekvenserna
for namn, sekvens in sekvenser:
        
    baser = {b: sekvens.count(b) for b in "ATCG"}

    # Skriver ut resultat för sekvenserna
    
    print(f"Sekvens: {namn}\n Totalt antal baser: {sum(baser.values())}")
    for b, antal in baser.items ():
        print(f" {b}: {antal}")
    print()

    # Diagramet för sekvenserna
    plt.bar(baser.keys(), baser.values(), color = "b", edgecolor="black")
    plt.title (f"DNA-analys: {namn}")
    plt.xlabel("Bas")
    plt.ylabel("Antal")
    plt.show()

print("Analys Klar")

""" 
HJÄLPMEDEL JAG ANVÄNT MIG AV:

- Har använt mig av kursmaterialet vi gått igenom för att göra uppgiften

- https://wwww.youtube.com/watch?v=UBZz6Hh8mY&t=23s: Den här videon hjälpte mig lite grann med chartsen
"""