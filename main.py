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

    for store in extract_all_files(folders_read):

        read_excel_store = pd.read_excel(store)

        if "Unnamed" in str(read_excel_store.columns[0]):
            read_excel_store = pd.read_excel(store, skiprows=2)
        else:
            read_excel_store = pd.read_excel(store)


        for fuck in read_excel_store.columns:
            print(fuck)

            if 'Дата' in fuck:
                print()


        # ------------------------------------------

        # with open('sw_data_new.csv', 'w') as f:
        #     writer = csv.writer(f)
        #     for row in str(read_excel_store):
        #         writer.writerow(row)

        # ------------------------------------------


if __name__ == '__main__':
    read_xlsx()
