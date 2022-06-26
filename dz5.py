# # 1 задача
#
# txt = open("txtfail.txt","w")
# l1=[]
# a=str(input())
# while a!='':
#     l1.append(a+'\n')
#     a = str(input())
# txt.writelines(l1)


# 2 задача not write
# l1=open('txtfail.txt','r')
# l1=l1.readline()
# l1.split('\n')
# o=len(l1)
# print(o)
# for i in l1:
#     m=len(i)
#     print(m)

# 3 задача
# создание техт файла
# txt=open('txtfile.txt','w')
# l=['antonov 19000\n','petrov 30000\n','sidorov 41000\n']
# txt.writelines(l)
#
# # решение задачи
# with open('txtfile.txt','r') as txt:
#     l1=txt.readlines()
#     n=[]
#     summ=0
#     for i in l1:
#         i=i.split()
#         m=int(i[1])
#         summ = summ + m
#         if m<20000:
#             n.append(i[0])
#     print('меньше 20000 получают: ',n)
#     print('средняя зарплата: ',int(summ/len(l1)),' рублей')

# 4 задача
# dict={'One':'Один','Two':'Два','Three':'Три','Four':'Четыре'}
# with open('4 zad.txt','r') as txt:
#     l1=txt.readlines()
#     l2=[]
#     for i in l1:
#         for key in dict:
#             i=i.replace(key,dict[key])
#         l2.append(i)
# with open ('4 zad2.txt','w') as txt:
#     txt.writelines(l2)

# 5 задача

# with open('5 zd.txt','w') as txt:
#     txt.write('5 4 67 3273 150 30')
# with open('5 zd.txt','r')as txt:
#     l=txt.readline()
#     l=l.split()
#     m=0
#     for i in l:
#         m+=int(i)
# print(m)

# 6 задача
# with open('6.txt','r') as txt:
#     l=txt.readlines()
#     for el in l:
#         name, chas=el.split(":")
#         m=[]
#         n=''
#         for i in chas:
#             if i==' ' or i.isdigit():
#                 m.append(i)
#         n=n.join(m).split()
#         summ=0
#         for a in n:
#             summ+=int(a)
#         print(name+':'+str(summ))

# 7 задача

# import json
# with open('7.txt','r') as txt:
#     list=txt.readlines()
#     d={}
#     k={}
#     m=0
#     n=0
#     for line in list:
#         line=line.split()
#         if int(line[2])>int(line[3]):
#             d[line[0]]=int(line[2])-int(line[3])
#             m+=int(line[2])-int(line[3])
#             n+=1
#         else:
#             k[line[0]]=int(line[3])-int(line[2])
#     d['averange_profit']=int(m/n)
# with open('7.json','w') as json_obj:
#     json.dump(d,json_obj)
#     json.dump(k,json_obj)


# def divisors(integer):
#     str=[]
#     for i in range(2,integer):
#         if integer%i==0:
#             a=str.append(i)
#         else:
#             a='(integer) is prime'
#     return(a)
# print(divisors(int(input())))


# так и не смог решить!!!
# def division(integer):
#     st=' '*integer
#     for i in range(2,integer):
#         if integer%i==0:
#             st[i-1]=i
# print(division(int(input())))

"""пытаюсь притащить множество из программы тестировщика (список плюс число) в множество чисто чисел.
потом надо перекатать множесво в список и все заработает"""
# def find_outlier(integers):
#     b=set()
#     for elel in integers:
#         if isinstance(elel,int):
#             b.add(elel)
#         else:
#             elel=elel.split(', ')
#             for el in elel:
#                 b.add(el)



'''верный кусок кода, который работает на списках.'''
#     integers=integers.split(', ')
#     for el in range(len(integers)):
#         if int(integers[el])%2!=int(integers[el-1])%2 and int(integers[el])%2!=int(integers[el-2])%2:
#             return(integers[el])
# print(find_outlier(input()))

# def find_outlier(integers):
#     b=[]
#     for el in integers:
#         if type(el) == 'int':
#             b=b.append(el)
#     return(b)
# a=([3, 4, 5, 7, 13, 21, 55],3)
# # for el in a:
# #     print(type(el))
# print(find_outlier(a))

# a=([3, 4, 5, 7, 13, 21, 55],3)
# b=[]
# for el in a:
#     if isinstance(el,list)==True:
#         print(el)

integers=input()
integers=integers.split(', ')
print(integers)
b=[]
for el in range(len(integers)):
    if int(integers[el])%2!=int(integers[el-1])%2 and int(integers[el])%2!=int(integers[el-2])%2:
        b=b.append(el)
print(b)


