# 1.Funcție care să calculeze și să returneze suma a două numere


# def suma_numere():
#     a = 5
#     b = 5
#     suma = a + b
#     print(f"Suma celor doua numere este {suma}")
# suma_numere()

# def suma_numere(a, b):
#     suma = a + b
#     print(f"Suma celor doua numere este {suma}")
#
# nr_1 = int(input("Nr_1: "))
# nr_2 = int(input("Nr_2: "))
#
# suma_numere(nr_1, nr_2)


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar


# def numar_par(numar):
#     if numar % 2 == 0:
#         return True
#     else:
#         return False
# numar = int(input("Introduceti un numar: "))
#
# print(numar_par(numar))


# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)


#
# def numar_caractere_nume_complet():
#
#     nume = input("Introduceti nume: ")
#     prenume = input("Introduceti prenume: ")
#     nume_mijlociu = input("Introduceti nume_mijlociu: ")
#     nume_complet = nume + prenume + nume_mijlociu
#     return len(nume_complet)
#
# numar_caractere = numar_caractere_nume_complet()
# print("Numarul total de carcactere din numele complet este: ", numar_caractere)

# 4. Funcție care returnează aria dreptunghiului

# def aria_dreptunghiului(lungime, latime):
#     aria = lungime * latime
#     return aria
#
# aria = aria_dreptunghiului(6, 4)
# print("Aria dreptunghiului este: ", aria)


# def aria_dreptunghiului():
#     lungime = float(input("Introduceți lungimea dreptunghiului: "))
#     latime = float(input("Introduceți lățimea dreptunghiului: "))
#     aria = lungime * latime
#     return aria
# aria = aria_dreptunghiului()
# print("Aria dreptunghiului este:", aria)

# def aria_dreptunghiului():
#     aria = float(input("Introduceti lungime: ")) * float(input("Introduceti latime: "))
#     return aria
#
# aria = aria_dreptunghiului()
# print("Aria dreptunghiului este: ", aria)


# 5. Funcție care returnează aria cercului

# def aria_cercului():
#     raza = float(input("Introduceți raza cercului: "))
#     pi = 3.14
#     aria = raza * pi ** 2
#     return aria
# aria = aria_cercului()
# print("Aria cercului este", aria)

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și Talse dacă nu găsește.

# def cauta_caracter(a, b):
#     return b in a
#
# a = input("Introduceti un text: ")
# b = input("Introduceti carcterul pe care il cautati: ")
#
# if cauta_caracter(a, b):
#     print("Caracterul", b, "se găsește în șirul", a)
# else:
#     print("Caracterul", b, "nu se găsește în șirul", a)


# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y


# def caractere_lower_upper(sir_caractere):
#     numar_caractere_lower = 0
#     numar_caractere_upper = 0
#
#     for caracter in sir_caractere:
#         if caracter.islower():
#             numar_caractere_lower += 1
#         elif caracter.isupper():
#             numar_caractere_upper += 1
#
#     print(f"Nr de caractere lower case este {numar_caractere_lower}")
#     print(f"Nr de caractere upper case este {numar_caractere_upper}")
#
#
# sir_caractere = input("Introduceti un sir de caractere: ")
# caractere_lower_upper(sir_caractere)

#
# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive

# def numere_pozitive(lista):
#     lista_pozitive = []
#     for numar in lista:
#         if numar > 0:
#             lista_pozitive.append(numar)
#     return lista_pozitive
#
#
# lista = [-2, -1, 0, 1, 2]
# lista_pozitive = numere_pozitive(lista)
# print(lista_pozitive)

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

# x = int(input('Introduceti primul numar: '))
# y = int(input('Introduceti al doilea numar: '))
#
# def comparare_numere(x, y):
#     if x > y:
#         print(f"{x} este mai mare decat {y}")
#     elif y > x:
#         print(f"{y} este mai mare decat {x}")
#     else:
#         print("Numerele sunt egale")
#
#
# comparare_numere(x,y)


# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False

# numar = int(input('Introduceti un numar pentru a fi adaugat in set: '))
#
# def adauga_numar_in_set(numar, set_numere):
#     if numar in set_numere:
#         print(f"Nu am adaugat numarul {numar} in set.")
#         return False
#     else:
#         set_numere.add(numar)
#         print(f"Am adaugat numarul nou in set.Acesta este numarul {numar}")
#         return True
#
#
# set_numere = {1, 2, 3,4,5}
# rezultat = adauga_numar_in_set(numar, set_numere)
#
# if rezultat:
#     print(f"Numarul {numar} a fost adaugat cu succes in set")
# else:
#     print(f"Numarul {numar} exista deja in set.")