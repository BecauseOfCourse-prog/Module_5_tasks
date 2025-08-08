import csv
import json

students = [
    {
        "имя": "Анна",
        "возраст": 20,
        "город": "Москва",
        "предметы": ["Python", "JavaScript"]
    },
    {
        "имя": "Петр",
        "возраст": 22,
        "город": "Санкт-Петербург",
        "предметы": ["Python", "Java"]
    },
    {
        "имя": "Мария",
        "возраст": 21,
        "город": "Киев",
        "предметы": ["JavaScript", "SQL"]
    }
]

with open("students.json", "w", encoding="cp1251") as jsonfile:
        json.dump(students, jsonfile)

with open("students.json", "r", encoding="cp1251") as jsonfile:
    data = json.load(jsonfile)
print(data)
print(f"Общее количество студентов в файле: {len(data)}")

def max_age():
    ages = []
    for i in range(len(data)):
        ages.append(data[i]["возраст"])
    for i in range(len(data)):
        if data[i]["возраст"] == max(ages):
            return data[i]

oldest = max_age()
print(f"Студент с наибольшим возрастом: {oldest}")

def specific_studs(subj):
    n = 0
    for i in range(len(data)):
        if subj in data[i]["предметы"]:
            n += 1
    return n

subj = input("Введите название предмета, по которому студенты будут подсчитаны: ")
studs_num = specific_studs(subj)
print(f"Число студентов, изучающих {subj}: {studs_num}")





sales = [
    ["Дата", "Продукт", "Сумма"],
    ["2023-01-01", "Продукт A", 500],
    ["2023-02-15", "Продукт B", 700],
    ["2023-03-10", "Продукт A", 800],
    ["2023-04-05", "Продукт C", 600],
    ["2023-04-20", "Продукт B", 900],
    ["2023-05-12", "Продукт A", 1000]
]

with open("sales.csv", "w", encoding="cp1251") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(sales)

sum_sales = 0
with open("sales.csv", encoding="cp1251") as csvfile:
    reader = csv.reader(csvfile)
    data_sales = list(reader)
    data_sales = list(filter(lambda sub_list: sub_list, data_sales))
    data_sales_info = data_sales
    data_sales_info.pop(0)
    for i in range(len(data_sales_info)):
        sum_sales += int(data_sales_info[i][2])
    print("Общая сумма продаж: ", sum_sales)

prods = {}
for i in range(len(data_sales_info)):
    if data_sales_info[i][1] not in prods:
        prods[data_sales_info[i][1]] = int(data_sales_info[i][2])
    else:
        prods[data_sales_info[i][1]] += int(data_sales_info[i][2])
print(f"Продукт с наибольшим объёмом продаж: {next(key for key, value in prods.items() if value == max(prods.values()))}")

months = {}
for i in range(len(data_sales_info)):
    if data_sales_info[i][0][5:7] not in months:
        months[data_sales_info[i][0][5:7]] = int(data_sales_info[i][2])
    else:
        months[data_sales_info[i][0][5:7]] += int(data_sales_info[i][2])
print(f"Общая сумма продаж для каждого месяца: {months}")






employees = [
    {
        "id": 1,
        "имя": "Иван",
        "должность": "Менеджер"
    },
    {
        "id": 2,
        "имя": "Елена",
        "должность": "Аналитик"
    },
    {
        "id": 3,
        "имя": "Дмитрий",
        "должность": "Разработчик"
    }
]

with open("employees.json", "w", encoding="cp1251") as jsonfile2:
        json.dump(employees, jsonfile2)

with open("employees.json", "r", encoding="cp1251") as jsonfile2:
    data_emp = json.load(jsonfile2)
print(data_emp)

performance = [
    ["employee_id", "performance"],
    ["1", "85"],
    ["2", "92"],
    ["3", "78"]
]

with open("performance.csv", "w", encoding="cp1251") as csvfile2:
    writer = csv.writer(csvfile2)
    writer.writerows(performance)

with open("performance.csv", encoding="cp1251") as csvfile2:
    reader = csv.reader(csvfile2)
    data_performance = list(reader)
    data_performance = list(filter(lambda sub_list: sub_list, data_performance))
    data_performance_info = data_performance
    data_performance_info.pop(0)
    employees_performance = data_emp
    for i in range(len(data_emp)):
        if data_performance_info[i][0] == str(employees_performance[i]["id"]):
            employees_performance[i]["perf"] = data_performance_info[i][1]
    print(employees_performance)

avg_perf = []
for i in range(len(data_performance_info)):
  avg_perf.append(int(data_performance_info[i][1]))
print(f"Средняя производительность среди всех сотрудников: {sum(avg_perf)/len(avg_perf)}")

def max_perf():
    for i in range(len(employees_performance)):
        if employees_performance[i]["perf"] == str(max(avg_perf)):
            return employees_performance[i]

optimal = max_perf()
print(f"Сотрудник с наибольшей производительностью: {optimal}")














