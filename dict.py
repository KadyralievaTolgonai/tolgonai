# def filter_list(l):
#     a=[]
#     for i in l:
       
#         if (str!=type(i)):
#             a.append(i)
#     return a

   
# print(filter_list([1,2,'e']))
    
# def square_digits(num):
#    a=str(num)
#    for i in a:
#     i=i**2
#    return i
# print(square_digits(4677))


# def square_digits(num):
  
# #     b=str(num).replace('',' ')
# # #     b=b.split()
# # #     c=[int(i) for i in b]
# # #     a=[i**2 for i in c]
# # #     d=[str(i) for i in a]
# # #     h=''.join(d)
# # #     x=int(h)
# # #     return x
    
# # # print(square_digits(243))




# # text=input()
# # d={}
# # for c in text:
# #     if  c   in d:
       
# #      d[c]=d[c]+1
  
# #     else:
# #      d[c]=1
# # for k in d:
# #     print(k,d[k])

# # a=input()
# # s=a.isalnum()
# # if a.isalnum():
# #     print(s)








# # def count_digits(text):
# #     # Создаем словарь для хранения частоты вхождения цифр
# #     digit_frequency = {}

# #     # Проходим по каждому символу в тексте
# #     for char in text:
# #         # Проверяем, является ли символ цифрой
# #         if char.isdigit():
# #             # Если цифра уже есть в словаре, увеличиваем ее счетчик
# #             if char in digit_frequency:
# #                 digit_frequency[char] += 1
# #             # Если цифры нет в словаре, добавляем ее и устанавливаем счетчик в 1
# #             else:
# #                 digit_frequency[char] = 1

# #     return digit_frequency

# # def main():
# #     text = input("Введите текст: ")
# #     # Получаем словарь с частотой вхождения цифр в текст
# #     frequency_dict = count_digits(text)
    
# #     print("Частота вхождения цифр:")
# #     for digit, frequency in sorted(frequency_dict.items()):
# #         print(f"Цифра {digit}: {frequency} раз")

# # if __name__ == "__main__":
# #     main()





# # d=input()
# # f={}
# # for i in d:
# #     if i.isdigit():
# #         if i in f:
# #             f[i]+=1
# #         else:
# #             f[i]=1
# # for i,k in f.items():
# #     print(i,k)


# o=input()

# s={"россия":"москва","казакстан":"астана","кыргызстан":"бишкек"}
# if o in s:
#     print(f'{o}-{s[o]}')



# # for i in s:
# #     if i in o:
# #         print(s[i])
# #     elif s[i] in o:
# #         print(i)
# # else:
# #      print("no")



# list_=[i if i%2==1 else i**2 for i in range(1,11)]
# print(list_)


# Рассмотрим данный пример, дан список:

# old_list = [-2, 5, -8, -16, 9, 58] 
# На базе этого списка нужно создать новый, где все отрицательные числа будут заменены строкой 'меньше нуля'.

# Простого условия, по которому должны сортироваться числа здесь не достаточно, ведь нам нужно заменить некоторые из строк. Используя тернарные операторы, мы можем переписать наше условие таким образом:

# x if x > 0 else 'меньше нуля' 
# То есть, мы должны оставить число (х) если оно больше нуля, в противном случае (else) заменить его строкой 'меньше нуля'.

# Теперь нужно просто указать что применяем тернарный оператор для каждого элемента х списка old_list:

# x if x > 0 else 'меньше нуля' for x in old_list 
# Оборачиваем в квадратные скобки, присвоим переменной new_list и распечатаем результат:

# my_list = [x if x > 0 else 'меньше нуля' for x in old_list] 

# print(my_list) 
# Получаем в терминале:

# ['меньше нуля', 5, 'меньше нуля', 'меньше нуля', 9, 58] 



list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
int_list=[i if i >=0 else 1 for i in list_ ]
print(int_list)

list_ = [False, True, False, True, False, True, False, True, False, True] 
l=[0 if i==False else 1 for i in list_]
print(l)


list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 

new_list=[len(i) for i in list_name]
print(new_list)



list1 = [2, 4, 6, 8, 10, 12, 14]
l=[i**2 for i in list1 if i**2>50]
print(l)


string = "happy birthday!"
list_=[i.replace('!','').replace(' ','')  for i in string]
list_.pop()
list_.remove('')
print(list_)

# Задание 26
# Дан словарь:
# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# Используйте его чтобы создать список, из значений внутренних словарей
# Вывод:

# [3, 45, 23, 9, 12, 89]
dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
l=[i for i in dict_.values() for i in i.values() ]
print(l)


# Задание 27
# Из списка:
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# Создайте словарь, занесите только те имена, длина которых больше 4. Ключами будут имена, а значениями их длины, возведенные
# в квадрат.
# Вывод:

# {'george': 36, 'ringo': 25, 'patty': 25, 'cynthia': 49, 'linda': 25}


# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# l={i:len(i)**2 for i in list_name if len(i)>4}
# print(l)


dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

j=[ k.upper() for k,v in dict_.items() if 200<v<5000]
print(j)


dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

dict2={i:i.count('i')for i in dict1 if i.replace('i','')}
print(dict2)

dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

dict2={i.replace('i',''):i.count('i') for i in dict1 }
print(dict2)


list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]




# Задание 30
# Из списка
# list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
# Создайте новый list2, не добавляя все пустые значения (0, None, [], {}, '')
# Вывод:


[1, 2, 3, 'a', 'abc', 23, [1, 2, 3, 4], {'a': 1, 'b': 2}, 'drf']
list2=[i for i in list1 if i]
print(list2)



SPL_Patrons = [
['Kim Tremblay', 134],
['Emily Wilson', 42],
['Jessica Smith', 215],
['Alex Roy', 151],
['Sarah Khan', 105],
['Samuel Lee', 220],
['William Brown', 24],
['Ayesha Qureshi', 199],
['David Martin', 56],
['Ajeet Patel',69]
]

l=[i for i in SPL_Patrons for i in i if type(i)==int if i>100]
print(l)



SPL_Patrons = [
['Kim Tremblay', 134],
['Emily Wilson', 42],
['Jessica Smith', 215],
['Alex Roy', 151],
['Sarah Khan', 105],
['Samuel Lee', 220],
['William Brown', 24],
['Ayesha Qureshi', 199],
['David Martin', 56],
['Ajeet Patel',69]
]

readers=[ i[0]  for i in SPL_Patrons if i[1]>100]
print(readers)




dict_ = {
    'Sasha': {
        'likes': 23,
        'comments': 2,
        'rating': 4
    },
    'Aliya': {
        'likes': 34,
        'comments': 5,
        'rating': 5
    },
    'Dasha': {
        'likes': 15,
        'comments': 3,
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': 2,
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': 7,
        'rating': 2
    }
}


l=[i['likes'] for i in dict_.values() if i['rating']>3 ]
print(sum(l))

# Экстра задание 1
# Создайте список list_ от 0 до 10 включительно c помощью специальной функции которая генерирует последовательно чисел,
# отфильтруйте список оставив в нем только четные элементы,
# затем разделите каждый элемент на 2 и выведите результат,
# нужно работать только с одним списком, нельзя создавать доп. списки.
# Необходимо использовать list comprehension
# Распечатайте результат.
list_ =list(i/2 for i in filter(lambda x:x%2==0,range(11))  )
print(list_)




class Solution:
    def __init__(self,a):
        self.a=a
    
    def twoSum(self):
       
     return self.a[0]+self.a[1]
p=Solution([2,7,11,15])
print(p.twoSum())


# Экстра задание 2
# Создайте словарь dict_ в котором ключами будут числа, а значениями строки. Перебирите словарь циклом:

# если ключ четный, нужно заменить его значение на длину этого значения
# если ключ нечетный то возвести длинну его значения в 3 степень
# Распечатайте dict_.
dict_={6:"tfjhvb",9:"ftyvhjb"}
a={i:len(k) if i%2==0 else len(k)**3 for i,k in dict_.items() }
print(a)
        
string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
a=string_.split()
for i in a:
 if i.isdigit():
    pass

print(i)
        
def get_type(h,k):
     return type(h)
     return type(k)
    
    
print(get_type(6,"h"))
print(get_type("jiu",9))


def divide(h,l):
    return h/l
print(divide(7,8))

dict_={9:"yty","hkj":"j:"}
def dictionary(dict_):
   
    for i in dict_.keys():
        print(i)
dictionary(dict_)


def is_palindrome(a):
    if a==a[::-1]:
        return True
    else:
         return False
print(is_palindrome("довод"))
    
def max_num(a,k):
    o=0
    if a>k:
        
        return a
    else:
        return k
   
print(max_num(10, 12))   

# Задание 9
# Создайте функцию:

# multiply_list()
# которая принимает список чисел и возвращает их произведение.

# Пример:

# print(multiply_list([1, 2, 3, 4, 5, 6])) 
# Вывод:


from functools import reduce
def multiply_list(a):
    
        p=reduce(lambda k,l:k*l,a)
        return p
print(multiply_list([1, 2, 3, 4, 5, 6])) 