import random

# a
list1 = [_ * 1 for _ in range(95, 106)]
print(list1)

# b
list2 = [_ for _ in range(10, 21, 2)]
print(list2)

# c
list3 = [random.choice([True, False]) for _ in range(1, 6)]
print(list3)

# d
# you should use variable "_" when you don't want to use extra variable and you use it
# only because you have to. helps by reducing the amount of code and you will know later on
# that you used this variable just because you had to.

# e
list4 = [random.randint(1,100) for _ in range(1, 11)]
print(list4)

# f
list5: list[int] = [n for n in list4 if n > 50]
print(list5)

# g
list6: list[int] = [n for n in [random.randint(1,100) for _ in range(1, 11)] if n > 50]
print(list6)

# h
str1 = input("please enter a string: ")
list7: list[str] = [char for char in str1 if char != "t" and char != " "]
print(list7)