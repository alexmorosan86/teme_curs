# 1. Funcție care primește o lună din an și returnează câte zile are acea luna


# luna = input('Introduceti o luna din an: ')
# def numar_zile(luna):
#     zile_luna = {
#         "ianuarie": 31,
#         "februarie": 28,
#         "martie": 31,
#         "aprilie": 30,
#         "mai": 31,
#         "iunie": 30,
#         "iulie": 31,
#         "august": 31,
#         "septembrie": 30,
#         "octombrie": 31,
#         "noiembrie": 30,
#         "decembrie": 31
#     }
#     if luna in zile_luna:
#         return zile_luna[luna]
#     else:
#         return None
# print('Luna are', numar_zile(luna) , 'zile')

#
# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
#
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)


# a= int(input('Introduceti nr a: '))
# b= int(input('Introduceti nr b: '))
# def calculator(a, b):
#     suma = a + b
#     diferenta = a - b
#     inmultirea = a * b
#     impartirea = a / b
#     return suma, diferenta, inmultirea, impartirea
#
# a, b, c, d = calculator(a, b)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

# . Funcție care primește 3 numere. Returnează valoarea maximă dintre ele


# a= int(input('Introduceti nr a: '))
# b= int(input('Introduceti nr b: '))
# c= int(input('Introduceti nr c: '))
#
# def maxim_trei(a, b, c):
#     return max(a, b, c)
#
# maxim = maxim_trei(a, b, c)
# print(f'Numarul maxim din cele trei numere introduse este:' , (maxim))



# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
# numerele comune

# lista1 = [1, 2, 3, 4, 5]
# lista2 = [2, 3, 4, 6, 8, 10]
#
#
# def numere_comune(lista1, lista2):
#     comune = []
#     for numar in lista1:
#         if numar in lista2 and numar not in comune:
#             comune.append(numar)
#     return comune
#
#
# comune = numere_comune(lista1, lista2)
# print(comune)


# 2.. Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
# invalidă.

# pret_initial = int(input('Introduceto pretul initial: '))
# reducere = int(input('Introduceto reducerea pe care doriti sa o aplicati in procente: '))
#
# def aplicare_reducere(pret_initial, reducere):
#     if reducere >= 100:
#         return "Reducerea este invalida!"
#     else:
#         pret_final = pret_initial * (1 - reducere / 100) #reducere de 10 %
#         return pret_final
#
#
# pret_final = aplicare_reducere(pret_initial, reducere)
# print(f'Pretul dupa aplicare reducerii este de :', (pret_final))

# 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)

# import datetime
# # pytz este o biblioteca ce lucreaza cu fusurile orare din intreaga lume
# import pytz
#
#
# def data_ora_curenta():
#     zona_orara = pytz.timezone('Europe/Bucharest')
#     data_ora = datetime.datetime.now(zona_orara)
#     return data_ora.strftime('%d-%m-%Y %H:%M:%S')
#
#
# print(f'Data si ora curenta in Romania este', (data_ora_curenta()))
#
#
# def data_ora_curenta():
#     zona_orara = pytz.timezone('Asia/Shanghai')
#     data_ora = datetime.datetime.now(zona_orara)
#     return data_ora.strftime('%d-%m-%Y %H:%M:%S')
#
#
# print(f'Data si ora curenta in China este', (data_ora_curenta()))
#
#
# def data_ora_curenta():
#     zona_orara = pytz.timezone('Europe/London')
#     data_ora = datetime.datetime.now(zona_orara)
#     return data_ora.strftime('%d-%m-%Y %H:%M:%S')
#
#
# print(f'Data si ora curenta in Anglia este', (data_ora_curenta()))


