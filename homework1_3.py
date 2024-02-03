import re 

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone(phone_number: str):
    patt= r'[\d]+'
    step_1 = re.findall(patt, phone_number)  # Перший крок - обробляємо номери і видаляємо всі символи крім цифр
    clean_number = "".join(step_1)  # Об'єднуємо результат в єдиний рядок з цифр
    if len(clean_number) == 10:  # Далі перевіряємо формат введення номеру користувачем (з кодом чи без) і приводимо до єдиного формату
        full_number = "+38" + clean_number
    elif len(clean_number) == 11:
        full_number = "+3" + clean_number
    elif len(clean_number) == 12:
        full_number = "+" + clean_number
    return full_number

for num in raw_numbers:
    sanitized_number = normalize_phone(num)
    print (sanitized_number)
