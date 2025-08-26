import itertools

items = [1, 2, 3, 4]
for i in itertools.combinations(items, 2):
    print(i)

for p in itertools.permutations("Python"):
    print(p)

a = ["a", "b"]
b = [1, 2, 3]
c = ["x", "y"]
count = 0
for item in itertools.cycle(itertools.chain(a, b, c)):
    if count == 5:
        break
    print(item)
    count += 1

def fib():
  f1,f2 = 1,1
  while True:
    yield f1
    f1,f2 = f2,f1+f2
print(list(itertools.islice(fib(), 10)))

l = list(itertools.product(['red', 'blue'],['shirt', 'shoes']))
for i in range(len(l)):
    print(l[i])