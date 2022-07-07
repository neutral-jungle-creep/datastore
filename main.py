'''
DOCSTRING:
1. сандали - искать по ручке запрос с двумя И вместо одной
1.1 если онлайн поиск, править запись
1.2 иначе удалить запись
'''
import functions
from loguru import logger


def mine() -> None:
    data = functions.read(file_name)
    head = functions.head
    for line in data:
        if functions.search_word(old_word, line):
            result_code = analiz(line)

    functions.head = 'name|query|shardKey|new name|new query|new shardKey\n'
    functions.write('C:\\CodePy\\wb\\datastore\\main_reports\\additional_search', additional_search)
    functions.write('C:\\CodePy\\wb\\datastore\\main_reports\\merger', merger)
    functions.write('C:\\CodePy\\wb\\datastore\\main_reports\\delete', delete)


def analiz(line: str) -> int:
    '''Примет строку из коллекции с данными. Вернет код результата полученный из ручки v2 по запросу с новым словом.
    1 - допоиск; 2 - онлайн поиск; 3 - остальное(бренд, пересет, каталожная выдача)'''
    query = line[1:line.index(')')]
    request_old = functions.request_v2(query)
    request_new = functions.request_v2(query.replace(old_word, new_word))
    logger.info(f'old query: {request_old} | new query: {request_new}\n')
    if '&_t0=' in request_new["query"]:
        report(additional_search, request_old, request_new)
        return 1
    elif '&_t1=' in request_new["query"]:
        report(merger, request_old, request_new)
        return 2
    else:
        report(delete, request_old, request_new)
        return 3


def report(word: list, old: dict, new: dict) -> None:
    '''Примет название коллекции и два словаря, добавит в коллекцию отформатированный отчет'''
    word.append(f'{functions.format_report(old)}|{functions.format_report(new)}\n')


if __name__ == '__main__':
    logger.add('logs.log')
    file_name = input('Название файла: ')  # название файла
    old_word = input('Заменяемое слово: ')  # слово, которое будет искать скрипт в файле в колонке Query
    new_word = input('Новое слово: ')  # слово, на которое скрипт заменит найденное старое
    new_data = []
    additional_search, merger, delete = [], [], []
    mine()