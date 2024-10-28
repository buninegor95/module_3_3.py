def print_params(a = 1, b = 'строка', c = True, *values_list_,**values_dict_):
    print(a, b, c)

print_params()
print_params(b = 758485745)
print_params(b = 25)
print_params(c = [1,2,3])

values_list_ = [63.95, 'ночь', False]
values_dict_ = {'a1': "бобор", 'b1': 43, 'c1': True}
print_params(*values_list_, **values_dict_)

values_list_2 = [65.435, 'день']
print_params(*values_list_2, 42)