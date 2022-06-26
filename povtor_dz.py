# 1 домашка 1 задача

# a=2344
# b='Hello world'
# c=True
# d=f"{a} {b} {c}"
# print(a)
# print(type(a))
# print(b)
# print(type((b)))
# print(c)
# print(type(c))
# print(d)
# print(type(d))


# 2 задача
# a=int(input('Вводи количество секунд '))
# print (f"{a//3600:02}:{(a%3600)//60:02}:{a%60:02}")

# 3 задача

# a=str(input('вводи число n '))
# print (int(a)+int(a*2)+int(a*3))

# 4 задача

# a=int(input('вводи целое положительное число '))
# c=0
# while a!=1:
#     if a%10>c:
#         c=a%10
#     a=a//10
# print(c)

# 5 задача

# a=int(input('введи выручку фирмы '))
# b=int(input('введи издержки фирмы '))
# if a>b:
#     print(f"прибыль, рентабельность {(a-b)/a*100}%")
#     c=int(input('какая численность сотрудников? '))
#     print(f"прибыль на одного сотрудника {(a-b)/c}")
# elif a<b:
#     print('убыток')
# else:
#     print('точка безубыточности')

# 6 задача

# a=int(input('сколько пробежал в первый день? '))
# b=int(input('какая цель? '))
# cnt=1
# while b>a:
#     a=a*1.1
#     cnt+=1
# print(f"на {cnt} день спортсмен достигнет результата не менее 3 км.")



# 2 домашка 1 задача

# list=[]
# a=53
# list.append(a)
# b="hello world"
# list.insert(0,b)
# c=True
# list.append(c)
# d=5.3
# list.insert(0,d)
# print(type(list[0]))
# print(type(list[1]))
# print(type(list[2]))
# print(type(list[3]))

# 2 задача
#
# list=input('введи элементы списка через пробел ')
# list=list.split(' ')
# if len(list)%2==0:
#     list[::2],list[1::2]=list[1::2],list[::2]
#     print(list)
# else:
#     # konec=list[-1]
#     # del list[-1]
#     list[::2],list[1::2]=list[1::2],list[::2]
#     # list.append(konec)
#     print(list)

# 3 задача
# c=int(input('вводи месяц в виде целого числа '))
# dict={12:'winter',1:'winter',2:'winter',3:'spring',4:'spring',5:'spring',6:'summer',7:'summer',8:'summer',9:'autumn',10:'autumn',11:'autumn',}
# print(dict[c])

# 4 задача

# l=input('вводи ')
# l=l.split()
# for e in l:
#     print(e[:10:])

# 5 задача
# my_list=[7,5,3,3,2]
# c=int(input('вводи цифру '))
# cnt=0
# if c < my_list[-1]:
#     my_list.append(c)
# else:
#     while c<= my_list[cnt]:
#         cnt+=1
#     my_list.insert(cnt,c)
# print(my_list)


# 6 задача
#
# c=int(input("введи 1 если заполняем структуру данных или что угодно если приступаем к аналитике "))
# list=[]
# cnt=0
# while c == 1:
#     name=input('вводи через пробел:номер товара, название, цена, количество, единица измерения ')
#     name=name.split()
#     d= {'название':name[1],'цена':name[2],'количество':name[3],'единица измерения':name[4]}
#     kort=(int(name[0]),d)
#     list.append(kort)
#     c = int(input("введи 1 если заполняем структуру данных или 2 если приступаем к аналитике "))
#     cnt+=1
# an=set()
# an1=set()
# an2=set()
# an3=set()
# for el in range (cnt):
#     an.add(list[el][1]['название'])
#     an1.add(list[el][1]['цена'])
#     an2.add(list[el][1]['количество'])
#     an3.add(list[el][1]['единица измерения'])
# dct={'названия':an,'цены': an1,'количества':an2,'единицы измерения' :an3}
# print(dct)


# 3 домашка

# 1 задача
# def y(a,b,*args):
#     if b==0:
#         c='деление на ноль'
#     else:
#         c=a/b
#     return(c)
# print(y(int(input("вводи первое число ")),int(input("вводи второе число "))))

# 2 задача

# def y(name,surname,year,city,email,tel,**kwargs):
#     l=f"{name} {surname} {year} {city} {email} {tel}"
#     return(l)
# d={"name": "igor",
#    "surname": "glushkov",
#    "year":"1991",
#    "city":"s-pb",
#    "email": "@gmail.com",
# "tel":"nokia"}
# print(y(**d))



# 3 задача

# def my_funk(a,b,c,*args):
#     return (a+b+c-min(a,b,c))
# print(my_funk(int(input("вводи первое число ")),int(input("вводи второе число ")),int(input("вводи третее число "))))



# 4 задача
# 1 способ
# def my_funk(x,y):
#     return(x**y)

# 2 способ
# def my_funk(x,y):
#     cnt=0
#     c=1
#     while cnt>y:
#         c=c/x
#         cnt=cnt-1
#     return(c)

# x=5.0
# y=int(-2)
# print(my_funk(x,y))

# 5 задача

# решение с применением нежелательного global
# summ=0
# def my_f(l):
#     global summ
#     l=l.split()
#     for el in l:
#         if el == 'quit':
#             return(summ)
#         el=int(el)
#         summ+=el
#     print(summ)
#     my_f(input('вводи числа через пробел, когда всё введи quit  '))
#     return(summ)
# print(my_f(input('вводи числа через пробел, когда всё введи quit  ')))
#

# решение через циклы. без функции
# l=input('vvodi ')
# l=l.split(' ')
# summ=0
# while 'quit' not in l:
#     for el in l:
#         el=int(el)
#         summ+=el
#     print(summ)
#     l=input('vvodi ')
#     l=l.split(' ')
# for el in l:
#     if el=='quit':
#         print(summ)
#     else:
#         el=int(el)
#         summ+=el
#



# решение без глобал, но не понятно нафига функция тогда. это просто циклы под функцией
#
#
# def funk():
#     summ=0
#     while True:
#         l=input('vvodi chisla, quit esli stop ')
#         if 'quit' not in l:
#             summ+=sum(map(int,l.split()))
#             print(summ)
#         else:
#             l=l.split()
#             for el in l:
#                 if el == 'quit':
#                     return(summ)
#                     break
#                 else:
#                     el=int(el)
#                     summ+=el
# print(funk())




# 6 задача
#
#
# def funk(l):
#     l=l.split()
#     s=[]
#     for el in l:
#         el=el.capitalize()
#         s.append(el)
#     s=' '.join(s)
#     return (s)
# print(funk(input('input string ')))



# 4 домашка

# 1 задача

# from sys import argv
#
# def ras4et_zp(a,b,c):
#     try:
#         x=int(a)/int(b)+int(c)
#         return (x)
#     except ValueError as err:
#         return ('ошибка: ', err)
# print(ras4et_zp(argv[1],argv[2],argv[3]))


# 2 зачада

# l=[300,2,12,44,1,1,4,10,7,1,78,123,55]

# def spisok(a):
#     m=[]
#     for x in range(len(a)-1):
#         if a[x]>a[x+1]:
#             m.append(a[x])
#     return(m)
# print(spisok(l))


# 3 задача

# a=[x for x in range(20,241) if x%20==0 or x%21==0 ]
# print(a)

# 4 задача

# def funk(l):
#     m=[]
#     for x in range(len(l)):
#         if l.count(l[x])==1:
#             m.append(l[x])
#     return (m)
# list=[2,2,7,23,1,44,44,3,2,10,7,4,11]
# print(funk(list))

# 5 задача

# from functools import reduce
# x=[el for el in range(100,1000) if el%2==0]
# print(reduce(lambda a,b :a*b ,x))

# 6 задача

# from itertools import count
# from itertools import cycle

# for el in count(int(input('вводи число с которого начнем '))):
#     print(el,end='')
#     quit=input()
#     if quit=='q':
#         break


# l=[1,3,5,7,9]
# for el in cycle(l):
#     print(el, end='')
#     quit=input()
#     if quit=='q':
#         break


# 7 задача

# def fact(n):
#     cnt=1
#     m=1
#     while cnt<n:
#         m*=cnt
#         cnt+=1
#         yield (m)
# for el in fact(int(input('вводи число '))):
#     print(el)


# 5 домашка

# 1 задача
#
# with open("7dz_3zad.txt", 'w') as txt:
#     c=input("Enter text ")
#     while c  !=  "":
#         txt.write(c)
#         txt.write("\n")
#         c = input("Enter text ")

# 2 задача

# with open("7dz_povtor.txt",'r') as txt2:
#     c = txt2.readlines()
#     print(f"количество строк равно= {len(c)}")
#     for el in range(len(c)):
#         print(f"Количество слов строки номер {el+1}: {len(c[el].split())}")

# 3 задача

# with open("7dz_3zad.txt",'r') as txt:
#     txt=txt.readlines()
#     sum=0
#     for el in range(len(txt)):
#         m= int((txt[el].split())[1])
#         sum+=m
#         n=(txt[el].split())[0]
#         if m < 20000 :
#             print(f"зп меньше 20к у: {n}")
#     print(f"Средняя зарплата: {sum/(len(txt))}")

# 4 задача

# with open("7dz_4zad1.txt",'r') as txt:
#     txt = txt.readlines()
#     dict = {"One":"один","Two":"два","Three":"три","Four":"четыре"}
#     answ=list()
#     for el in range(len(txt)):
#         n= (dict[txt[el].split('-')[0]])+" - " + txt[el].split('-')[1]
#         answ.append(n)
# with open("7dz_4zad2.txt",'w') as txt:
#     for el in answ:
#         txt.write(el)


# 5 задача

# with open("7dz_5zad.txt",'w') as txt:
#     el = input('вводи число ')
#     while el != "":
#         txt.write(el)
#         txt.write(' ')
#         el = input('вводи число ')
# with open("7dz_5zad.txt",'r') as txt:
#     txt = txt.readline().split()
#     answ=0
#     for el in txt:
#         answ += int(el)
#     print(answ)

# 6 задача
# import re
#
# with open("7dz_6zad.txt",'r') as txt:
#     txt = txt.readlines()
#     answ = dict()
#     for el in txt:
#         num = re.findall(r'\d+', el)
#         el = el.split(':')
#         summ=0
#         for al in num:
#             summ += int(al)
#         answ[el[0]]=summ
#     print(answ)

# 7 задача
# import json
# with open("7.txt",'r') as txt:
#     txt = txt.readlines()
#     dict1 = {}
#     dict2 = {}
#     dict3 = {}
#     answ = list()
#     summ = 0
#     for el in txt:
#         el = el.split()
#         if int(el[2]) > int(el[3]):
#             dict1[el[0]] = int(el[2]) - int(el[3])
#             summ += int(el[2])-int(el[3])
#         else:
#             dict3[el[0]] = int(el[2]) - int(el[3])
#     dict2['average profit'] = summ/ len(txt)
#     answ.append(dict1)
#     answ.append(dict2)
#     answ.append(dict3)
# with open("7.json", 'w') as json_obj:
#     json.dump(answ, json_obj)




