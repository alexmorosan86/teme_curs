# 1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
# Un if else evalueaza niste conditii daca sunt adevrate sau false, de exemplu daca conditia A este True,
# printeaza ceva, daca este False printeaza altceva

# 2. Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural
# daca este numar intreg mai mare ca 0)

#
# x = int(input("Introduceți un număr: "))
# if x > 0 and x == int(x):
#   print(x, "este un număr natural.")
# else:
#   print(x, "nu este un număr natural.")


# 3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

#
# x = int(input("Introduceți un număr: "))
# if x > 0 :
#      print(x, "este un număr pozitiv.")
# elif x == 0:
#      print(x, " este un număr neutru.")
# else:
#      print(x, " este un număr negativ.")

# 4.Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).


# x = int(input("Introduceți un număr: "))
#
# if -2 <= x <=13:
#     print(x, " se afla intre intervalul -2 si 13")
# else:
#     print(x, " nu  se afla intre intervalul -2 si 13")

# 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
# cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
# abs

# x = int(input('Introduceti primul numar: '))
# y = int(input('Introduceti al doilea numar: '))
#
# if abs(x - y) < 5:
#     print("Diferența dintre x și y este mai mică de 5.")
# else:
#     print("Diferența dintre x și y nu este mai mică de 5.")

# 6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)

# x = int(input("Introduceți un număr: "))
#
# if not(5 <= x <= 27):
#     print(x," NU se află între 5 și 27.")
# else:
#     print(x," se află între 5 și 27.")

# 7. Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
# daca nu, afiseaza care din ele este mai mare

# x = int(input("Introduceți un număr: "))
# y = int(input("Introduceți un număr: "))
#
# if x == y:
#     print('Numerele sunt egale')
# elif x > y:
#     print(str(x) + ' este mai mare decat '+ str(y))
# else:
#     print('Nici o conditie nu este adevarata si intra in else')

# 8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
# triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
# oarecare (nicio latura nu e egala).

# x = int(input("Introduceți un număr : "))
# y = int(input("Introduceți un număr: "))
# z = int(input("Introduceți un număr: "))
#
# if z != x and x == y:
#     print('Triunghiul este isoscel')
# elif x == y == z:
#     print('Triunghiul este echilateral')
# else:
#     print('Este un triunghi oarecare')

# 9.Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
# Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

# letter = input("Introduceți o literă: ")
#
# if letter.lower() in 'aeiou':
#     print("Litera este o vocală.")
# elif letter.upper() in 'aeiou':
#     print("Litera este o vocală.")
# else:
#     print("Litera nu este o vocală.")

# 10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum
# urmeaza:
# a. Peste 9 => A
# b. Peste 8 => B
# c. Peste 7 => C
# d. Peste 6 => D
# e. Peste 4 => E
# f. 4 sau sub => F

# nota = float(input("Introduceți nota din sistemul românesc: "))
#
# if nota >= 9:
#     nota_american = 'A'
# elif nota >= 8:
#     nota_american = 'B'
# elif nota >= 7:
#     nota_american = 'C'
# elif nota >= 6:
#     nota_american = 'D'
# elif nota >= 4:
#     nota_american = 'E'
# else:
#     nota_american = 'F'
#
# print("Nota în sistemul american este:", nota_american)