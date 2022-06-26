# 1 задача

# class Matrix:
#     def __init__(self,lis):
#         if type(lis) == list:
#             for el in lis:
#                 if type(el) == list:
#                     for element in el:
#                         if type(element) == int:
#                             continue
#                         else:
#                             raise ValueError('Не верный формат')
#                 else:
#                     raise ValueError('Не верный формат')
#             self.lis = lis
#         else:
#             raise ValueError('Не верный формат')
#
#     def __str__(self):
#         answ = list()
#         for listiki in self.lis:
#             stroka = ''
#             for elements in range(len(listiki)):
#                 stroka += str(listiki[elements])
#                 stroka += ' '*(5-len(str(listiki[elements])))
#             answ.append(stroka)
#         itog = '\n'.join(answ)
#         return itog
#
#     def __add__(self, other):
#         if len(self.lis) != len(other.lis):
#             raise ValueError('Размер суммтруемых матриц не совпадает!!!')
#         for num in range(len(self.lis)):
#             if len(self.lis[num]) != len(other.lis[num]):
#                 raise ValueError('Размер суммтруемых  матриц не совпадает!!!')
#         add = list()
#         for num in range(len(self.lis)):
#             add1 = list()
#             for num1 in range(len(self.lis[num])):
#                 add1.append(self.lis[num][num1]+other.lis[num][num1])
#             add.append(add1)
#         return Matrix(add)
#
# тесты (ахах
#        )
# l=[[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21]]
# m = Matrix(l)
# print(m)
#
# print('')
#
# l1 = [[22,23,24,25,26,27,28],[29,30,31,32,33,34,35],[36,37,38,39,40,41,42]]
# n= Matrix(l1)
# print(n)
# print('')
# print(m+n)
# print('')
# print(m+n+n)


# 2 задача (не решил)

# class Wear:
#     koef = 0
#     def __init__(self,name):
#         if type(name) != str:
#             raise ValueError('не верный формат названия')
#         else:
#             self.name = name
#
#
#
# class Palto(Wear):
#     def __init__(self,name,V):
#         super().__init__(name)
#         if type(V) != int:
#             raise ValueError('не верный формат размера')
#         self.V = V
#     @property
#     def rashod_tkani(self):
#         rash = self.V/6.5+0.5
#         return rash
#
#
# class Suit(Wear):
#     def __init__(self,name,H):
#         super().__init__(name)
#         if type(H) != int:
#             raise ValueError('не верный формат размера')
#         self.H = H
#     @property
#     def rashod_tkani1(self):
#         rash = self.H*2 + 0.3
#         return rash
#
# m= Suit('пальто',110)
# c=1
# n=Suit('костюм', 60)
# c=1
# k=Palto('костюм', 60)
# c=1
# print(Wear.koef)




# 3 задача

# class Kletka:
#     def __init__(self,numb):
#         self.numb = numb
#
#     def __add__(self, other):
#         return Kletka(self.numb + other.numb)
#     def __sub__(self, other):
#         if self.numb == other.numb:
#             print('вычитание невозможно. клетки равны')
#             return None
#         else:
#             return Kletka((self.numb - other.numb)*(2*(self.numb > other.numb)-1))
#
#     def __mul__(self, other):
#         return Kletka(self.numb * other.numb)
#
#     def __truediv__(self, other):
#         return Kletka(max(self.numb,other.numb)//min(self.numb,other.numb))
#
#     def make_order(self,long):
#         mo = ''
#         for el in range(self.numb//long):
#             mo += '*' * long
#             mo += '\n'
#         mo += '*' * (self.numb%long)
#         return mo
#
# m= Kletka(12)
# n=Kletka(40)
# c= m - n
# c=1
# c= m/n
# c=1
#
# print(n.make_order(12))
# print(m.make_order(5))
