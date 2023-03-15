from abc import ABC, abstractmethod


#
#
# class Pisica:
#     nume = None
#     rasa = None
#     varsta = None
#     culoare = None
#
#     def __init__(self, nume, culoare):
#         self.nume = nume
#         self.culoare = culoare
#
#
#     def miauna(self):
#         print(f"Pisica face Miau Miau")
#
#
#     def descriere(self):
#         print(f"Pisica {self.nume} are culoarea {self.culoare}")
#
#
#     def varsta(self, varsta):
#         self.varsta = varsta
#         print(f"Pisica {self.nume}  are varsta de {self.varsta} ani")
#
#
# tom = Pisica('Tom', 'Alb')
#
# tom.miauna()
# tom.descriere()
# tom.varsta(4)
#
# sam = Pisica('sam', 'neagra')
#
# sam.descriere()
# sam.miauna()
# sam.varsta(10)


class FormaGeometrica(ABC):
    PI = 3.14
    culoare = "Alb"

    @abstractmethod
    def aria(self):
        pass

    def descriere(self):
        print("Cel mai probabil am colturi")


class Patrat(FormaGeometrica):
    __latura = None

    # def __init__(self, latura_din_ext):
    #     self.__latura = latura_din_ext

    def aria(self):
        return self.__latura * self.__latura

    def set_latura(self, latura_din_ext):
        if latura_din_ext <= 0:
            print("Latura nu poate fi negativa")
        else:
            self.__latura = latura_din_ext

    def get_latura(self):
        return self.__latura

    def delete_latura(self):
        del self.__latura


patratel = Patrat()
patratel.set_latura(-5)
patratel.set_latura(5)

arie_patratel = patratel.aria()
print(f'Aria patratului e {arie_patratel}')

latura_patratel = patratel.get_latura()

print(f"Latura patratului patratel: {latura_patratel}")

patratel.delete_latura()

print(f"Latura patratului patratel: {patratel.get_latura()}")

patratel.descriere()

class Cerc(FormaGeometrica):
    __raza = None
    culoare = "Rosu"

    def __init__(self, raza_cercului):
        self.__raza = raza_cercului

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza_din_ext):
        if raza_din_ext <= 0:
            print("Raza este prea mica")
        else:
            self.__raza = raza_din_ext

    def delete_raza(self):
        del self.__raza

    def aria(self):
        return self.PI * self.__raza ** 2

    def descriere(self):
        super().descriere()

        print("Eu nu am colturi")

        print(f"Initial am fost {super().culoare} iar acum sunt {self.culoare}")


cerculet = Cerc(5)
cerculet.descriere()
print(f"Aria cercului este {cerculet.aria()}")

