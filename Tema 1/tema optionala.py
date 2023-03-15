1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.

text = input('Introduceti un text impar: ')
lungime = len(text)
mijloc = int(lungime/2)
print('Caracterul din mijloc este: ', text[mijloc])

text = input('Va rugam introduceti un text impar: ')
lungime = len(text)

if lungime % 2 == 1:
    print('Textul este de dimensiune impara.')
    caracter_mijloc = text[len(text) // 2]
    print(f'Caracterul din mijloc este: {caracter_mijloc}')
else:
    print(input('Va rugam introduceti un text impar: '))



2. Folosind assert, verifică dacă un string este palindrom.

text = input('Introduceri un cuvant palindrom: ')
if str(text) == str(text)[::-1] :
    print('Este un palindrom')
else:
    print('Nu este un palindrom')


3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.

text_1, text_2 = input('Introduceti un text format din doua cuvinte: ').split()
# print(text_1, text_2)

4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.

text = input('Introduceti un text: ')
primul_caracter = text[0]
print(primul_caracter)
text_update = primul_caracter + text[1:-1].replace(primul_caracter, primul_caracter.upper()) + text[-1]
print(text_update)

5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****


user_name = input("Please enter a usename: ")
password = input("Please enter a password: ")
password_len = len(password)
password_hide = '*' * password_len
print('Parola pt user ' + user_name + ' este ' + password_hide + ' si are ' + str(password_len) + ' caractere.')








