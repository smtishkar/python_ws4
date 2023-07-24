# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.



def company_profit_calculation(my_dict):
    list_money = []
    for values in my_dict.values():
        list_money.append(sum(values)>0)
    return all(list_money)

my_dict = {'А' : [100, -200, 300],
           'Б' : [300, -100, 200],
           'В' : [200, -200, 300]
           }


print(company_profit_calculation(my_dict))