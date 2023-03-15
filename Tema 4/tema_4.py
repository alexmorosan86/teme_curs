# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
#                                              'Fiat', 'Trabant', 'Opel']


# for i in range(len(masini)):
#     print(f"Masina mea preferata este:{masini[i]}")
#
# # for masina in masini:
# #     print(f"Masina mea preferata este: {masina}")

# i = 0
# while i < (len(masini)):
#     print(f"Masina mea preferata este:{masini[i]}")
#     i += 1



# 2. Aceeași listă:
# Folosește un for else
# În for
#
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.



# masini = ['Audi', 'Volvo', 'Bmw', 'Mercedes', 'Aston Martin', 'Lăstun',
#                                              'Fiat', 'Trabant', 'Opel']
#
# for index, masina in enumerate(masini):
#     if index == 0 or index == len(masini) - 1:
#          (masini[index]) = masina.upper()
# else:
#     print(masini)


# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘


# masini = ['Audi', 'Volvo', 'Bmw', 'Mercedes', 'Aston Martin', 'Lăstun',
#                                             'Fiat', 'Trabant', 'Opel']

# for masina in masini:
#     if masina == "Mercedes":
#         print(f"Am gasit masina dorita de dvs: {masina} ")
#         break
#
#     else:
#         print(f"Am gasit masina : {masina}. Mai cautam.")


# i = 0
#
# while i < len(masini):
#     masina = masini[i]
#     if masina == 'Mercedes':
#         print('Am gasit masina dorita de dvs:', [masina])
#         break
#     else:
#         print(f'Am gasit masina {masina}. Mai cautam.')
#         i += 1
# else:
#     print('Nu am gasit masina dorita.')




# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.


# masini = ['Audi', 'Volvo', 'Bmw', 'Mercedes', 'Aston Martin', 'Lăstun',
#                                             'Fiat', 'Trabant', 'Opel']
#
# for masina in masini:
#     if masina in ['Trabant', 'Lastun']:
#         continue
#     print(f'S-ar putea să vă placă mașina {masina}.')


# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.


# masini = ['Audi', 'Volvo', 'Bmw', 'Mercedes', 'Aston Martin', 'Lăstun',
#                                             'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
#
# for i in range(len(masini)):
#     if masini[i] == 'Lăstun' or masini[i] == 'Trabant':
#         masini_vechi.append(masini[i])
#         masini[i] = 'Tesla'
#
# print("Modele vechi:", masini_vechi)
# print("Modele noi:", masini)


# 6. Având dict:
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.


# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
#
#
#
# buget = 15000
# for masina, pret in pret_masini.items():
#     if pret <= buget:
#         print(f"Pentru un buget de sub {buget} euro puteți alege mașina: {masina}")
#
# print("Toate masinile disponibile sunt:")
# for masina in pret_masini:
#     print(masina)

# 7. Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# i = 0
# for nr in numere:
#     if nr == 3:
#         i += 1
#
# print(f"Numărul 3 apare de {i} ori în lista.")

# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).



# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# suma = 0
#
# for numar in numere:
#     print('Suma numerelor din lsta este:', suma)
#     suma += numar
#
# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# cel_mai_mare = numere[0]
#
# for numar in numere:
#     if numar > cel_mai_mare:
#         cel_mai_mare = numar
#
# print("Cel mai mare număr este:", cel_mai_mare)

# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.


# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
#
# for i in range(len(numere)):
#     if numere[i] > 0:
#         numere[i] = -numere[i]
#
# print("Lista cu numere negative:", numere)