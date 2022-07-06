'''
DOCSTRING: Удаляет из файла все строки, содержащие введенную подстроку.
Принимает название файла без расширения и строку.
Возвращает файл del_lines_{file_name} с отредактированными строками.
'''
from loguru import logger
import functions


def main(word: str) -> None:
    '''Запишет в файл с именем del_lines_{file_name}.csv коллекцию строк,
    не содержащих в человеческом запросе введенного слова.'''
    counter_del = 0  # считает удаленные строки
    data = functions.read(file_name)
    for line in data:
        if not functions.search_word(word, line):
            new_data.append(line)
        else:
            logger.info(f'Человеческий запрос с введенным словом = {line[:line.index(")") + 1]}')
            logger.info(f'Удаленная строка - {line}')
            counter_del += 1
    logger.debug(f'Удалено {counter_del} строк со словом {word}')
    functions.write(f'del_lines_{file_name}', new_data)


if __name__ == '__main__':
    logger.add('logs.log')
    file_name = input('Название файла: ')  # название файла
    word_del = input('Слово: ')  # слово, которое будет искать скрипт в файле в колонке Query
    new_data = []
    main(word_del)