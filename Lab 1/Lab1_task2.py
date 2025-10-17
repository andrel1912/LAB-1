import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
# Huvudprogrammet (Man skriver in filen du vill ska läsas)

filnamn = input("Ange filnamn:")

# Läser in dna-filen 

with open(filnamn, encoding='utf-8') as f:
    sekvenser = []
    namn = ""
    sekvens = ""

    for rad in f:
        rad = rad.strip()
        if not rad:
            continue # hoppa över tomma
        
        if rad.startswith(">"):
            if namn != "":
                sekvenser.append((namn, sekvens.upper()))
            namn = rad[1:]
            sekvens = ""
        else:
            sekvens += rad # lägg till raden i sekvensen


    if namn != "":
        sekvenser.append((namn, sekvens.upper()))

                    

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
    plt.bar(baser.keys(), baser.values(), color = "r", edgecolor="black")
    plt.title (f"DNA-analys: {namn}")
    plt.xlabel("Bas")
    plt.ylabel("Antal")
    plt.show()

print("Analys Klar")