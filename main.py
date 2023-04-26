import glob
import os
import pandas as pd


def folders(dirxlsx=None):
    """
    Функция возвращает форматированый путь до рабочей директории
    :param dirxlsx: Путь до рабочей директории (если None то возвращается путь текущей директории)
    :return: Магия
    """

    if dirxlsx is None:
        ref_dir = os.path.abspath(os.curdir)
    else:
        ref_dir = dirxlsx

    return ref_dir


def extract_all_files(folders_ex):
    """
    Функция для поиска и добавления файлов по которым будет производиться извлечение данных
    :return: Список файлов с полными путями
    """
    files_list = []
    for file in sorted(glob.glob(f'{folders(folders_ex)}/Склад[0-9]*.xls*')):
        print(file)
        files_list.append(os.path.join(folders(), file))

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
