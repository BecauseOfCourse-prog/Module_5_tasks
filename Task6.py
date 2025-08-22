import datetime

now = datetime.datetime.now()
print("Текущая дата и время:", now)
daysofweek = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
print("День:", daysofweek[now.weekday()])
year = int(now.year)
if year % 4 != 0:
    print("Текущий год не високосный")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Текущий год високосный")
    else:
        print("Текущий год не високосный")
else:
    print("Текущий год високосный")

parsed_date = datetime.datetime.strptime(input("Введите дату в формате год-месяц-день: "), "%Y-%m-%d")
print("Распарсенная дата:", parsed_date)
difference_days = parsed_date - now
print("Дней осталось до введённой даты:", difference_days.days)
difference = parsed_date - now
print("Разница между текущей датой и введённой:", difference)