'''
DOCSTRING: Модуль для чтения и записи в файл.
'''
from loguru import logger


def read(file: str) -> list:
    '''Примет строку - название файла. Вернет список строк из файла без строки заголовка.'''
    with open(f'C:\\Pепозиторий\\datastore-1\\indices\\{file}.csv', 'r', encoding='utf-8') as file_input:
        global head
        head = file_input.readline()
        data = file_input.readlines()
        logger.debug(f'Прочитано {len(data)} строк')
    return data


def write(file: str, data: list) -> None:
    '''Примет строку - название файла и список строк с данными. Список построчно в файл.'''
    with open(f'new_{file}.csv', 'w', encoding='utf-8') as file_output:
        file_output.write(head)
        file_output.writelines(data)
        logger.debug(f'Записано {len(data)} строк')
