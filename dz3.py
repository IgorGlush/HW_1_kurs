# t=[((1,2),(6,0),(4,0),(5,2))]
#
# def second_el(*t):
#     second_el[1]=second_el[0]
#     return t
# print (t)


# l=[((1,2),(6,0),(4,0),(5,2))]
# for t in l:
#   t.append(-1)
# print(l)


# 1 задача
# a=int(input('1 chislo ', ))
# b=int(input('2 chislo ', ))
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print('delenie na 0')

# 2 задача
# def dannie (name:str,surname:str,age,city:str,email:str,tel:str):
#     res=name+' '+surname+' '+age+' '+city+' '+email+' '+tel
#     return(res)
#
# c=dannie(name=input('имя ' ),age=input('год рождения ' ),city=input('город ' ),surname=input('фамилия ' ),email=input('email ' ),tel=input('тлф ' ))
# print(c)

# def my_funk(a,b,c):

# 3 задача
# def c(a,b,c):
#     return(a*b*c/min(a,b,c))
# p=c(int(input()),int(input()),int(input()))
# print(p)


# 4 задача
# def my_function (x,y):
#     c=x**y
#     return(c)
# m= my_function(float(input()),int(input()))
# print(m)

# 4 задача 2 способ
# def my_funktion (y,x):
#     i = 1
#     c = 1
#     while i <= x:
#         c = c * y
#         i += 1
#     return(c)
# m=my_funktion(float(input('введи число ', )),int(input('введи степень ', )))
# print(m)

# 5 задача (без функции)
# m=0
# while True:
#     x = input("вводи числа через пробел. стоп знак $ ", )
#     x = x.split(' ')
#     i = 0
#     while i < len(x):
#         if x[i] == '$':
#             print(m)
#             exit()
#         else:
#             f = int(x[i])
#             m = m + f
#             i += 1



# 6 задача
# def funk(x):
#     x = x.split(' ')
#     n=[]
#     for i in x:
#         i = i.capitalize()
#         n+=i+' '
#     return(n)
# c=funk(input())
# print(c)