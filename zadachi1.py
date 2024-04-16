# #3.1
# names=["toto","nono","pepe"]

# for i in names:
#  print(i)

# #3.2
# for i in names:
#     a=f'hello,{i}'
#     print(a)

# #3.3
# car=["mers","bmb"]
# for i in car:
#     print(f'я хотел бы купить мотоцикл {i}')

# #3.4

# invite=["lura","kat","nas","rita"]
# l=["hiu"]
# p=["jn"]

# # def invite_func(*args):
# #     # for i in list_:
# #     #     t=f'добро пожаловать  всем в гости,{i}'
# #     #     print(t)
# #     mas = []
# #     for m in args:
# #         mas.extend(m)

# #     for i in mas:
# #         t=f'добро пожаловать  всем в гости,{i}'
# #         print(t)

# # invite_func(invite,l,p)

# #3.5
# n=invite[0:len(invite)]

# n[0]="lili"

# def invite_func(*args):
#     # for i in list_:
#     #     t=f'добро пожаловать  всем в гости,{i}'
#     #     print(t)
#     mas = []
#     for m in args:
#         mas.extend(m)

#     for i in mas:
#         t=f'добро пожаловать  всем в гости,{i}'
#         print(t)

# invite_func(n)
# print(invite[0])


#3.6
l=["kata","lolo","koko","popo","ubin"]


def invite(*args):
    global mas
    mas=[]
    for i in args:
       
        mas.extend(i)
        mas.insert(0,"ioio")
        mas.insert(len(mas)//2,"toto")
        mas.append("hoho")
        mas.insert(0,"uiui")
        print(mas)
  
    for m in mas:
        t=f'добро пожаловать  всем в гости,{m}'
        print(t)


invite(l)
# print(f'список расширился на  {mas[0]} {mas[len(mas)//2]} {mas[-1]}')


# 3.7



def invite(*args):
    global mas
    mas=[]
    for i in args:
       
        mas.extend(i)
        mas.insert(0,"ioio")
        mas.insert(len(mas)//2,"toto")
        mas.append("hoho")
        mas.insert(0,"uiui")
  
    for m in mas[:2]:
        t=f'придут толко,{m}'
        print(t)
    while len(mas)>2:
        removed_guest = mas.pop()
        print(f"Извините, {removed_guest}, но ваше приглашение отменено.")
    print("Приглашения остаются в силе для следующих гостей:")
    for guest in mas:
        print(guest)

    # del mas[0:]
    # print(mas)

       
    
    
   
  
       


invite(l)

# 3.8

country=["polsha","almaty",'bishkek','moskva']
country.reverse()
country.reverse()
country.sort(reverse=True)

print(country)

p=len(mas)
print(p)


