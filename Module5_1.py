# l1 = [x if x%2 == 0 else "|" for x in range(31)]  # якщо є else, то умова ставиться перед for. якщо else немає, то умова має бути після for
# print (l1)
# for el in l1:
#     print (el, end="")


# l2 = [x*x for x in range(31) if x%2 == 0]  
# print(l2)


# d1 = {x:x*x for x in range(31) if x%2!=0} # словник
# print(d1)
# d2 = {x for x in range(31) if x%2!=0} # множина
# print(d2)


# la = [1, 2, 3, 6, 7, 9, 12, 13, 15, 16]
# l3 = [x for x in la if x%2!=0] # робимо із одного списку інший за певною умовою
# l4 = [x for x in la if x%2!=0][2::] # зріз в новому списку
# print(l3)
# print(l4)

# s1 = "abcdaef"
# s2 = [x for x in s1 if x > "c"] # по алфавіту
# print(s2)

# s3 = "w234 234rf   234r234r 345".split(" ")
# s4 = [x for x in s3 if x != "" and x != "345"] # прибираємо зайві елементи, які були створені пілся split
# print(s4)

# s5 = '1 2 3 4 5 6 7'.split()
# s6 = [int(x) for x in s5] # після split робимо з рядків int
# print(s5)
# print(s6)



"""COLLECTIONS"""

"""from collections import namedtuple"""

# t1 = ("red", 12434) # Стандартний тюпл, але хз що за інфа в ньому. Також тюпл незмінний

# nt1 = namedtuple("Vehicle", ["color", "mileage"]) # типу шаблон для даних в тюплі, т.зв іменований тюпл

# car1 = nt1("red", 12434)
# print(car1) # Vehicle(color='red', mileage=12434)
# print(car1.color) # можна звернутись до елементу(параметра) з неймедтюпла
# print(car1[0]) # можна звертатись по індексу

# nt2 = namedtuple("Pet", "name type age") # альетрнативний варіант запису елементів(параметрів) - без списку
# pet1 = [nt2("Thor", "cat", 7), nt2("Odin", "dog", 8), nt2("Huginn", "raven", 2)]
# for pet in pet1:
#     print(pet)
#     print(pet.name)


'''car_template = namedtuple("Vehicle", ["color", "mileage"])'''

# car1 = car_template("red", 12434)
# # print(car1._asdict()) # зробити словник

# car2 = car1._replace(color="green")# робить заміну параметра, але не змінює в оригінальному неймед тюплі параметр
# print(car2)
# print(car1)

# car3 = car_template._make(["yellow", 342345]) # створюєм новий неймед тюпл по існуючому шаблону
# print(car3)

# l1 = [[1, 1000],
# [2, 2000],
# [3, 3000],
# [4, 4000]]
# l2 = []
# for parametrs in l1:
#     l2.append(car_template._make(parametrs)._asdict()) # робим словник по шаблону cars_template із параметрами із списка l1
# print(l2)


"""from collections import Counter"""

# s1 = "Абабагаламага".lower()
# c1 = Counter(s1)
# print(c1)
# print(dict(c1)) # можна одразу зробити словник
# c2 = c1['а']
# print(c2) # подивитись скільки конкретний символ зустрічається


# d1 = {"apples": 7, "bananas": 4, "oranges": 3}
# c3 = Counter(d1) # можна зі словника зробити Counter
# print(c3) # Counter({'apples': 7, 'bananas': 4, 'oranges': 3})
# d2 = {"apples": 15, "oranges": 10}
# c3.update(d2) # додаємо в каутер нові дані по окремим елементам. словник не додасть, а замінить дані на нові
# print(c3) # Counter({'apples': 22, 'oranges': 13, 'bananas': 4})
# d3 = {"apples": 2, "oranges": 2} 
# c3.subtract(d3) # а тепер віднімаємо
# print(c3) # Counter({'apples': 20, 'oranges': 11, 'bananas': 4})


# s2 = "абабагаламага"
# c4 = Counter(s2)
# print(c4.most_common(2)) # виводить значення які найчастіше зустрічаються. в дужках приймає кількість найчастіших. без значення в дужках виведе все


# s3 = "абабагаламага"
# c5 = Counter(s3)
# print(c5)
# c5.update("амальгама") # додаємо нові елементи в каунтер
# print(c5)
# print(c5.total()) # загальна кількість елементів


# d4 = {"apples": 7, "bananas": 4, "oranges": 3}
# c6 = Counter(d4)
# print(c6)
# c6.subtract(["apples", "apples", "apples", "bananas"]) # можна відняти поштучно!
# print(c6)


"""from collections import defaultdict"""

# str1 = "абабагаламага"

# d1 = defaultdict()

# d1.default_factory=int
# for letter in str1:
#     d1[letter]+=1
# print(d1)

# d1.default_factory=list
# for letter in str1:
#     d1["list1"].append(letter)
# print(d1)

# d1.default_factory=set # якщо елемент у форматі set відсутній, то він його створює із заданим ключем, і додає значення 
# for letter in str1:
#     d1["list2"].update(letter)
# print(d1)

'''from collections import deque'''

# dq1 = deque() # базово містить порожній список

# dq1.append(2) # дописує елемент в кінець списку
# dq1.appendleft(1) # дописує на початок списку

# dq1.extend([3,4]) # одразу додає декілька елементів в кінець
# dq1.extendleft([0,-1]) # одразу додає декілька елементів на початок

# dq1.pop() # прибирає елемент з кінця і зберігає його в себе (повертає його)
# dq1.popleft() # прибирає елемент спочатку і зберігає його в себе (повертає його)

# print(dq1)

# print(dq1.index(1)) # показує індекс елемента в списку

# print(dq1.count(3)) # показує скільки цей елемент зустрічається в списку

# dq1.remove(3) # видаляє конкретний символ, не повертає його
# print(dq1)

# dq1.rotate(2) # зсуває усі символи на визначену кількість позицій. можна вкаувати відємні значення - буде зсув ліворуч
# print(dq1)

# dq1.clear() # очищає список
# print(dq1) 


"""from decimal import *"""

# print(1.1+2.2) # 3.3000000000000003
# getcontext().prec=3 # задати кількість знаків, що буде виводити. решту відсікатиме
# print(Decimal("1.1")+ Decimal("2.2")) # 3.30. Краще переводити з рядка, а не з флоат, бо флоат буде містити купу знаків після коми

# import math 
# r = 10
# c = 2*math.pi*r
# print (c) # 62.83185307179586 --> башато зайвих цифр після коми. Decimal може прибрати їх

