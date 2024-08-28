# Стиль кода часть II. Цикл While.

my_list : list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(my_list)
i : int = 0
print("Исходные данные:", my_list)
print("Положительные числа, пока не встретили отрицательное или не закончился список (выход за границу):")
while i <= len(my_list):
    if my_list[i] == 0:
        i += 1
    elif my_list[i] > 0 :
        print(my_list[i])
        i += 1
        continue
    else:
        break
