import datetime 

# weekday пщвертає день тижня у форматі від 0 (понеділок) до 6 (неділя)
specific_date1 = datetime.date(2020, 4, 26).weekday()
print(specific_date1)
specific_date2 = datetime.datetime(2020, 4, 25, 12, 45, 57, 34567).weekday()
print(f"Today is: {specific_date2}")