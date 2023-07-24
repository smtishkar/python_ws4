# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии. 


def dict_bonus(*args):
    result_dict = {}
    for name, salary, bonus in zip(*args):
        result_dict[name] = (salary * float(bonus[:-1]))/100
    return result_dict


name = ['Вадим', 'Сергей', 'Андрей']
salary = [100_000, 150_000, 130_000]
bonus = [ '10.25%', '5.55%', '6.89%']

print(dict_bonus(name,salary,bonus))