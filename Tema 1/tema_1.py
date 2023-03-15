# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# variabila = este un loc in memoria calculatorului unde putem tine date
#
# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri devariabilă :
#
# - string
# - int
# - float
# - bool

# Observație: Valorile vor fi alese de tine după preferințe.



var_string = 'hello'
var_numar = 100
var_float = 8.75
var_boolean = True



print(var_string)
print(var_float)
print(var_numar)
print(var_boolean)

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.

print(type(var_string))
print(type(var_numar))
print(type(var_float))
print(type(var_boolean))



# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
# aceeași variabilă (suprascriere):
# - Verifică tipul acesteia.


var_float= round((var_float))
print(var_float)

#  5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.

print(f"Alex spune {var_string}.")
print(f"Alex are  {var_numar} de euro.")
print(f"Maria a luat  nota {var_float} la examen.")
print(f"Testarea este faina?{var_boolean}")



# 6. Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.

nume = input("Introducei un nume: ")
prenume = input("introducei un prenume: ")
nume_complet = len(nume) + len(prenume)
print(f'Numele complet are {nume_complet} caractere')

# 7. Citește de la tastatură:
# - lungimea;
# - lățimea.
# Afișează: 'Aria dreptunghiului este x'.


lungime = int(input("Va rog introduceti lungimea: "))
latime = int(input("Va rog introduceti latime: "))
aria = latime * lungime
print(f'Aria dreptunghiului este = {aria}')



#
# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
#
# - afișează de câte ori apare cuvântul 'the';

text = 'Coral is either the stupidest animal or the smartest rock'
text_2 = text.split() # despartim stringul
print(text_2)
print(text_2.count('the')) # printam de cate ori apare cuvantul ''the


#
# 9. Același string.
# ● Inlocuieste  cuvântul 'the' cu 'THE';
# ● Printează rezultatul.

text = 'Coral is either the stupidest animal or the smartest rock'
print(text.replace(' the', ' THE'))

#10 Același string.
# ● Folosiți un assert ca să verificați dacă acest string conține doar numere.


text = 'Coral is either the stupidest animal or the smartest rock'
assert text.isdigit() == True, "Eroare, textul nu contine  doar numere"











