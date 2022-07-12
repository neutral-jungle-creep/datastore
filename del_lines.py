import functions
from loguru import logger


def rewrite_file(file: str, data: list, lines: list) -> None:
    '''Перепишет файл датастора, запишет файл отчета.'''
    functions.write(f'{file}.csv', data)
    functions.write(name := functions.format_report_name(f'{file}', ['del']), lines)
    logger.debug(f'В файл {file} записано {len(data)} строк')
    logger.debug(f'В файл {name} записано {len(lines)} строк')


def del_lines(file: str, words: list) -> tuple:
    '''Примет путь к файлу и список слов для поиска. Вернет коллекцию с данными датастора без выключенных
    строк, в которых есть хотя бы одно из списка слов.'''
    data = functions.read(f'{file}.csv')
    lines = []
    logger.debug(f'Прочитано {len(data)} строк')
    new_data = []
    for line in data:
        if functions.search_word(words, line)[0] and 'no' == line.split('|')[2]:
            logger.info(f'Удалена строка {line}')
            lines.append(line)
        else:
            new_data.append(line)
    logger.debug(f'Удалено {len(data) - len(new_data)} строк')
    return new_data, lines


def main() -> None:
    logger.add('logs.log')
    file_name = input('Путь к файлу: ')  # путь к файлу
    words_search = input('Слова: ').split()  # слова, которые будет искать скрипт в файле
    result = del_lines(file_name, words_search)
    rewrite_file(file_name, result[0], result[1])


if __name__ == '__main__':
    main()