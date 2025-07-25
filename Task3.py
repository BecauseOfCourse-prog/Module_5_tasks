import csv
import json

def convert(csv_file, json_file):
    data = []
    with open(csv_file, 'r', encoding='cp1251') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data.append(row)
    csvfile.close()

    with open(json_file, 'w', encoding='cp1251') as jsonfile:
        json.dump(data, jsonfile, indent=4)
    jsonfile.close()

convert("newjson.json", "данные_с_заголовками.csv")
with open('newjson.json', 'r') as file:
    data = json.load(file)
print(f"Файл CSV успешно преобразован в JSON файл: ")
print(data)
