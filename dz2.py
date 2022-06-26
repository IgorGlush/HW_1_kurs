# c=['p','r',['ivet'],430]
# i=0
# u=len (c)
# while i < u:
#     print(type(c[i]))
#     i+=1

# задача 2
# c=list(input('вводи ', ))
# i=0
# u=1
# while u<len(c):
#     c[i],c[u]=c[u],c[i]
#     i+=2
#     u+=2
# print(c)


#задача 3 метод 1
# c=int(input('введите номер месяца числом ' ))
# d=[['весна'],['лето'],['осень'],['зима']]
# if c<3:
#     print(d[3])
# elif c<6:
#     print(d[0])
# elif c<9:
#     print(d[1])
# elif c<12:
#     print(d[2])
# else:
#     print(d[3])

#задача 3 метод 2
# c=int(input('введите номер месяца числом ' ))
# d={1:'зима',2:'зима',3:'весна',4:'весна',5:'весна',6:'лето',7:'лето',8:'лето',9:'осень',10:'осень',11:'осень',12:'зима'}
# print(d[c])

#задача 4
# c=input('вводи ' )
# с=c.split()
# i=0
# while i<len(с):
#     print(i+1, с[i][:10])
#     i+=1

#задача 5
# m=[7,5,3,3,2]
# c=int(input('вводи число ' ))
# i=0
# if c<=m[-1]:
#     m.append(c)
# else:
#     while c<=int(m[i]):
#         i+=1
#         u=int(m[i])
#     m.insert(i,c)
# print(m)

#задача 6
# spis=[]
# i=1
# a=int(input('добавляем товар(1) или анализируем(2)? '))
# while a==1:
#     b=input('название ' )
#     c=int(input('цена ' ))
#     d=int(input('количество ' ))
#     e=input('ед ' )
#     x=(i,{'название':b,'цена':c,'количество':d,'ед':e})
#     spis.append(x)
#     i+=1
#     a = int(input('добавляем товар(1) или анализируем(2)? '))
# z=set()
# x=set()
# v=set()
# f=set()
# for u in spis:
#     key=list(u[1].values())
#     z.add(key[0])
#     x.add(key[1])
#     v.add(key[2])
#     f.add(key[3])
# dict={'название':str(z),'цена':str(x),'количество':str(v),'ед':str(f)}
# print(dict)

# a='пися'
# b='попа'
# print(a+b)

