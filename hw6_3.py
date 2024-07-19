import random
index_3 = 3
bool_list = [random.choice([True, False]) for _ in range(index_3)]
print(bool_list)
print("all three are True: ", all(bool_list))
print("at least one True: ", any(bool_list))
print("all three are False: ", not any(bool_list))
print("at least one is False: ", not all(bool_list))

num_list: list[int] = [random.randint(-2, 2) for _ in range(-2, 2)]
print(num_list)
print("no 0 in sight:", all(num_list))
print("at least one different from 0:", any(num_list))
print("are all 0:", not any(num_list))
print("at least one is 0:", not all(num_list))