'''
DOCSTRING: Ищет записи, имеющие в человеческом запросе хотя бы одно из списка введенных слов.
Принимает полный путь к файлу c названием без расширения и список слов для поиска через пробел.
Записывает в папку reports_search файл {file_name}_{words}.csv, содержащий только выбранные строки.
'''
from loguru import logger
import functions
from pathlib import Path


def search_lines_report(file: str, words: list[str]) -> None:
    '''Запишет в файл с именем '{file_name}_{words}.csv строки с введенными словами.'''
    functions.make_dir('reports_search')
    data = functions.read(file)
    new_data = []
    for line in data:
        query = line.split("|")[0]
        result_search_word = functions.search_word(words, query)
        if result_search_word[0]:
            new_data.append(line)
            logger.info(f'запрос, прошедший проверку: {query}')
    functions.write(Path('reports_search', name := functions.format_report_name(file, words)), new_data)
    logger.debug(f'В файл {name} записано {len(new_data)} строк')


def main():
    logger.add('logs.log')
    file_name = input('Путь к файлу: ')  # путь к файлу
    words_search = input('Слова: ').split()  # слова, которые будет искать скрипт в файле в колонке Query
    search_lines_report(file_name, words_search)


if __name__ == '__main__':
    main()