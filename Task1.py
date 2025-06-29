# Название файла: test.txt
f = open(input("Введите название файла: "))
data = f.read()

def get_words(data):
    data = data.replace("—", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace(":", "").replace("\n", " ").lower()
    words = data.split(" ")
    words.remove("")
    return words

# Далее в функции get_words_dict() получаем словарь из слов, где ключ - это уникальное слово,

# а значение - количество вхождений данного слова в тексте.

def get_words_dict():
    words = get_words(data)
    words_dict = {}
    for i in range(len(words)):
        if words[i] in words_dict.keys():
            words_dict[words[i]] += 1
        else:
            words_dict[words[i]] = 0
    return words_dict

d = get_words_dict()
print("Кол-во слов: ", len(get_words(data)))
print("Кол-во уникальных слов: ", len(d.keys()))
print("Все использованные слова: ", d.items())
f.close()
