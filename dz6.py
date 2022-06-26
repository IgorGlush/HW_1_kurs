# 1 задача
# решение с использованием листа

# from time import sleep
#
# class TrafficLight:
#     def __init__(self, __color):
#         name_list = ['green', 'yellow', 'red']
#         if __color not in name_list:
#             raise ValueError('wrong color name!!')
#         else:
#             self.__color = __color
#
#     def running (self):
#         name_list = ['green', 'yellow', 'red']
#         if self.__color == name_list[0]:
#             print(name_list[0])
#             sleep(5)
#         elif self.__color == name_list[1]:
#             print(name_list[1])
#             sleep(2)
#             print(name_list[0])
#             sleep(5)
#         while True:
#             print(name_list[2])
#             sleep(7)
#             print(name_list[1])
#             sleep(2)
#             print(name_list[0])
#             sleep(5)
#
#
# two = TrafficLight('yellow')
# two.running()
# c=1
#  2 задача

# class Road:
#     def __init__(self, _leight, _width):
#         self._leight = _leight
#         self._width = _width
#
#     def massa (self):
#         return(self._leight * self._width * 0.025 * 5)
#
# print(Road(20,5000).massa())

# 4 задача

# class Car:
#     def __init__(self, speed, color, name, is_police):
#         # print(type(speed))
#         # self.speed = speed
#         if type(speed) != int:
#             raise ValueError('скорость измеряется в цифрах! ')
#         else:
#             self.speed = speed
#         self.color = color
#         self.name = name
#         if type(is_police) != bool:
#             raise ValueError ('недопустимое значение! можно: True если полиция, False если нет')
#         else:
#             self.is_police = is_police
#         self.is_police = is_police
#
#     def go(self):
#         print('машина поехала')
#
#     def stop(self):
#         print('машина остановилась')
#
#     def turn(self, directions):
#         dict = {'left':"машина повернула налево", "right":"машина повернула направо"}
#         print(dict[directions])
#
#     def ShowSpeed(self):
#         print('скорость: ', self.speed)



# class TownCar(Car):
#     def __init__(self,speed,color,name,is_police):
#         super().__init__(speed,color,name,is_police)
#
#     def ShowSpeed(self):
#         if self.speed > 60:
#             print('Превышение скорости!!!', self.speed)
#         else:
#             super().ShowSpeed()
#
# class WorkCar(Car):
#     def __init__(self,speed,color,name,is_police):
#         super().__init__(speed,color,name,is_police)
#
#     def ShowSpeed(self):
#         if self.speed > 40:
#             print('Превышение скорости!!!', self.speed)
#         else:
#             super().ShowSpeed()
#
#
# class SportCar(Car):
#     def __init__(self,speed,color,name,is_police):
#         super().__init__(speed,color,name,is_police)
#
# class PoliceCar(Car):
#     def __init__(self,speed,color,name,is_police):
#         super().__init__(speed,color,name,is_police)




# c= Car(25,'black' ,'cucumber' ,True)
# n=1
# g=TownCar(62,'white','rumbler',False)
# n=1
# x=WorkCar(55,'white','rumbler',False)
# c.go()
# n=1
# c.turn('left')
# n=1
# c.turn('right')
# n=1
# c.stop()
# n=1
# c.ShowSpeed()
# n=1
# g.ShowSpeed()
# x.ShowSpeed()
# m=1

# 3 задча

# class Worker:
#     def __init__(self, name, surname, position):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = { 'wage' :100000, 'bonus':50000}
#
# class Position(Worker):
#     def __init__(self,name, surname, position):
#         super().__init__(name, surname, position)
#
#     def get_full_name(self):
#         return (f"полное имя: {self.name} {self.surname}")
#
#     def get_total_income(self):
#         total = self._income['wage'] + self._income['bonus']
#         return (f"полный доход за месяц: {total}")
#
#
# c= Worker('ivan','petrov','boss')
# m=1
# d = Position('sergey','ivanov','gey')
# m=1
# print(d.get_full_name())
# m=1
# print(d.get_total_income())
# m=1


# 5 задача
# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         print('Запуск отрисовки')
#
# class Pen(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#
#
#     def draw(self):
#         super().draw()
#         print(f"рисуем используя: {self.title}")
# class Pencil(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#     def draw(self):
#         super().draw()
#         print(f"используется: {self.title}")
#
#
# class Hundle(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#     def draw(self):
#         super().draw()
#         print(f"в качесве инструмента у нас: {self.title}")
#
# d= Pen('ручка')
# d.draw()
# p = Pencil('карандаш')
# p.draw()
# o = Hundle('маркер')
# o.draw()