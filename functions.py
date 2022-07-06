'''
DOCSTRING: Модуль c функциями для работы файлами датастора.
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
    '''Примет строку - название файла и список строк с данными. Запишет список построчно в файл.'''
    with open(f'{file}.csv', 'w', encoding='utf-8') as file_output:
        file_output.write(head)
        file_output.writelines(data)
        logger.debug(f'Записано {len(data)} строк')


def search_word(word: str, line: str) -> bool:
    '''Примет слово и строку. Вернет булево значение в зависимости от наличия полученной строки
     в человеческом запросе'''
    query = line[1:line.index(')')].split()
    return word in query


def change_word(o_word: str, n_word: str, line: str) -> str:
    '''Примет заменяемое слово, новое слово и строку. Вернет строку с замененной подстрокой на новую.'''
    new_line = line.replace(f'{o_word} ', f'{n_word} ').replace(f'{o_word})',
                                                                f'{n_word})').replace(f'{o_word}"', f'{n_word}"')
    logger.info(f'Новая строка - {new_line}')
    return new_line
