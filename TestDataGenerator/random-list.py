import random

random_list = []

for i in range(20000):
    random_number = random.randint(1, 100000)
    random_list.append(random_number)

print(random_list)