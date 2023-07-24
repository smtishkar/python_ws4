# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


def sum_number(lst_numbers: list, num1: int, num2: int)-> int:
    return sum(lst_numbers[num1: num2 + 1])



my_list = [3, 6, 1, 12, 21]
print(sum_number(my_list, -21, 12))