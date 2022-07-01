'''
DOCSTRING: Удаляет из файла все строки, содержащие введенную подстроку.
Принимает название файла без расширения и строку.
Если сценарий вызван как импортируемый, возвращает коллекцию строк.
Иначе возвращает файл del_lines_{file_name} с отредактированными строками.
'''
from loguru import logger


def read_file(word: str, file: str, func=None) -> list:
    '''
    Вернет коллекцию строк, не содержащих в человеческом запросе введенного слова.
    Если сценарий запущен как импортируемый модуль, передавать именованный аргумент не требуется.
    '''
    counter_del = 0  # считает удаленные строки
    with open(f'{file}.csv', 'r', encoding='utf-8') as data:
        global head
        head = data.readline()  # первая строка
        logger.debug(f'Первая строка = {head}')
        for line in data.readlines():
            query = line[1:line.index(')')].split()
            if word not in query:
                new_data.append(line)
            else:
                logger.info(f'Человеческий запрос с выбранным словом = {query}')
                logger.info(f'Удаленная строка - {line}')
                counter_del += 1
        logger.debug(f'Удалено {counter_del} строк со словом {word}')
        if func is not None:
            logger.debug(f'Запуск функции write')
            func()
        return new_data


def write_file() -> None:
    '''Запишет в файл del_lines_{file}.csv отредактированную коллекцию строк.'''
    with open(f'del_lines_{file_name}.csv', 'w', encoding='utf-8') as data_output:
        data_output.write(head)
        data_output.writelines(new_data)
        logger.debug(f'В файл del_lines_{file_name}.csv записано {len(new_data) + 1} строк')


new_data = []


if __name__ == '__main__':
    logger.add('logs.log')
    word_del = input('Слово: ')  # слово, которое будет искать скрипт в файле в колонке Query
    file_name = input('Название файла: ')  # название файла (presets)
    read_file(word_del, file_name, write_file)