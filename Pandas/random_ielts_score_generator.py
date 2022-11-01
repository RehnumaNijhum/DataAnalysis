import random

first_number = [0.5, 1.0]
rand_idx = random.randrange(len(first_number))
random_num = first_number[rand_idx]
second_number = random.randint(0, 8)

result = random_num + second_number
print(result)