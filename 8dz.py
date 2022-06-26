# задачи 4-5-6
# from abc import ABC, abstractclassmethod
# from uuid import  uuid4
#
#
# class WarehouseOrgtechnik:
#     def __init__(self,size):
#         self.size = size
#         self.zapas = {}
#
#     def Priem_na_sklad(self,orgtechnik):
#         if orgtechnik.__class__ in self.zapas:
#             self.zapas[orgtechnik.__class__] += 1
#         else:
#             self.zapas[orgtechnik.__class__] = 1
#
#     def Otgruzka_So_Sklada(self,name,val: int):
#         try:
#             if self.zapas[name] >= val:
#                 self.zapas[name] -= val
#             else:
#                 print ("На складе нет", name, "в таком количестве, есть: ", self.zapas[name])
#                 c =1
#         except TypeError as err:
#             print("Недопустимое значение количества техники для отгрузки")
#         except KeyError as err:
#             print('Подобной техники нет на складе')
#
#
# class Orgtechnic(ABC):
#     def __init__(self,ves,razmer):
#         self.ves = ves
#         self.razmer = razmer
#
#
# class Printer(Orgtechnic):
#     def __init__(self, ves, razmer, skorost_pechati):
#         super().__init__(ves,razmer)
#         self.skorost_pechati = skorost_pechati
#         self.PrinterNumber = uuid4()
#
# class Skanner(Orgtechnic):
#     def __init__(self, ves, razmer, skorost_skana):
#         super().__init__(ves,razmer)
#         self.skorost_skana = skorost_skana
#         self.SkannerNumber = uuid4()
#
# class Xerox(Orgtechnic):
#     def __init__(self, ves, razmer, skorost_koprovania):
#         super().__init__(ves,razmer)
#         self.skorost_koprovania = skorost_koprovania
#         self.XeroxNumber = uuid4()
#
#
# Xero = Xerox(10, 'bolshoi', 'быстрая')
# Ska = Skanner (7, "srednii", 'nizko')
# с=1
# skl = WarehouseOrgtechnik(10000)
# skl.Priem_na_sklad(Xero)
# skl.Priem_na_sklad(Xero)
# skl.Priem_na_sklad(Ska)
# c=1
# skl.Otgruzka_So_Sklada(Xero.__class__, 2)
# c=1


# 7 задача

# class KompleksChislo:
#     def __init__(self,veshestv: int,mnimoe: int):
#         self.veshestv = veshestv
#         self.mnimoe = mnimoe
#
#     def __add__(self, other):
#         veshestv = self.veshestv + other.veshestv
#         mnimoe = self.mnimoe + other.mnimoe
#         return KompleksChislo(veshestv, mnimoe)
#
#     def __str__(self):
#         if self.mnimoe > 0:
#             return f"{self.veshestv} + {self.mnimoe}i"
#         else:
#             return f"{self.veshestv} {self.mnimoe}i"
#
#     def __sub__(self, other):
#         veshestv = self.veshestv - other.veshestv
#         mnimoe = self.mnimoe - other.mnimoe
#         return KompleksChislo(veshestv, mnimoe)
#
#     def __mul__(self, other):
#         veshestv = self.veshestv * other.veshestv - self.mnimoe * other.mnimoe
#         mnimoe = self.veshestv * other.mnimoe + other.veshestv * self.mnimoe
#         return KompleksChislo(veshestv, mnimoe)
#
#
# chislo = KompleksChislo(5, 7)
# chislo2 = KompleksChislo(10,20 )
# print(chislo - chislo2)


# proverka raboti git


