import matplotlib.pyplot as plt

# Huvudprogrammet (Man skriver in filen du vill ska läsas)

filnamn = input("Ange filnamn:")

# Läser in dna-filen 
with open(filnamn, encoding="utf-8") as f:
    rader = [rad.strip() for rad in f if rad.strip()] # Den här delen är till för att ta bort tomma rader
    sekvenser = 