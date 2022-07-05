'''
DOCSTRING: Ищет записи с введенной подстрокой в человеческом запросе.
Принимает название файла без расширения и слово для поиска.
Возвращает файл search_word_{file_name}.csv, содержащий только выбранные строки.
'''
import pandas as pd
import csv
from loguru import logger


def main(file: str) -> None:
    '''Запишет в файл с именем 'search_word_{file_name}.csv строки с введенным словом.'''
    with open(f'C:\\Pепозиторий\\datastore-1\\indices\\{file}.csv', 'r', encoding='utf-8') as file_input:
        head = file_input.readline()
        for line in file_input.readlines():
            query = line[1:line.index(')')].split()
            if word_for_search in query:
                new_data.append(line)
                logger.info(f'запрос, прошедший проверку: {query}')

    with open(f'search_word_{file_name}.csv', 'w', encoding='utf-8') as file_output:
        file_output.write(head)
        file_output.writelines(new_data)
        logger.debug(f'В файл search_word_{file}.csv записано {len(new_data)} строк со словом {word_for_search}')


word_for_search = input('Слово: ')  # слово, которое будет искать скрипт в файле в колонке Query
file_name = input('Название файла: ')  # название файла (presets)
new_data = []


if __name__ == '__main__':
    logger.add('logs.log')
    main(file_name)