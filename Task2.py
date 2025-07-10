import csv

data = [
    {'Имя': 'Анна', 'Возраст': '25', 'Город': 'Москва'},
    {'Имя': 'Петр', 'Возраст': '30', 'Город': 'Санкт-Петербург'},
    {'Имя': 'Мария', 'Возраст': '28', 'Город': 'Киев'}
]

with open('данные_с_заголовками.csv', 'w') as csvfile:
    fieldnames = ['Имя', 'Возраст', 'Город']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)

with open('данные_с_заголовками.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)

csvfile.close()


f = open("prices.txt", "r", encoding="utf-8")
data = f.read()
data = data.split("\n")
for i in range(len(data)):
    data[i] = data[i].split("\t")

with open('prices.csv', 'w+') as csvprices:
    writer = csv.writer(csvprices)
    writer.writerows(data)

f.close()
csvprices.close()

sum_prices = 0
with open('prices.csv') as csvprices:
    data_prices = csv.reader(csvprices)
    data_prices = list(data_prices)
    data_prices = list(filter(lambda sub_list: sub_list, data_prices))
    for i in range(len(data_prices)):
        sum_prices += int(data_prices[i][1])*int(data_prices[i][2])
    print("Общая стоимость заказа: ", sum_prices)

csvprices.close()



