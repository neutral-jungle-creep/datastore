'''
DOCSTRING: Ищет записи с введенной подстрокой в человеческом запросе.
Принимает название файла без расширения и слово для поиска.
Возвращает файл search_word_{file_name}.csv, содержащий только выбранные строки.
'''
from loguru import logger
import read_write


def main(func=None) -> None:
    '''Запишет в файл с именем 'search_word_{file_name}.csv строки с введенным словом.'''
    data = read_write.read(file_name)
    for line in data:
        query = line[1:line.index(')')].split()
        if word_for_search in query:
            new_data.append(line)
            logger.info(f'запрос, прошедший проверку: {query}')
    if func is not None:
        func(file_name, new_data)


if __name__ == '__main__':
    logger.add('logs.log')
    file_name = input('Название файла: ')  # название файла
    word_for_search = input('Слово: ')  # слово, которое будет искать скрипт в файле в колонке Query
    new_data = []
    main(read_write.write)