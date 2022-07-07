'''
DOCSTRING: Ищет записи с введенной подстрокой в человеческом запросе.
Принимает название файла без расширения и слово для поиска.
Возвращает файл search_word_{word}.csv, содержащий только выбранные строки.
'''
from loguru import logger
import functions


def main(word: str) -> None:
    '''Запишет в файл с именем 'search_word_{word}.csv строки с введенным словом.'''
    data = functions.read(file_name)
    new_data = []
    for line in data:
        if functions.search_word(word, line):
            new_data.append(line)
            logger.info(f'запрос, прошедший проверку: {line[:line.index(")") + 1]}')
    functions.write(f'search_word_{word}', new_data)
    logger.debug(f'В файл search_word_{word} записано {len(new_data)} строк')


if __name__ == '__main__':
    logger.add('logs.log')
    file_name = input('Путь к файлу: ')  # путь к файлу C:\\Pепозиторий\\datastore-1\\indices\\presets
    word_search = input('Слово: ')  # слово, которое будет искать скрипт в файле в колонке Query
    main(word_search)