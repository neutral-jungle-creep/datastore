'''
DOCSTRING: Ищет записи, имеющие в человеческом запросе хотя бы одно из списка введенных слов.
Принимает полный путь к файлу c названием без расширения и список слов для поиска через пробел.
Записывает в папку reports_search файл {file_name}_{words}.csv, содержащий только выбранные строки.
'''
from loguru import logger
import functions
from pathlib import Path


def main(words: list[str]) -> None:
    '''Запишет в файл с именем '{file_name}_{words}.csv строки с введенными словами.'''
    functions.make_dir('reports_search')
    data = functions.read(file_name)
    new_data = []
    for line in data:
        result_search_word = functions.search_word(words, line)
        if result_search_word[0]:
            new_data.append(line)
            logger.info(f'запрос, прошедший проверку: {line.split("|")[0]}')
    name = '_'.join(file_name.split('\\')[-3::2])
    word = '_'.join([word for word in words])
    functions.write(Path('reports_search', f'{name}_{word}.csv'), new_data)
    logger.debug(f'В файл {name}_{word} записано {len(new_data)} строк')


if __name__ == '__main__':
    logger.add('logs.log')
    file_name = input('Путь к файлу: ')  # путь к файлу C:\\Pепозиторий\\datastore-1\\indices\\presets
    words_search = input('Слова: ').split()  # слова, которые будет искать скрипт в файле в колонке Query
    main(words_search)