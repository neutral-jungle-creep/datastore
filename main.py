'''
DOCSTRING:
'''
import search_word
import change_lines
from loguru import logger


def read_file() -> None:
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
        logger.debug(f'Новый файл будет содержать {len(new_data) + 1} строк')
        change_lines.change(word)
        write_file(head)


def write_file(head: str) -> None:
    '''Запишет в файл new_{file}.csv отредактированную коллекцию строк.'''
    with open(f'new_{file}.csv', 'w', encoding='utf-8') as data_output:
        data_output.write(head)
        data_output.writelines(new_data)
        logger.debug(f'Файл new_{file}.csv записан')


if __name__ == '__main__':
    logger.add('logs.log')
    file = search_word.file_name
    word = search_word.word_for_search
    new_data = []
    search_word.search(file)
    read_file()