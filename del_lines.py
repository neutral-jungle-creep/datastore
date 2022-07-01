'''
DOCSTRING:
'''
from loguru import logger


def read_file(file: str, word: str) -> None:
    '''Запишет в коллекцию все строки, не содержащие в человеческом запросе введенное слово.'''
    counter_del = 0  # считает удаленные строки
    with open(f'{file}.csv', 'r', encoding='utf-8') as data:
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
        write_file(head)


def write_file(head: str) -> None:
    '''Запишет в файл main_{file}.csv отредактированную коллекцию строк.'''
    with open(f'main_{file}.csv', 'w', encoding='utf-8') as data_output:
        data_output.write(head)
        data_output.writelines(new_data)
        logger.debug(f'В файл main_{file}.csv записано {len(new_data) + 1} строк')


if __name__ == '__main__':
    logger.add('logs.log')
    file = input('Название файла: ')  # название файла (presets)
    word = input('Слово: ')  # слово, которое будет искать скрипт в файле в колонке Query
    new_data = []
    read_file(file, word)