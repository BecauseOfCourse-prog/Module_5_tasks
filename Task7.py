import random
import collections

numlist = []
for i in range(100):
    a = random.randint(0, 100)
    numlist.append(a)
counter = collections.Counter(numlist)
print(counter)
uniqkeys = []
for key, value in counter.items():
        if value == 1:
            uniqkeys.append(key)
print(uniqkeys)
for i in range(3):
    biggestvalue = 0
    biggestkey = 0
    for key, value in counter.items():
            if value > biggestvalue:
                biggestvalue = value
                biggestkey = key
    print(f"{biggestkey} количество вхождений: {biggestvalue}")
    del counter[biggestkey]



Book = collections.namedtuple("Book", ["title", "author", "genre"])
book1 = Book("Война и мир", "Лев Толстой", "Роман")
book2 = Book("Двадцать тысяч лье под водой", "Жюль Верн", "Научная фантастика")
book3 = Book("Хребты безумия", "Говард Филлипс Лавкрафт", "Ужасы")
print(book1.title, book1.genre)
print(book2.title, book2.author)
print(book3.author, book3.genre)



dictsample = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]
defdict = collections.defaultdict(list)
for key, value in dictsample:
    defdict[key].append(value)
print(defdict.items())



deq = collections.deque([1, 2, 3])
print(deq)
deq.append(4)
print(deq)
deq.appendleft(0)
print(deq)
deq.pop()
print(deq)
deq.popleft()
print(deq)



def add_right(deque, a):
    deque.append(a)

def add_left(deque, a):
    deque.appendleft(a)

def delete_right(deque):
    deque.pop()

def delete_left(deque):
    deque.popleft()

deque = collections.deque([])
add_right(deque, 1)
print(deque)
add_left(deque,0)
print(deque)
delete_right(deque)
print(deque)
delete_left(deque)
print(deque)
