import pandas as pd

new_dict = {'ДАТА': [], 'НАИМЕНОВАНИЕ': [], 'БРЕНД': [], 'АРТИКУЛ': [], 'КЛИЕНТ': [], 'КОЛИЧЕСТВО': [], 'ЦЕНА': [],
                'СУММА': [], 'ПРОДАЖА': [],
                'СУММА ПРОДАЖИ': [], 'Unnamed: 10': None, 'СКЛАД': [], 'Unnamed: 12': None, 'Unnamed: 13': None,
                'ПРИМЕЧАНИЕ': [], 'НОМЕР ЗАКАЗА': []}

head_file = pd.read_excel('Склад17.xlsx', header=None)

for x in head_file[0]:
    if str(x) != 'NaT':
        new_dict['ДАТА'].append(str(x))

len_index = head_file.index.stop
for i in range(0, len_index, 2):
    new_dict['АРТИКУЛ'].append(head_file.loc[[i], 2].values[0].split(',')[0])

for i in range(0, len_index, 2):
    new_dict['БРЕНД'].append(head_file.loc[[i], 2].values[0].split(',')[1].split(':')[1])

for i in range(1, len_index, 2):
    new_dict['НАИМЕНОВАНИЕ'].append(head_file.loc[[i], 2].values[0])

for i in range(0, len_index, 2):
    new_dict['КОЛИЧЕСТВО'].append(int(head_file.loc[[i], 3].values[0]))

for i in range(0, len_index, 2):
    new_dict['ЦЕНА'].append(int(head_file.loc[[i], 4].values[0]))

for i in range(0, len_index, 2):
    new_dict['СУММА'].append(int(head_file.loc[[i], 5].values[0]))

for i in range(0, len_index, 2):
    new_dict['ПРИМЕЧАНИЕ'].append(head_file.loc[[i], 8].values[0])

len_max = len(new_dict['ДАТА'])
for x in new_dict.values():
    if x is None:
        pass
    else:
        if len(x) < len_max:
            quantity = len_max - len(x)
            for i in range(quantity):
                x.append(None)

print(new_dict)



# print(new_dict)
# for i in range(0, len_index, 2):
#     print(head_file[2])
# for i in head_file[2].index:
#     print()