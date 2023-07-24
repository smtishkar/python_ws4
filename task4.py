# Функция получает на вход список чисел. 
# Отсортируйте его элементы in place без использования встроенных в язык сортировок. 
# Как вариант напишите сортировку пузырьком. 
# Её описание есть в википедии.



from typing import List


def sort_namber(nambers: List[int]) -> None:
    for i in range(len(nambers)):
        for j in range(i, len(nambers)):
            if nambers[i] > nambers[j]:
                nambers[i], nambers[j] = nambers[j], nambers[i]


namber: List[int] = [7, 954, 91, 37, 7, 1, -4, 6]

print(namber)

sort_namber(namber)

print(namber)