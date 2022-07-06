'''
DOCSTRING: Ищет записи с введенной подстрокой в человеческом запросе.
Принимает название файла без расширения и слово для поиска.
Возвращает файл search_word_{file_name}.csv, содержащий только выбранные строки.
'''
from loguru import logger
import functions


def main(word: str) -> None:
    '''Запишет в файл с именем 'search_word_{file_name}.csv строки с введенным словом.'''
    data = functions.read(file_name)
    for line in data:
        if functions.search_word(word, line):
            new_data.append(line)
            logger.info(f'запрос, прошедший проверку: {line[:line.index(")") + 1]}')
    functions.write('search_word', new_data)


if __name__ == '__main__':
    logger.add('logs.log')
    file_name = input('Название файла: ')  # название файла
    word_search = input('Слово: ')  # слово, которое будет искать скрипт в файле в колонке Query
    new_data = []
    main(word_search)