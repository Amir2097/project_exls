import glob
import os
import re
import pandas as pd
from sys import platform
from sample import sample
import datetime

return_list = []


def extract_all_files(folders_ex):
    """
    Функция для поиска и добавления файлов по которым будет производиться извлечение данных
    :return: Список файлов с полными путями
    """
    files_list = []
    for file in sorted(glob.glob(f'{folders_ex}/Склад[0-9]*.xls*')):
        files_list.append(os.path.join(folders_ex, file))

    return files_list


def read_xlsx(folders_read=os.path.abspath(os.curdir)):
    """

    :return:
    """

    global head_file, current_warehouse_number

    colnames = ['ДАТА', 'НАИМЕНОВАНИЕ', 'БРЕНД', 'АРТИКУЛ', 'КЛИЕНТ', 'КОЛИЧЕСТВО', 'ЦЕНА', 'СУММА', 'ПРОДАЖА',
                'СУММА ПРОДАЖИ', 'Unnamed: 10', 'СКЛАД', 'Unnamed: 12', 'Unnamed: 13', 'ПРИМЕЧАНИЕ', 'НОМЕР ЗАКАЗА']

    if platform == "linux" or platform == "linux2":
        head_file = pd.read_excel(f'{folders_read}/Главный.xlsx')
        head_file.columns = colnames  # Переименование столбцов

    elif platform == "darwin":
        pass
    elif platform == "win32":
        head_file = pd.read_excel(f'{folders_read}\Главный.xlsx')
        head_file.columns = colnames  # Переименование столбцов

    new_dict = {'ДАТА': [], 'НАИМЕНОВАНИЕ': [], 'БРЕНД': [], 'АРТИКУЛ': [], 'КЛИЕНТ': [], 'КОЛИЧЕСТВО': [], 'ЦЕНА': [],
                'СУММА': [], 'ПРОДАЖА': [],
                'СУММА ПРОДАЖИ': [], 'Unnamed: 10': None, 'СКЛАД': [], 'Unnamed: 12': None, 'Unnamed: 13': None,
                'ПРИМЕЧАНИЕ': [], 'НОМЕР ЗАКАЗА': []}

    for store in extract_all_files(folders_read):

        pattern = re.compile(r"[0-9]+")

        if platform == "linux" or platform == "linux2":
            current_warehouse_number = pattern.findall(((store.split(r'/')[-1]).split('.')[0]))[0]
        elif platform == "darwin":
            pass
        elif platform == "win32":
            current_warehouse_number = pattern.findall(((store.split(r'\\')[-1]).split('.')[0]))[0]

        return_list.append(current_warehouse_number)

        read_excel_store = pd.read_excel(store)

        if "Unnamed" in str(read_excel_store.columns[0]):
            read_excel_store = pd.read_excel(store, skiprows=2)
        else:
            read_excel_store = pd.read_excel(store)

        if type(read_excel_store.columns.values[0]) == datetime.datetime:
            sample(store, new_dict, current_warehouse_number)

        else:
            for fuck in read_excel_store.columns:
                if 'дата' in fuck.lower():
                    date_store = read_excel_store[fuck]
                    for i in date_store:
                        if len(i) > 9:
                            ii = i.split(' ')[0].split('-')
                            form_ii = f'{ii[2]}.{ii[1]}.{ii[0]}'
                            new_dict['ДАТА'].append(form_ii)

                        if len(i) == 8:
                            ii = i.split('.')
                            form_ii = f'{ii[0]}.{ii[1]}.20{ii[2]}'
                            new_dict['ДАТА'].append(form_ii)
                        new_dict['СКЛАД'].append(current_warehouse_number)

                if 'наим' in fuck.lower() or 'описание' in fuck.lower():
                    title_store = read_excel_store[fuck]
                    for i in title_store:
                        new_dict['НАИМЕНОВАНИЕ'].append(i)

                if 'бренд' in fuck.lower():
                    brand_store = read_excel_store[fuck]
                    for i in brand_store:
                        new_dict['БРЕНД'].append(i)

                if 'артик' in fuck.lower() or 'код дет' in fuck.lower():
                    article_store = read_excel_store[fuck]
                    for i in article_store:
                        new_dict['АРТИКУЛ'].append(i)

                if 'клиент' in fuck.lower():
                    client_store = read_excel_store[fuck]
                    for i in client_store:
                        new_dict['КЛИЕНТ'].append(i)

                if 'колич' in fuck.lower() or 'кол-во' in fuck.lower() or 'зак.' in fuck.lower():
                    quantity_store = read_excel_store[fuck]
                    for i in quantity_store:
                        new_dict['КОЛИЧЕСТВО'].append(i)

                if 'цена' in fuck.lower():
                    price_store = read_excel_store[fuck]
                    for i in price_store:
                        new_dict['ЦЕНА'].append(i)

                if 'сумма' == fuck.lower() or 'cумма, руб.' == fuck.lower():
                    summ_store = read_excel_store[fuck]
                    for i in summ_store:
                        new_dict['СУММА'].append(i)

                if 'продажа' == fuck.lower():
                    summ_store = read_excel_store[fuck]
                    for i in summ_store:
                        new_dict['ПРОДАЖА'].append(i)

                if 'сумма прод' in fuck.lower():
                    summ_buy_store = read_excel_store[fuck]
                    for i in summ_buy_store:
                        new_dict['СУММА ПРОДАЖИ'].append(i)

                if 'прим' in fuck.lower() or 'ваш комм' in fuck.lower():
                    note_store = read_excel_store[fuck]
                    for i in note_store:
                        new_dict['ПРИМЕЧАНИЕ'].append(i)

                if 'номер зак' in fuck.lower() or '№' in fuck.lower():
                    number_store = read_excel_store[fuck]
                    for i in number_store:
                        new_dict['НОМЕР ЗАКАЗА'].append(i)

            len_max = len(new_dict['ДАТА'])
            for x in new_dict.values():

                if x is None:
                    pass
                else:
                    if len(x) < len_max:
                        quantity = len_max - len(x)
                        for i in range(quantity):
                            x.append(None)

    if platform == "linux" or platform == "linux2":
        fd = pd.DataFrame(new_dict)
        fd.to_excel(f'{folders_read}/sample.xlsx', index=False)
        reads_exc = pd.read_excel(f'{folders_read}/sample.xlsx')

        xs = pd.DataFrame()
        xs = pd.concat([head_file, reads_exc])
        xs.to_excel(f'{folders_read}/Главный.xlsx', index=False)
    elif platform == "darwin":
        pass
    elif platform == "win32":
        fd = pd.DataFrame(new_dict)
        fd.to_excel(f'{folders_read}\sample.xlsx', index=False)
        reads_exc = pd.read_excel(f'{folders_read}\sample.xlsx')

        xs = pd.DataFrame()
        xs = pd.concat([head_file, reads_exc])
        xs.to_excel(f'{folders_read}\Главный.xlsx', index=False)

    return [return_list]


if __name__ == '__main__':
    read_xlsx()
