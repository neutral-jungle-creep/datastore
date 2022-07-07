'''
DOCSTRING: Принимает название файла без расширения, строку, которую заменить, и строку, на которую заменить.
Если онлайн поиск, правит имеющуюся запись
1.2 иначе удалить запись
'''
import functions
from loguru import logger
# 554486 554523

def mine() -> None:
    '''Запишет два файла с отчетами в папку main_reports и измененный файл с пресетами presets.csv.'''
    data = functions.read(file_name)
    head = functions.head
    for line in data:
        if functions.search_word(old_word, line):
            if analiz(line):
                new_data.append(functions.change_word(old_word, new_word, line))
        else:
            new_data.append(line)

    functions.head = 'name|query|shardKey|new name|new query|new shardKey\n'
    functions.write('C:\\CodePy\\wb\\datastore\\main_reports\\edit_preset', edit_preset)
    functions.write('C:\\CodePy\\wb\\datastore\\main_reports\\del_preset', del_preset)

    functions.head = head
    functions.write(file_name, new_data)
    logger.debug(f'Удалено {len(data) - len(new_data)} строк')


def analiz(line: str) -> int:
    '''Примет строку из коллекции с данными. Вернет код результата полученный из ручки v2 по запросу с новым словом.
    1 - допоиск и онлайн поиск; 0 - остальное(бренд, каталог, пресет).'''
    query = line[1:line.index(')')]
    request_old = functions.request_v2(query)
    request_new = functions.request_v2(query.replace(old_word, new_word))
    logger.info(f'old query: {request_old} | new query: {request_new}\n')
    if '_t0=' in request_new["query"]:
        report(edit_preset, request_old, request_new)
        return 1
    else:
        report(del_preset, request_old, request_new)
        return 0


def report(word: list, old: dict, new: dict) -> None:
    '''Примет название коллекции и два словаря, добавит в коллекцию отформатированный отчет'''
    word.append(f'{functions.format_report(old)}|{functions.format_report(new)}\n')


if __name__ == '__main__':
    logger.add('logs.log')
    file_name = input('Название файла: ')  # название файла
    old_word = input('Заменяемое слово: ')  # слово, которое будет искать скрипт в файле в колонке Query
    new_word = input('Новое слово: ')  # слово, на которое скрипт заменит найденное старое
    new_data, edit_preset, del_preset = [], [], []
    mine()