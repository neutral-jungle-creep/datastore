'''
DOCSTRING: Ищет записи с введенной подстрокой в человеческом запросе.
Принимает название файла без расширения и слово для поиска.
Записывает в папку reports_search файл {dir}_{file_name}_{word}.csv, содержащий только выбранные строки.
'''
from loguru import logger
import functions
from pathlib import Path


def main(word: str) -> None:
    '''Запишет в файл с именем 'search_word_{word}.csv строки с введенным словом.'''
    functions.make_dir('reports_search')
    data = functions.read(file_name)
    new_data = []
    for line in data:
        if functions.search_word(word, line):
            new_data.append(line)
            logger.info(f'запрос, прошедший проверку: {line[:line.index(")") + 1]}')
    name = '_'.join(file_name.split('\\')[-3::2])
    functions.write(f'reports_search\\{name}_{word}', new_data)
    logger.debug(f'В файл {name}_{word} записано {len(new_data)} строк')


if __name__ == '__main__':
    logger.add('logs.log')
    file_name = input('Путь к файлу: ')  # путь к файлу C:\\Pепозиторий\\datastore-1\\indices\\presets
    word_search = input('Слово: ')  # слово, которое будет искать скрипт в файле в колонке Query
    main(word_search)