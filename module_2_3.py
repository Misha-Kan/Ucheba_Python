my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
it = 0
while it < len(my_list):
    if my_list[it] < 0:
        break
    elif my_list[it] == 0:
        it += 1
        continue
    elif my_list[it] > 0:
        print(my_list[it])
        it += 1


