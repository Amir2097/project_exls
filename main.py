import csv
import glob
import os
import pandas as pd
import numpy as np


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

    colnames = ['ДАТА', 'НАИМЕНОВАНИЕ', 'БРЕНД', 'АРТИКУЛ', 'КЛИЕНТ', 'КОЛИЧЕСТВО', 'ЦЕНА', 'СУММА', 'ПРОДАЖА',
                'СУММА ПРОДАЖИ', 'Unnamed: 10', 'СКЛАД', 'Unnamed: 12', 'Unnamed: 13', 'ПРИМЕЧАНИЕ', 'НОМЕР ЗАКАЗА']

    head_file = pd.read_excel('Главный.xlsx')
    head_file.columns = colnames  # Переименование столбцов

    new_dict = {'ДАТА': [], 'НАИМЕНОВАНИЕ': [], 'БРЕНД': [], 'АРТИКУЛ': [], 'КЛИЕНТ': [], 'КОЛИЧЕСТВО': [], 'ЦЕНА': [], 'СУММА': [], 'ПРОДАЖА': [],
                'СУММА ПРОДАЖИ': [], 'Unnamed: 10': None, 'СКЛАД': [], 'Unnamed: 12': None, 'Unnamed: 13': None, 'ПРИМЕЧАНИЕ': [], 'НОМЕР ЗАКАЗА': []}

    for store in extract_all_files(folders_read):

        read_excel_store = pd.read_excel(store)
        print(store)

        if "Unnamed" in str(read_excel_store.columns[0]):
            read_excel_store = pd.read_excel(store, skiprows=2)
        else:
            read_excel_store = pd.read_excel(store)

        for fuck in read_excel_store.columns:

            if 'дата' in fuck.lower():
                date_store = read_excel_store[fuck]
                for i in date_store:
                    new_dict['ДАТА'].append(i)

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

            if 'склад' == fuck.lower():
                store_store = read_excel_store[fuck]
                for i in store_store:
                    new_dict['СКЛАД'].append(i)

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

    fd = pd.DataFrame(new_dict)
    sample = fd.to_excel('sample.xlsx')


        # ------------------------------------------

        # with open('sw_data_new.csv', 'w') as f:
        #     writer = csv.writer(f)
        #     for row in str(read_excel_store):
        #         writer.writerow(row)

        # ------------------------------------------


if __name__ == '__main__':
    read_xlsx()
    # extract_all_files()
