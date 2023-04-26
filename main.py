import glob
import os
import openpyxl
import pandas as pd


def folders(dirxlsx=None):
    """
    Функция принимает путь для файлов складов
    """

    if dirxlsx is None:
        ref_dir = os.path.abspath(os.curdir)
    else:
        ref_dir = dirxlsx

    return ref_dir


def extract_all_files():
    """
    Добавление всех путей в список
    :return:
    """
    files_list = []
    print(folders())
    for file in sorted(glob.glob(f'{folders()}/Склад[0-9]*.xls*')):
        print(file)
        files_list.append(os.path.join(folders(), file))

    print(files_list)
    return files_list


def read_xlsx():
    """

    :return:
    """
    for store in extract_all_files():

        file_store = pd.read_excel(store)




if __name__ == '__main__':
    read_xlsx()
    # extract_all_files()
