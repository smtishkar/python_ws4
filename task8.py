# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


# # Recreating the variables
# tests = "test value" 
# variables = "another test value"
# s = "single letter variable"
# check = "this variable does not end with s"

# # Redefining the function
# def replace_s_variables():
#     variables_dict = globals()
#     for var_name in list(variables_dict.keys()):
#         if var_name.endswith('s') and var_name != 's':
#             new_var_name = var_name[:-1]
#             variables_dict[new_var_name] = variables_dict[var_name]
#             variables_dict[var_name] = None

# # Let's first print the initial values of variables
# print("Initial values:")
# print(f"tests: {tests}")
# print(f"variables: {variables}")
# print(f"s: {s}")
# print(f"check: {check}")

# # Calling the function
# replace_s_variables()

# # Printing the values of variables after the function execution
# print("\nValues after function execution:")
# print(f"tests: {tests}")
# print(f"variables: {variables}")
# print(f"s: {s}")
# print(f"check: {check}")

# # Printing the values of new variables
# print("\nValues of new variables:")
# print(f"test: {test}")
# print(f"variable: {variable}")





# Recreating the variables
import os

tests = "test value" 
variables = "another test value"
s = "single letter variable"
check = "this variable does not end with s"

# Redefining the function
def replace_s_variables():
    variables_dict = globals()
    for var_name in list(variables_dict.keys()):
        if var_name.endswith('s') and var_name != 's':
            new_var_name = var_name[:-1]
            variables_dict[new_var_name] = variables_dict[var_name]
            variables_dict[var_name] = None


print(f'ГЛОБАЛОЧКИ:  {globals()}')