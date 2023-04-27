import csv
import glob
import os
import pandas as pd


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
                'СУММА ПРОДАЖИ', '      ', 'СКЛАД', '      ', '      ', 'ПРИМЕЧАНИЕ', 'НОМЕР ЗАКАЗА']

    head_file = pd.read_excel('Главный.xlsx')
    head_file.columns = colnames  # Переименование столбцов


    for store in extract_all_files(folders_read):

        read_excel_store = pd.read_excel(store)

        if "Unnamed" in str(read_excel_store.columns[0]):
            read_excel_store = pd.read_excel(store, skiprows=2)
        else:
            read_excel_store = pd.read_excel(store)

        for fuck in read_excel_store.columns:

            if 'дата' in fuck.lower():
                date_store = read_excel_store[fuck]


            if 'наим' in fuck.lower():
                title_store = read_excel_store[fuck]

            if 'бренд' in fuck.lower():
                brand_store = read_excel_store[fuck]

            if 'артик' in fuck.lower() or 'код дет' in fuck.lower():
                article_store = read_excel_store[fuck]

            if 'клиент' in fuck.lower():
                client_store = read_excel_store[fuck]

            if 'колич' in fuck.lower() or 'кол-во' in fuck.lower():
                quantity_store = read_excel_store[fuck]

            if 'цена' in fuck.lower():
                price_store = read_excel_store[fuck]

            if 'сумма' == fuck.lower():
                summ_store = read_excel_store[fuck]

            if 'сумма прод' in fuck.lower():
                summ_buy_store = read_excel_store[fuck]

            if 'склад' == fuck.lower():
                store_store = read_excel_store[fuck]

            if 'прим' in fuck.lower() or 'ваш комм' in fuck.lower():
                note_store = read_excel_store[fuck]

            if 'номер зак' in fuck.lower() or '№' in fuck.lower():
                number_store = read_excel_store[fuck]

        # ------------------------------------------

        # with open('sw_data_new.csv', 'w') as f:
        #     writer = csv.writer(f)
        #     for row in str(read_excel_store):
        #         writer.writerow(row)

        # ------------------------------------------


if __name__ == '__main__':
    read_xlsx()
    # extract_all_files()
