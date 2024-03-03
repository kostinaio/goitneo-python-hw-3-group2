

from collections import defaultdict
from datetime import datetime

def get_birthdays_per_week(users):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Автоматично створюємо пустий список
    birthdays_per_week = defaultdict(list)

    #Отримання поточної дати
    today = datetime.today().date()

    #Перебір користувачів
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо до типу date
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1) #Оцінка дати на цей рік
        
        delta_days = (birthday_this_year - today).days  #Порівняння з поточною датою
        
        #Визначення дня тижня
        if delta_days < 7:
            day_of_week = birthday_this_year.strftime("%A")
            if day_of_week == 'Saturday' or day_of_week == 'Sunday':
                day_of_week = 'Monday'  # Привітати в понеділок, якщо вихідний
            birthdays_per_week[day_of_week].append(name)

    for day in weekdays:
        if birthdays_per_week[day]:
            print(f"{day}: {', '.join(birthdays_per_week[day])}")

# Приклад використання:
# users = [
#     {"name": "Bill Gates", "birthday": datetime(1955, 10, 23)},
#     {"name": "Steve Jobs", "birthday": datetime(1955, 2, 25)},
#     {"name": "Iryna Kostina", "birthday": datetime(1995, 2, 28)},
#     {"name": "Andrii Kostin", "birthday": datetime(2020, 2, 23)},
#     {"name": "Ihor Kostin", "birthday": datetime(1995, 2, 24)}
# ]

# get_birthdays_per_week(users)