import time

seconds = time.time()
print ("\nSeconds since epoch (01.01.1970) =", seconds)
print(type(seconds)) # float

local_time1 = time.ctime(seconds)
print("\nLocal time:", local_time1)
print(type(local_time1)) # str

local_time2 = time.localtime(seconds)
print(f"\nМісцевий час: {local_time2}")
print(type(local_time2))  # time.struct_time

local_time_UTC = time.gmtime(seconds)
print(f"\nМісцевий час переведно в UTC: {local_time_UTC}")
print(type(local_time_UTC))  # time.struct_time

# print("Printed immediately")
# time.sleep(5)
# print("Printed after 5 seconds")

# i=0
# for c in ("HELLO"):
#     print(i*" "+c)
#     i+=1
#     time.sleep(.5)

"""ЛІЧИЛЬНИК ЧАСУ"""
# start_time = time.perf_counter()        # Записуємо час на початку виконання
# for i in range(1_000_000):              # Виконуємо якусь операцію
#     pass                                # Просто проходить цикл мільйон разів
# end_time = time.perf_counter()          # Записуємо час після виконання операції
# execution_time = end_time - start_time  # Розраховуємо та виводимо час виконання
# print(f"Час виконання: {execution_time} секунд")
