# 1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

# x = int(input('Introducteti un numar: '))
# if len(str(abs(x))) == 4:
#     print(f'{x} are 4 cifre ' )
# else:
#     print(f'{x}  nu are 4 cifre ')

# 2. Verifica daca x are exact 6 cifre

# x = int(input('Introducteti un numar: '))
# if len(str(abs(x))) == 6:
#     print(f'{x} are 6 cifre ' )
# else:
#     print(f'{x}  nu are 6 cifre ')

# if x >= 100000 and x <= 999999:
#     print('Numarul ' + str(x) + ' are 6 cifre')
# else:
#     print('Numarul ' + str(x) + ' nu are are 6 cifre')


# x = int(input('Introducteti un numar: '))
#
# if len(str(x)) == 6:
#     print("Numarul are 6 cifre.")
# else:
#     print("Numarul nu are 6 cifre.")

# 3. Verifica daca x este numar par sau impar

# x = int(input('Introducteti un numar: '))
# if x % 2 == 0:
#     print(x, 'este un numar par')
# else:
#     print(x, 'este un numar impar')


# 4. Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre
# ele

# x = int(input("Introduceți un număr : "))
# y = int(input("Introduceți un număr: "))
# z = int(input("Introduceți un număr: "))
#
# if x >= y and x >= z:
#     print(x, 'este cel mai mare numar')
# elif y >= x and y >= z:
#     print(y, 'este cel mai mare numar')
# else:
#     print(z, 'este cel mai mare numar')


# 5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca
# triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de
# 180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat
# lungimea celei de-a treia laturi)

# x = int(input("Introduceți un număr : "))
# y = int(input("Introduceți un număr: "))
# z = int(input("Introduceți un număr: "))
#
# if x + y + z == 180:
#     print("Triunghiul este valid")
# elif x + y > z:
#     print("Triunghiul este valid")
# else:
#     print("Triunghiul nu este valid")

# sau
#
# if (x + y > z) and (x + z > y) and (y + z > x):
#     print("Triunghiul este valid")
# else:
#     print("Triunghiul nu este valid")

# 6. Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de
# la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă
# ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the
# smarte'

# text = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input('Introducteti un numar: '))
# print((text[:-x]))

# 7. Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format
# din primele 5 caractere + ultimele 5

# text = 'Coral is either the stupidest animal or the smartest rock'
# string_nou = text[:5] + text[-5:]
# print(string_nou)


# 8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
# indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
# (hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
# afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
# animal or the smartest '

# text = 'Coral is either the stupidest animal or the smartest rock'
# index = text_nou.index("rock")
# print(text_nou[:index])

# 9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se
# va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
# e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o
# functie pentru a face string-ul case insensitive)

# text = input('Introduceti un text: ')
# text_nou = text.casefold()
# assert text_nou[0] == text_nou[-1], ' Eroare Primul si ultimul caracter nu  sunt la fel'
# print('Primul caracter si ultimul sunt la fel')


# 10. Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)
#
# text = '0123456789'
#
# print('Numere pare din text sunt : ' + text[0::2])
# print('Numere impare din text sunt : ' + text[1::2])


# Exerciții Bonus
# 1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
# inputuri urmatoarele informatii:
# a. Varsta
# b. Insotit de mama
# c. Insotit de tata
# d. Pasaport
# e. Act permisiune mama
# f. Act permisiune tata
# Conditii de imbarcare:
# 1. Daca pers are varsta peste 18 ani si are pasaport
# 2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# 3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
# si are permisiune in scris de la celalat parinte
#
# Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate
# variantele care crezi ca ar trebui testate. Genereaza scenarii de testare cu expected results si
# apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.
# Exemple:
# 1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# 2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca





# def verificare_imbarcare(varsta, pasaport, insotit_tata, insotit_mama, act_permisiune_mama, act_permisiune_tata):
#     if varsta >= 18 and pasaport:
#         return True
#
#     elif varsta < 18 and pasaport and insotit_tata and insotit_mama:
#         return True
#
#     elif varsta < 18 and (insotit_tata or insotit_tata) and (act_permisiune_mama or act_permisiune_tata):
#         return True
#
#     else:
#         return False
#
# # are peste 18 ani, Nu are pasaport, fara mama, fara tata, fara permisiune mama, fara permisiune tata == Nu poate calatori
# assert verificare_imbarcare(19,False,False,False,False,False) == False
#
# # are sub 18 ani, are pasaport, cu mama, cu tata, fara permisiune mama, fara permisiune tata == Poate calatori
# assert verificare_imbarcare(17,True,True,True, False, False) == True
#
# # are sub 18 ani, are pasaport, cu tata, fara mama, permisiune de la mama, fara permisiune de la tata == Poate calatori
# assert verificare_imbarcare(15, True,True,False,True,False) == True
#
# # are sub 18 ani, are pasaport, fara tata, cu mama, fara permisiune de la mama, cu permisiune de la tata == Poate calatori
# assert verificare_imbarcare(14,True,True,True, False, True) == True
#
# # are sub 18 ani, nu are pasaport, fara tata, cu mama, fara permisiune mama, fara permisiune tata == Nu poate calatori
# assert verificare_imbarcare(16,False,False,True,False,False) == False
# def verificare_imbarcare(varsta, pasaport, insotit_tata, insotit_mama, act_permisiune_mama, act_permisiune_tata):
#     if varsta >= 18 and pasaport:
#         return True
#
#     elif varsta < 18 and pasaport and insotit_tata and insotit_mama:
#         return True
#
#     elif varsta < 18 and (insotit_tata or insotit_tata) and (act_permisiune_mama or act_permisiune_tata):
#         return True
#
#     else:
#         return False
#
# # are peste 18 ani, Nu are pasaport, fara mama, fara tata, fara permisiune mama, fara permisiune tata == Nu poate calatori
# assert verificare_imbarcare(19,False,False,False,False,False) == False
#
# # are sub 18 ani, are pasaport, cu mama, cu tata, fara permisiune mama, fara permisiune tata == Poate calatori
# assert verificare_imbarcare(17,True,True,True, False, False) == True

# are sub 18 ani, are pasaport, cu tata, fara mama, permisiune de la mama, fara permisiune de la tata == Poate calatori
# assert verificare_imbarcare(15, True,True,False,True,False) == True
#
# # are sub 18 ani, are pasaport, fara tata, cu mama, fara permisiune de la mama, cu permisiune de la tata == Poate calatori
# assert verificare_imbarcare(14,True,True,True, False, True) == True
#
# # are sub 18 ani, nu are pasaport, fara tata, cu mama, fara permisiune mama, fara permisiune tata == Nu poate calatori
# assert verificare_imbarcare(16,False,False,True,False,False) == False





