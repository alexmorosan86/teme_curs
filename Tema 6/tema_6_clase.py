# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()
#
# class Cerc:
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descrie_cerc(self):
#         print(f"Cercul are raza {self.raza} și culoarea {self.culoare}.")
#
#     def aria(self):
#         return 3.14 * self.raza ** 2
#
#     def diametru(self):
#         return self.raza * 2
#
#     def circumferinta(self):
#         return 2 * 3.14 * self.raza
#
# cream un obiect cerc_nou de tip clasa
# cerc_nou = Cerc(5, "alb")
#
# aplema metodele definite in clasa
#
# cerc_nou.descrie_cerc()
# aria_cerc_nou = cerc_nou.aria()
# print(f"Aria cercului este {aria_cerc_nou}.")
# diametru_cerc_nou = cerc_nou.diametru()
# print(f"Diametrul cercului este {diametru_cerc_nou}.")
# circumferinta_cerc_nou = cerc_nou.circumferinta()
# print(f"Circumferinta cercului este {circumferinta_cerc_nou}.")
#
#
#
# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
#
#
# class Dreptunghi:
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descrie(self):
#         print(f"Acesta este un dreptunghi de lungime {self.lungime}, latime {self.latime} și culoare {self.culoare}.")
#
#     def aria(self):
#         return self.lungime * self.latime
#
#     def perimetrul(self):
#         return 2 * (self.lungime + self.latime)
#
#     def schimba_culoarea(self, noua_culoare):
#         self.culoare = noua_culoare
#
# cream un obiect dreptunghi de tip clasa
# dreptunghi = Dreptunghi(5, 5, "rosu")
#
# apelam metodele definite in clasa
#
# dreptunghi.descrie()
# print(f"Aria dreptunghiului este {dreptunghi.aria()}")
# print(f"Perimetrul dreptunghiului este {dreptunghi.perimetrul()}")
# dreptunghi.schimba_culoarea("albastru")
# dreptunghi.descrie()
#
#
# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)
#
#
# class Angajat:
#     # nume = None
#     # Prenume = None
#     # salariu = None
#     an = 12
#
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#
#
#     def descrie(self):
#         print(f'Acest angajat are numele {self.nume} {self.prenume} si are  un salariu de {self.salariu} ron.')
#
#     def nume_complet(self):
#         print(f'Numele complet al angajatului este {self.nume} {self.prenume} .')
#
#     def salariu_lunar(self):
#         print(f'Salariul lunar al angajatului este de {self.salariu}/ luna.')
#
#     def salariu_anual(self):
#         return 12 * self.salariu
#
#     def marire_salariu(self, procent):
#         self.salariu *= (1 + procent / 100)  #aplicam la  salariu un procent  10 %
#
#
# cream un obiect angajat de tip clasa
# angajat = Angajat('Alex', 'Morosan', 1000)
#
# apelam metodele definite in clasa
#
# angajat.descrie()
# angajat.nume_complet()
# angajat.salariu_lunar()
# angajat.salariu_anual() * 12
# print(f"Salariul anual al angajatului este {angajat.salariu_anual()} lei.")
# angajat.marire_salariu(10) # aplicam procentul de 10 %
# angajat.descrie()  # apelam din nou metoda de descriere pentru a afisa salariul marit
#
#
# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)
#
# class Cont:
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#
#
#     def afisare_sold(self):
#         print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} ron.')
#
#     def debitare_cont(self, suma):
#         if suma > self.sold:
#             print('Fonduri insuficiente.Adresati-va bancii.')
#         else:
#             self.sold -= suma
#             print(f"A fost debitată suma de {suma} lei din contul {self.iban}.")
#
#     def creditare_cont(self, suma):
#         self.sold += suma
#         print(f"A fost creditată suma de {suma} lei în contul {self.iban}.")
#
# cont = Cont('Ro12121142435435454', 'Alex Morosan', 3000 ) # cream un obiect cont de tip Clasa
#
#
# apelam metodele definite in clasa
#
# cont.afisare_sold()
# cont.debitare_cont(1000)
# cont.afisare_sold()
# cont.creditare_cont(2000)
# cont.afisare_sold()
#
#
#
#
#
