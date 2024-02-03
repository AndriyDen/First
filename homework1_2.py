import random

def get_numbers_ticket(min: int, max: int, quantity: int): # Функція приймає 3 параметри у форматі int
    if 1000 <= min or \
        min < 1 or \
        1000 < max or \
        max <= 1 or \
        max - min <= 0 or \
        quantity >= max - min: # Перевіряємо відповідність параметрів заданим обмеженням
            return []
    else:
        a = range(min, max + 1)  # Беремо послідовність цифр від (min) до (max+1), так як останнє значення не включається
        k = random.sample(a, quantity) # З отриманої послідовності (a) беремо кількість рендомних унікальних чисел відповідно до параметра (quantity) -> повертає список із рендомними числами
        k = sorted(k)
        return k

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
                
    