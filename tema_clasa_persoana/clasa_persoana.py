# Fa o clasa Persoana care sa aiba:
# - nume,
# - prenume,
# - varsta,
# - CNP,
# field-uri private, cu getter setter pentru fiecare, apoi fa un Student sau Elev care extinde Persoana si sa aiba
# - un Nr matricol
# - un dict in care are notele (Materie: Nota)
# - getter si setter pentru Nr matricol
# - getter pentru nota (functia primeste numele materiei ca parametru si verifica in dict daca exista materia, daca da returneaza nota, altfel afiseaza un mesaj)
# - setter pentru nota (functia primeste 2 parametri: materia si nota pe care le inserezi in dict)
# - o metoda listare_note, care afiseaza numele studentului si notele pe care le are la fiecare materie


class Persoana:
    nume = None
    prenume = None
    varsta = None
    cnp = None

    def __init__(self, nume, prenume, varsta, cnp):
        self.__nume = nume
        self.__prenume = prenume
        self.__varsta = varsta
        self.__cnp = cnp

    def get_nume(self):
        return self.__nume

    def set_nume(self, nume):
        self.__nume = nume

    def get_prenume(self):
        return self.__prenume

    def set_prenume(self, prenume):
        self.__prenume = prenume

    def get_varsta(self):
        return self.__varsta

    def set_varsta(self, varsta):
        self.__varsta = varsta

    def get_cnp(self):
        return self.__cnp

    def set_cnp(self, cnp):
        self.__cnp = cnp


class Student(Persoana):
    def __init__(self, nume, prenume, varsta, cnp, nr_matricol):
        super().__init__(nume, prenume, varsta, cnp)
        self.__nr_matricol = nr_matricol
        self.__note = {}

    def get_nr_matricol(self):
        return self.__nr_matricol

    def set_nr_matricol(self, nr_matricol):
        self.__nr_matricol = nr_matricol

    def get_nota(self, materie):
        if materie in self.__note:
            return self.__note[materie]
        else:
            print(f'Materia {materie} nu a fost gasita')


    def set_nota(self, materie, nota):
        self.__note[materie] = nota

    def listare_note(self):
        print(f'Studentul {self.get_nume()}, {self.get_prenume()} are notele: ')
        for materie, nota in self.__note.items():
            print("{}: {}".format(materie, nota))


s = Student("Morosan", "Alex", 20, "1234567890123", "1234")
s.set_nota("Matematica", 8.4)
s.set_nota("Fizica", 8)
s.listare_note()
# print mesaj daca nu materia nu a fost gasita
print(s.get_nota("Informatica"))

