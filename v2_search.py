'''
DOCSTRING: Создает отчет о выдаче человеческого запроса с введенным словом и при его изменении.
Принимает строку с изменяемым словом и со словом на которое требуется заменить.
'''
from loguru import logger
import functions
from pathlib import Path


def main() -> None:
    '''Запишет в файлы результаты выдачи до и после изменения слова в человеческом запросе.'''
    functions.make_dir('reports_v2_search')
    data = functions.read(file_name)[:-1]
    for line in data:
        query = line.split("|")[0]
        result_search_word = functions.search_word(old_words, line)
        if result_search_word[0]:
            request_old = query
            logger.info(f'Старый запрос: {request_old}')
            request_new = query.replace(result_search_word[1], new_word)
            logger.debug(f'Новый запрос: {request_new}')
            new_data.append(f'{functions.format_report(functions.request_v2(request_old))}|'
                            f'{functions.format_report(functions.request_v2(request_new))}\n')
    functions.head = 'name|query|shardKey|new name|new query|new shardKey\n'
    functions.write(Path('reports_v2_search', f'v2_{new_word}'), new_data)
    logger.debug(f'В файл v2_{new_word} записано {len(new_data)} строк')


if __name__ == '__main__':
    logger.add('logs.log')
    file_name = input('Название файла: ')
    old_words = input('Заменяемые слова: ').split()  # слова, которые будет искать скрипт в файле в колонке Query
    new_word = input('Новое слово: ')  # слово, на которое скрипт заменит найденное старое
    new_data = []
    main()