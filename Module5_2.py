"""ФУНКЦІОНАЛЬНЕ ПРОГРАМУВАННЯ"""

# print(list(map(lambda x: x*x, range(10)))) # map проганяє через функцію на першому місці, всі ітеровані обєкти з другого місця.

# def sum(a,b):
#     def f(b): # функція всередині функції має доступ до зміннихх в батьківській функції
#         return a+b
#     return f(b)

# a = sum(2,3)
# print(a)

# def connect(*args):
#     def connect_tcp(): # замкнена функція. бажано не сунути в дочірню функцію змінні за межами батьківської
#         return 1
#     def connect_udp():
#         return 2
#     if args[0]=='udp': # якщо запускаємо функцію connect, то вона спочатку перевіряє чи задано їй параметр "udp". якщо задано, то повертає 2
#         a = connect_udp()
#     else: # якщо не задано визначений параметр, то спрацьовує else, і повертає 1
#         a = connect_tcp()
#     return a

# print(connect("udp"))


"""DECORATOR"""


# def deci(func): # декоратор отримує функцію як аргумент, так і повертає теж функцію - wrapper
#     def wrapper(*args, **kwargs):
#         original_result = func(*args, **kwargs)
#         modified = "<i>"+original_result+"</i>"
#         return modified
#     return wrapper

# def decb(func):
#     def wrapper(*args, **kwargs):
#         original_result = func(*args, **kwargs)
#         modified = "<b>"+original_result+"</b>"
#         return modified
#     return wrapper

# @deci # додаємо до функції output декоратор з іншої функції - dec. 
# @decb # спочатку застосовується цей декоратор, потім @deci. тобто знизу вгору від функції
# def output(something):
#     return something

# print(output("s"))

"""-----------------------------------------"""

# def dec_log(func): # декоратором зберігаєм в лог, що робить основна функція
#     def wrapper(*args, **kwargs):
#         print("----------------")
#         print(f"Function: {func.__name__}")
#         print(f"parametrs: {args}, {kwargs}")
#         res=func(*args, **kwargs)
#         print (f"Result: {res}") 
#         print("-----------------")       
#         return res
#     return wrapper

# @dec_log # додаєм декоратор по кожній функції, результати якої треба зберігти
# def output(something):
#     return something

# @dec_log
# def sum2(a,b):
#     return a+b 

# @dec_log
# def prod2(a,b):
#     return a*b

# print(output("string"))
# print(sum2(3,4))
# print(prod2(3,4))


"""ГЕНЕРАТОРИ .... YIELD"""

"""ЧОМУ ПОВЕРТАЄ НЕ ВСІ ЧИСЛА З РЕНЖУ 10???"""
# def gen_numbers(a): # функція з генератором yield виконується один раз і чекає, коли до неї знов звернуться
#     for i in range(a):
#         yield i

# n1 = gen_numbers(10)
# for i in n1:
#     print(i)
    # next(n1) # next(n1) робить скіп кожного другого обєкта. тобто for бере один обєкт і друкує його, потім next скіпає другий обєкт, на наступній ітерації for бере вже третій обєкт

# def get_numbers():
#     yield 100
#     yield 200
#     yield 300

# n2 = get_numbers()
# print([i for i in n2]) # створюємо список через генератор
# print([i for i in n2]) # два раии не працює через ту саму змінну - повертає 0. треба або інша змінна, або викликати функцію напряму
    

"""map, zip, enumerate"""

# list1 = [1,2,3,4,5,6,7,8,9,10]
# list1 = [i+1 for i in range(10)] # те саме, що і вище
# print(list1)

# list2 = map(lambda x: x*x,list1) # передаємо два параметри - функцію, яка буде виконуватись, та власне ітерабельний обєкт. функцію def передаємо в map без ()
# print(list(list2)) # map повертає обєкт map. його треба завернути у шось, щоб отримати інший обєкт (list, set)

# list3 = filter(lambda x: x%2==0, list1)
# print(list(list3)) # filter треба теж у шось завернути - list, set ...

# # map змінює кожний елемент, filter фільтрує елементи, і не змінює. ???

# list4 = any(i%2==0 for i in list1) # показує, що в списку є хоч одне число, яке відповідає умові (діляться на 2 без залишку). повертає True/ False
# print(list4)

# list5 = all(x%2== 0 for x in list1) # показує, що в списку всі числа відповідають умові (діляться на 2 без залишку). повертає True/ False
# print(list5)

# list6 = enumerate(list1)
# print(list(list6)) # нумерує елементи в списку через створення пар в кортежах. Нумерація зліва, значення списку справа

# list6_5 = dict(enumerate(list1))
# print(list6_5)
# list6_6 = {x:y for x,y in enumerate(list1)} # те саме, що і list6_5

# list7 = zip(list1, "qwerty") # обєднує декілька ітерабельних обєкта. наприклад, два списка. zip повертає список із кортежів. класно робити словники
# print(list(list7))
# dict7 = dict(zip(list1, "qwerty")) # хєранули словник
# print(dict7)

# from functools import *
# list8 = reduce(lambda x, y: x+y, list1) # ніхєра не ясно. сума/добуток всіх елементів в списку. або зліпити всі елементи в рядок. типу звести все до купи
# print(list8)

