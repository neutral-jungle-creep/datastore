'''
DOCSTRING:Принимает список строк с заменяемыми словами и строку со словом на которое требуется их заменить.
Создает отчет о выдаче человеческого запроса с введенным словом и при его изменении.
Может быть использована как импортируемый модуль.
'''
from loguru import logger
import functions
from pathlib import Path


def v2_change_word_report(file: str, o_words: list[str], n_word: str) -> None:
    '''Запишет в файлы результаты выдачи до и после изменения слова в человеческом запросе.'''
    new_data = []
    functions.make_dir('reports_v2_search')
    data = functions.read(file)[:-1]  # убрать последнюю пустую строку
    for line in data:
        query = line.split("|")[0]
        result_search_word = functions.search_word(o_words, query)
        if result_search_word[0]:
            request_old, request_new = query, query.replace(result_search_word[1], n_word)
            logger.debug(f'Старый запрос: {request_old}; Новый запрос: {request_new}')
            new_data.append(f'{functions.format_report(functions.request_v2(request_old))}|'
                            f'{functions.format_report(functions.request_v2(request_new))}\n')
    functions.head = 'name|query|shardKey|new name|new query|new shardKey\n'
    functions.write(Path('reports_v2_search', functions.format_report_name(file, o_words)), new_data)
    logger.debug(f'В файл v2_{n_word} записано {len(new_data)} строк')


def main():
    logger.add('logs.log')
    file_name = input('Название файла: ')
    old_words = input('Заменяемые слова: ').split()  # слова, которые будет искать скрипт в файле в колонке Query
    new_word = input('Новое слово: ')  # слово, на которое скрипт заменит найденное старое
    v2_change_word_report(file_name, old_words, new_word)


if __name__ == '__main__':
    main()
