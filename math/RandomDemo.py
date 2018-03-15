import random

print(random.random())

print(random.uniform(1, 10))

print(random.uniform(10, 1))

print(random.randint(11,20))
print(random.randint(20,20))

print(random.randrange(10,18,2))

print(random.choice("Pythontab.com"))
print(random.choice(["python", "tab", "com"]))
print(random.choice(("python", "tab", "com")))

list = [1, 2,3 ,4, 5, 6, 7, 8, 9, 10]
random.shuffle(list)
print(list)

slice = random.sample(list, 3)
print(slice)
print(list)