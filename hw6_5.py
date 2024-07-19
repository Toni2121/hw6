# a
list1: list[int] = [_ for _ in range(1,5)]

# b
while True:
    try:
        input_num : int = int(input("please enter a nummber: "))
        if input_num == -999:
            break
        else:
            list1.append(input_num)
        print(list1)
    except Exception as e:
        print(f"somthing went wrong... ---{e}--- please try again")
