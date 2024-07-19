temp: list[float] = []
while True:
    input_temp: float = float(input("please enter the temperature (enter -999 when done): "))
    if -50 < input_temp < 50:
        temp.append(input_temp)
    print(temp)

    if input_temp == -999:
        break

new_temp_list: list[float] = [-20.0, 39.1, 18.5]
temp.extend(new_temp_list)
print(temp)


print(f"highest temperature is:  {max(temp)}")
print(f"lowest temperature is:  {min(temp)}")
print(f"average temperature  is:  {sum(temp) / len(temp)}")


import statistics
print(f"the average temperature by 'statistics' is: {statistics.mean(temp) : .2f}")


del temp[0]
print(temp)


temp.remove(18.5)
print(temp)


temp_last: float = temp.pop(-1)


print(temp)
print(temp_last)


copy_temp = temp.copy()
copy_temp.sort()
print(copy_temp)
copy_temp.sort(reverse=True)
print(copy_temp)


print('After sorted', sorted(temp))
print('After reverse sorted', sorted(temp, reverse=True))
print('After list and reversed', list(reversed(temp)))
#sorted doesn't change the list unlike sort


# reversed function return iterator object
list_not_reversed = [1, 2, 3, 4, 5]
reversed_iterator = reversed(list_not_reversed)
reversed_list = list(reversed_iterator)
print(reversed_list)
