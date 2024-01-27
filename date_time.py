import datetime

current_time = datetime.datetime.now()
# print(current_time)
# print(datetime.datetime.now().year)
# print(current_time.year)
# print(current_time.month)
# print(current_time.day)
# print(current_time.hour)
# print(current_time.minute)
# print(current_time.second)
# print(current_time.microsecond)
# print(current_time.tzinfo)            # Часова зона

# print(current_time.date())              # Дата без часу
# print(current_time.time())              # Час без дати

# specific_date1 = datetime.date(2020, 4, 25)
# specific_time1 = datetime.time(12, 40, 57)
# combined_datetime = datetime.datetime.combine(specific_date1, specific_time1)
# print(combined_datetime)


# specific_date2 = datetime.datetime(year=2020, month=4, day=25, hour=12, minute=45, second =57, microsecond=34567) # можна записати лише цифрами через кому
# print(specific_date2)

# # weekday пщвертає день тижня у форматі від 0 (понеділок) до 6 (неділя)
# specific_date1 = datetime.date(2020, 4, 26).weekday()
# print(specific_date1)
# specific_date2 = datetime.datetime(2020, 4, 25, 12, 45, 57, 34567).weekday()
# print(f"Today is: {specific_date2}")


# # Створення двох об'єктів datetime
# datetime1 = datetime.datetime(2023, 3, 14, 12, 0)
# datetime2 = datetime.datetime(2023, 3, 15, 12, 0)
# # Порівняння дат
# print(datetime1 == datetime2)  # False, тому що дати не однакові
# print(datetime1 != datetime2)  # True, тому що дати різні
# print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
# print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2

""" timedelta """
# x = current_time - datetime.datetime(2024, 1, 1) # різниця між двома датами
# print(x)
# print(type(x))  # об'єкт timedelta

# delta = datetime.timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2)
# print(delta)

# seventh_day_2019 = datetime.datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime.datetime(year=2020, month=1, day=7, hour=14)
# difference = seventh_day_2020 - seventh_day_2019
# print(difference)  # 365 days, 0:00:00
# print(difference.total_seconds())  # 31536000.0
# print(type(difference)) # datetime.timedelta
# print(type(difference.total_seconds())) # float


# first_d = datetime.datetime(2024, 2, 15, 15, 40)
# second_d = datetime.timedelta(hours = 22)
# together = first + second # Додаємо до певної дати визначений проміжок часу
# print(together)

""" toordinal - дні з початку ери"""
# # Отримання поядкового номеру ДНЯ (int) з початку ери. Так можна визначати різницю днів між двома датами в int
# first = datetime.datetime(2024, 2, 15, 15, 40)
# second = datetime.date(2020, 4, 25)
# ordinal1 = first.toordinal()
# ordinal2 = second.toordinal()
# print(ordinal1)
# print(ordinal2)

""" timestamp """
# # Конвертація datetime в timestamp
# timestamp1 = datetime.datetime.timestamp(current_time)
# print(timestamp1)  # Виведе timestamp поточного часу

# # Припустимо, є timestamp
# timest = 1617183600
# # Конвертація timestamp назад у datetime
# dt_object = datetime.datetime.fromtimestamp(timest)
# print(dt_object)  # Виведе відповідний datetime

""" strftime
%Y - рік з чотирма цифрами (наприклад, 2023).
%y - рік з двома цифрами (наприклад, 23).
%m - місяць як номер (наприклад, 03 для березня).
%d - день місяця як номер (наприклад, 14).
%H - година (24-годинний формат) (наприклад, 15).
%I - година (12-годинний формат) (наприклад, 03).
%M - хвилини (наприклад, 05).
%S - секунди (наприклад, 09).
%A - повна назва дня тижня (наприклад, Tuesday).
%a - скорочена назва дня тижня (наприклад, Tue).
%B - повна назва місяця (наприклад, March).
%b або %h - скорочена назва місяця (наприклад, Mar).
%p - AM або PM для 12-годинного формату."""
# print(current_time)
# required_format = "%d %b, %Y %I:%M %p"
# formatted_time = current_time.strftime(required_format)
# print(formatted_time)
# print(type(formatted_time)) # strftime переводить datetime у формат str

# # Припустимо, у нас є дата у вигляді рядка
# date_string = "2023.03.14"
# # Перетворення рядка в об'єкт datetime. Спочатку вказуємо рядок, який хочемо перетворити, потім ключ-формат для перетворення
# datetime_object = datetime.datetime.strptime(date_string, "%Y.%m.%d")
# print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу (зворотній від strftime)

""" ISO format """
# # Перетворення з/в ISO формат
# iso_format = current_time.isoformat()  #клас str
# print(iso_format)
# print(type(iso_format))
# iso_date_string = "2023-03-14T12:39:29.992996"
# date_from_iso = datetime.datetime.fromisoformat(iso_date_string) # клас datetime.datetime
# print(date_from_iso)
# print(type(date_from_iso))
# Дні тижні в ISO форматі (від 1(понеділок) до 7 (неділя))
# day_of_week = current_time.isoweekday()   # Використання isoweekday() для отримання дня тижня
# print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня

# # Створення ISO календаря у форматі кортежа (ISO_рік, ISO_тиждень, ISO_день_тижня)
# now = datetime.datetime.now() # Створення об'єкта datetime
# iso_calendar = now.isocalendar() # Отримання ISO календаря
# print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")

""" timezones """
# utc_now = datetime.datetime.now(datetime.UTC)
# print(utc_now)  # Виведе поточний час в UTC

# print( " -Local to ISO 8601 without microsecond:")
# print(datetime.datetime.now().replace(microsecond=0).isoformat())
# print( " -UTC to ISO 8601 with TimeZone information (Python 3):")
# print(datetime.datetime.now(tz=datetime.timezone.utc).isoformat())
# print( " -UTC to ISO 8601 with Local TimeZone information without microsecond (Python 3):")
# print(datetime.datetime.now().astimezone().replace(microsecond=0).isoformat())
# print( " -Local to ISO 8601 with TimeZone information (Python 3):")
# print(datetime.datetime.now().astimezone().isoformat())

# # Припустимо, місцевий час належить до часової зони UTC+2
# local_timezone = datetime.timezone(datetime.timedelta(hours=2))
# local_time = datetime.datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)
# # Конвертація локального часу в UTC
# utc_time = local_time.astimezone(datetime.timezone.utc)
# print(utc_time)  # Виведе час в UTC

# # Час у конкретній часовій зоні
# timezone_offset = datetime.timezone(datetime.timedelta(hours=2))  # Наприклад, UTC+2
# timezone_datetime = datetime.datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)
# # Конвертація у формат ISO 8601
# iso_format_with_timezone = timezone_datetime.isoformat()
# print(iso_format_with_timezone)