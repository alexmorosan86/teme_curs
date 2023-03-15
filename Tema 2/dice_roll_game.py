# 2. Joc de noroc
# - Cauta pe net si vezi cum se genereaza un numar random
# - Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
# Numarul salvat va fi generat random cu metoda gasita in online
# - Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
# - Verifica si afiseaza daca utilizatorul a ghicit numarul
# - Vor exista 3 optiuni care vor trebui tratate:
# ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# ● Ai ghicit. Felicitari? Ai ales x si zarul a fost y


import random

dice_roll = random.randint(1, 6) # generam un nr de la 1 la 6

numar_jucator = int(input("Introduceti un numar intre 1-6: "))

if numar_jucator == dice_roll:
    print("Ai ghicit. Felicitari! Ai ales", numar_jucator, "si zarul a fost", dice_roll)
elif numar_jucator < dice_roll:
    print("Ai pierdut. Ai ales un numar mai mic. Ai ales", numar_jucator, "dar a fost", dice_roll)
else:
    print("Ai pierdut. Ai ales un numar mai mare. Ai ales", numar_jucator, "dar a fost", dice_roll)
