def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(1, 3, 5)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = 2500, 'НЕ_число', False
values_dict = {'a': 2024, 'b':"август",'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = 1564257, 'Это проверка '
print_params(*values_list_2, 42)
