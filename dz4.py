# задача 1
#
# from sys import argv
# def zp(a,b,c):
#     try:
#         return a*b+c
#     except ValueError as err:
#         print('ошибка ',err)
# x=zp(int(argv[1]),int(argv[2]),int(argv[3]))
# print(x)

# 2 задача

# a=[300,2,12,44,1,1,4,10,7,1,78,123,55]
# m=[a[i] for i in range(1,len(a)) if a[i]>a[i-1]]
# print(m)

# # m=[m.append(a[i]) for i in range(1,len(a)) if a[i]>a[i-1]]    выдает нан нан нан нан ???

# 3 задача
# n=[m for m in range(20,241) if m%20==0 or m%21==0 ]
# print(n)
# 4 задача
# n=[2,2,2,7,23,1,44,44,3,2,10,7,4,11]
# m=[k for k in n if n.count(k)==1]
# print(m)

# 5 задача
#
# from functools import reduce
# n=[m for m in range(100,1000,2)]
# otvet=reduce(lambda x,y:x*y,n)
# print(otvet)


# 2 видео по генераторам. эксперименты.
# def func3(n):
#     cnt=0
#     while cnt<n:
#         yield cnt
#         cnt+=1
#
# d=func3(10)
# print(3 in d)
# print(next(d))
# # print(list(d))


# 6 задача. 1 часть
# from itertools import count
# for i in count(int(input())):
#     print(i,end="")
#     quit=input()
#     if quit=='q':
#         break


# 6 задача. 2 часть
#
# from itertools import cycle
# k=input().split()
# m=cycle(k)
# quit=None
# while quit!='q':
#     print(next(m), end="")
#     quit=input()

# 7  задача

# def funk(n):
#     cnt=1
#     p=1
#     while cnt<=n:
#         p=p*cnt
#         yield(p)
#         cnt+=1
# k=funk(int(input()))
# print(next(k))
# print(next(k))



# вроде как верный вариант решения 7 задачи....???


# for el in range(int(input())):
#     def funk(el):
#         cnt=1
#         p=1
#         while cnt<=el+1:
#             p=p*cnt
#             cnt+=1
#         yield(p)
#     c=funk(el)
#     print(next(c))

# l=[1,2,3,44,56,]
# iterator=iter(l)
# print(next(iterator))


