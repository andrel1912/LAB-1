import matplotlib.pyplot as plt

# Huvudprogrammet (Man skriver in filen du vill ska läsas)

filnamn = input("Ange filnamn:")

# Läser in dna-filen 
with open(filnamn, encoding="utf-8") as f:
    rader = [rad.strip() for rad in f if rad.strip()] # Den här delen är till för att ta bort tomma rader
    sekvenser = [(rader[i][1:], rader[i+1].upper()) for i in range(0, len(rader), 2)]

    print ("/nResultat av DNA-analys/n")

    # Analyserar sekvenserna
    for namn, sekvens in sekvenser:
        # Räknar baser
        baser = 