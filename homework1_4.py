import datetime

users = [
    {"name": "John Doe", "birthday": "1985.02.05"},
    {"name": "Jane Smith", "birthday": "1990.02.10"}
]

def get_upcoming_birthdays(users: list):

    this_day = datetime.datetime.now().date()  # Поточна дата

    congratulation_list = []  # Створюємо список, який повертатиме функція

    for user in users:

        format = "%Y.%m.%d"
        birthday_this_year = str(this_day.year) + user["birthday"][4::]  # Визначаємо дату народження юзера у цьому році
        birthday_this_year_dt = datetime.datetime.strptime(birthday_this_year, format).date()  # Переводимо дату народження у формат дейттайм

        difference = birthday_this_year_dt.toordinal() - this_day.toordinal()  #  Різниця в днях між датою народження у цьому році та поточною датою

        if difference >= 0 and difference < 8:  #  Аналізуємо виключно ДР на найближчі 7 днів (включно із сьогодні)
            if birthday_this_year_dt.weekday() < 5:  # Якщо ДР припадає на період з понеділка по п*ятницю, просто додаємо в список дату привітання
                congratulation_list.append({"name":user["name"], "congralulation_date":birthday_this_year})
            
            elif birthday_this_year_dt.weekday() == 5: # Якщо ДР припадає на суботу, додаємо 2 дні для отримання дати привітання (понеділок)
                congratulation_date_dt = birthday_this_year_dt + datetime.timedelta(days=2)
                congratulation_date = congratulation_date_dt.strftime("%Y.%m.%d")
                congratulation_list.append({"name":user["name"], "congralulation_date":congratulation_date})
            
            elif birthday_this_year_dt.weekday() == 6: # Якщо ДР припадає на неділю, додаємо 1 день для отримання дати привітання (понеділок)
                congratulation_date_dt = birthday_this_year_dt + datetime.timedelta(days=1)
                congratulation_date = congratulation_date_dt.strftime("%Y.%m.%d")
                congratulation_list.append({"name":user["name"], "congralulation_date":congratulation_date})

    return congratulation_list


print (get_upcoming_birthdays(users))


