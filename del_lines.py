import functions
from loguru import logger


def rewrite_file(file: str, data: list) -> None:
    ''''''
    functions.write(f'{file}.csv', data)


def del_lines(file: str, words: list) -> list:
    '''Примет путь к файлу и список слов для поиска. Вернет коллекцию с данными датастора без выключенных
    строк, в которых есть хотя бы одно из списка слов.'''
    data = functions.read(f'{file}.csv')
    new_data = []
    for line in data:
        if functions.search_word(words,line) and 'no' == line.split('|'):
            logger.debug(f'Удалена строка {line}')
        else:
            new_data.append(line)
    return new_data


def main() -> None:
    logger.add('logs.log')
    file_name = input('Путь к файлу: ')  # путь к файлу
    words_search = input('Слова: ').split()  # слова, которые будет искать скрипт в файле
    data = del_lines(file_name, words_search)
    rewrite_file(file_name, data)


if __name__ == '__main__':
    main()