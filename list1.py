# # 29 Вам дан список из 3 чисел, выведите все возможные комбинации с этими числами
# # Например:
# from itertools import *
# list_ = [1, 2, 3]
# t=[]
# for i in permutations(list_):
#     t.append(list(i))

# p=''
# for e in t:
#     for w in e:
#      p+=str(w)
#      p+=' '
#      r=p[0:5]
#      u=p[5:11]
#      w=p[11:17]
#      q=p[17:23]
#      f=p[23:29]
#      c=p[29:35]
     
     
# print('\n',r)
# print(u)
# print(w)
# print(q)
# print(f)
# print(c)


# from itertools import *
# list_ = [1, 2, 3]
# t=[]
# for i in permutations(list_):
#     print(i) 


# 30 Создайте список с 3 вложенными списками, где внутри должно быть три 0 K = 3 (количество списков и элементов)
# Результат:

# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# K = 1
# p=[0]*K
# y=[]
# for i in range(K):
#     y.append(p)


# print(y)

#   Задание 31
# Вам дан список со строками, необходимо перевернуть эти строки, а также отсортировать по длине
# Например:

# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# Результат:

# ['deR', 'eulB', 'neerG', 'etihW', 'kcalB', 'wolleY', 'egnarO']

# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# t=[]
# for i in colors:
#     j=''
#     for y in i:
#         j=y+j
#     t.append(j)
#     t=sorted(t,key=lambda x:len(x))
   



# print(t)



# 32 Вам дан список с элементами, добавьте элемент, который хранится в переменной element в этот список после каждого n-ого шага
# Например:

list_ = [1,2,3,4,5,6,7,8,9,0]
step = 2
element = 'A'



# Результат:

# [1, 2, 'A', 3, 4, 'A', 5, 6, 'A', 7, 8, 'A', 9, 0, 'A']




# Вам дан список со вложенными списками, выведите тот список, у которого самая большая сумма
# Например:

lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
l=lists[0]
# Результат:

# [10, 11, 12]

for  i in lists:
    if sum(l)<sum(i):
        l=i

     
print(l)


# Задание 34
# Дан список целых чисел с повторяющимися элементами. Вам надо создать еще один список, содержащий только повторяющиеся элементы. Проще говоря, новый список должен содержать элементы, которых больше одного.
# Например:

list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Результат:

# repeated = [20, 30, -20, 60]
o=list(filter(lambda x:list_.count(x)>1,list_))
print(list(dict.fromkeys(o)))



# Задание 35
# Вам дан список из букв, пользователь вводит 2 буквы, от какой и до какой буквы нужно соединить в одну строку, ваш код должен соединить эти буквы
# Например:

# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# merge_from = 'a'
# merge_to = 'd'
# Результат:

# ['abcd', 'e', 'f', 'g']




# Задание 21
# Вам дан список из строк, в которых длина строки равна 2 или более, в новый список запишите индексы тех строк, у которых первый и последний символы совпадают.
# Например:

str_list = ['abc', 'xyz', 'aba', '1221']
# str_list=range(len(str_list))
# print(str_list)
# Результат:

# indexs = [2, 3]
# index=[]
# for i in str_list:
#     if i[0]==i[-1]:
#         index.append(str_list.index(i))
       
        
# print(index)


# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# merge_from = 'a'
# merge_to = 'd'

# for i in chars:
#     if i==merge_from and i==merge_to:
#         h=''.join(i)
#         print(h)
# b = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# for i,k in b.items():
#     if k%2==0:
#         b[i]="2"
# print(b)


# a= {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b={}
# for i,k in a.items():
#     if k%2==0:
#         b[i]="2"
#     else:
#         b[i]=k
# print(b)
a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
for i,k in list(a.items()):
    if k==None:
        a.pop(i)
print(a)


a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
b={}
for i,k in a.items():
    k=k/5
    b[i]=k

    
print(b)


a = {'apple': 2, 'orange': 5, 'banana': 10}
    
for i,k in list(a.items()):
    if k%2==0:
        a.pop(i)
    
print(a)


a = {'a': 1, 'b': 2, 'c': 3} 
b={}
for i,k in list(a.items()):
    b[k]=i
    
print(b)


a = {'a': 3, 'b': 2}
b=0
for i in list(a.values()):
    b+=i
print(b)


dict_ = {'x': 1, 'y': 2, 'z': 1}
p=list(dict_.keys())
print(p[0])

dict_ = {'a': 1, 'b': 2, 'c': 1}


# o=[]
# for i,k in list(dict_.items()):
#     o.append(i)
#     o.remove('b')
   
# print(o)


dict_ = {'a': 1, 'b': 2, 'c': 1}
print(dict_.keys())


dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
a=dict_.values()
print(max(a))

dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 


for i,k in list(dict1.items()):
    if k%2!=0:
        dict1[i]="1"
print(dict1)

dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
dict2=dict1.copy()

for i,k in dict1.items():
    if k%2!=0:
        dict2[i]=1
print(dict2)

# Дан словарь, оставьте все элементы с пустыми значениями, остальные удалите
#  dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# Вывод:
# {'a': None, 'd': None}

dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
for i,k in  list(dict_.items()):
    if k!=None:
        del dict_[i]
print(dict_)


dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 

dict2 = {}

for i,k in dict1.items():
    i=i**2
    dict2[i]=k
print(dict2)


dict_ = {'Bootcamp': 6, 'Makers': 6, 'coding': 6, 'hello': 5}
a=dict_.values()
a=max(a)
if a in dict_.values():

    print(dict_.keys())


# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# dic={}
# for i,k in dict_.items():
#     for y in k.values():
#         dic[i]=y
# print(dic)

dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
dic={}
for i,k in dict_.items():
    for y in k.values():
        dic[i]=y
print(dic)

a={4, 6, 100, -45, -6} 
b={4, 5, -5, -6}
a=a.intersection(b)
print(a)


tilek={"Dodo","ImperiaPizza","FreshBox"}
timur={"OchakKebab","FreshBox"}
alexander={"FreshBox","KFC"}

elina={"Dodo","ImperiaPizza","FreshBox","OchakKebab","FreshBox","FreshBox","KFC"}
a=elina.intersection(tilek,timur,alexander)
print(a)



# Задание 13
# Роберт загадал пять чисел.

# Используя методы множеств, напишите код определяющий, кто из перечисленных ниже людей угадал хотя бы одно число из загаданных Робертом.

# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10}
# Если есть хотя бы одно число, которое угадал kail и хотя бы одно число, которое угадала merri, вывод должен быть:

# "kail merri"
# Если же только один из них угадал, то запринтите имя того, кто угадал

# # Если же никто не угадал заданное число, выведите строку:

# # no one
# # Пример:

# # robert = {5, 7, 11, 10, 28} 
# # kail = {1, 5, 14, 8, 22} 
# # merri = {19, 20, 3, 11, 10}
# # output:

# # "kail merri"


# # dict_ = {
# #     'math': {
# #         'sum': sum
# #     },
# #     'vars': {
# #         'a': 5,
# #         'b': 20,
# #         'c': 50
# #     }
# # }

# # print(dict_)





# dict_ = {
#     'math': {
#         'sum': sum
#     },
#     'vars': {
#         'a': 5,
#         'b': 20,
#         'c': 50
#     }
# }

# a=dict_.get('math')
# p=a.get('sum')
# s=dict_.get('vars')
# s=s.values()
# f=p(s)

# print(f)

# Задание 34
# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом, чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря
# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# dict_ = {}
# Вывод:
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven'}

# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# dict_ = {}

# for i in range(len(list1)):
#     dict_[list1[i]]=list2[i]
# print(dict_)


# import functools
# a = {'a': 10, 'b': 9, 'c': 3}
# s=[]
# for i in a.values():
#     s.append(i)
#     b=functools.reduce(lambda a,b: a*b,s)
# print(b)



# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = input()

# if dict_.keys()==key:
#         print("Key is present in the dictionary")
# else:
#         print("Key is not present in the dictionary")



# import functools
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# f=[]

# for i,k in dict1.items():
#     for y in k.values():
#         f.append(y)

# a=f[0:2]
# b=f[2:4]
# c=f[4:6]
# a=functools.reduce(lambda a,b:a*b,a)
# b=functools.reduce(lambda a,b:a*b,b)
# c=functools.reduce(lambda a,b:a*b,c)
# dict2['a']=a
# dict2['b']=b
# dict2['c']=c
# print(dict2)


# string = "pythonist" 
# a=string.count("p")
# print(a)
# dict_={}
# for i in string:
#     if i not in dict_:
#         dict_[i]=string.count(i)
# print(dict_)



string = "pythonist" 
# for i in string:
#    pass
# print(string.count(i))
dict_=dict(map(lambda i: (i,string.count(i)),string))
print(dict_)


# def  sum_digits(a):
#     a=str(a)
#     r
    
# print(sum_digits(105)) 



a=677
a=str(a).replace('',' ').split()
s=[int(i) for i in a]
s=sum(s)

print(s)
    

def  sum_digits(a):

    a=677
    a=str(a).replace('',' ').split()
    s=[int(i) for i in a]
    s=sum(s)

    return s 
    
   
print(sum_digits(105)) 

p={"k":[{"r":1,"l":0},{"r":2,"l":0},{"r":3,"l":0},{"r":4,"l":0}],"o": [{"r":1,"l":0},{"r":2,"l":0}]}
for i in p.values():
    
        t='r'
        if t in i:
          print(len(t))
        
        



