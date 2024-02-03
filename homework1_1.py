import datetime

def get_days_from_today(date: str):
    format = "%Y-%m-%d"
    try:
        datetime_object = datetime.datetime.strptime(date, format)
        difference = datetime.datetime.now().toordinal() - datetime_object.toordinal()
        return difference
    except Exception as e:
        print(f"Oopsie, we found an error: {e}")
    
print(get_days_from_today("1990-04-25"))