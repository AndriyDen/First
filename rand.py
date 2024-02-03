import random

# def max_(list_=None):
#     if list_ is not None:
#         max_=0
#         for i in list_:
#             if max_<i:
#                 max_=i
#     return max_

# list_=[]
# while len(list_)<10:
#     a=random.randint(0,100)
#     if a not in list_:
#         list_.append(a)
# print(list_)
# print(max_(list_))


# random.seed()
# list1=[]
# while len(list1)<10:
#    a=random.randint(0,10)
#    if a not in list1:
#        list1.append(a)
# print(list1)
# s=random.sample(list1,6)
# print(s)
# # print(max(list1))


# colors = ['червоний', 'зелений', 'синій']
# weights = [100, 1, 1]
# chosen_color = random.choices(colors, weights, k=10)
# print(chosen_color)

a = range(0, 101)
k = random.sample(a, 10) # sample дає унікальні значення
p = random.choices(a, k=10) # choices може мати повтори. Кількість виводів обов'язково через аргумент "k"
print(k)
print(p)
