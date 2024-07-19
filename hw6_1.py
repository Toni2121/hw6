num: list[int] = []
for i in range(80,100):
    num.append(i)
print(num)
first_index = num[0]
print(f"The first index in the list is {first_index}")
last_index = num[-1]
print(f"The last index in the list is {last_index}")
list_length = len(num)
print(f"There are {list_length} indexes")
index_3_12 = num[3:13]
print(index_3_12)
index_3_end = num[3:]
print(index_3_end)
index_start_9 = num[:10]
print(index_start_9)
num.insert(10,999)
print(num)
print(num[::-1])
num.pop(11)
print(num[1::2])