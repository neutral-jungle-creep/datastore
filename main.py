'''
DOCSTRING: Принимает путь к файлу с его именем без расширения, список слов, которые нужно заменить,
и строку, на которую нужно их заменить. Если онлайн поиск или допоиск, правит имеющуюся запись, иначе удаляет запись.
В папке reports_main хранятся отчеты: edit_preset_{new_word} - записи, которые были отредактированы,
del_preset_{new_word} - записи, которые были удалены.
'''
import functions
from loguru import logger


def mine() -> None:
    '''Запишет два файла с отчетами в папку reports_main и перепишет файл в папке датастора по введенному
     в начале программы пути.'''
    functions.make_dir('reports_main')
    data = functions.read(file_name)
    logger.debug(f'Прочитано {len(data)} строк')
    head = functions.head
    for line in data:
        result_search_word = functions.search_word(old_words, line)
        if result_search_word[0]:
            if analiz(result_search_word[1], line):
                new_data.append(functions.change_word(result_search_word[1], new_word, line))
        else:
            new_data.append(line)

    functions.head = 'name|query|shardKey|new name|new query|new shardKey\n'
    functions.write(f'reports_main\\edit_preset_{new_word}', edit_preset)
    functions.write(f'reports_main\\del_preset_{new_word}', del_preset)

    functions.head = head
    functions.write(file_name, new_data)
    logger.debug(f'В файл {file_name} записано {len(new_data)} строк')
    logger.debug(f'Удалено {len(data) - len(new_data)} строк')


def analiz(old_word: str, line: str) -> int:
    '''Примет неверное слово и строку из коллекции с данными файла датастора. Вернет код результата
    полученный из ручки v2 по запросу с новым словом. 1 - допоиск и онлайн поиск;
    0 - остальное(бренд, каталог, пресет).'''
    query = line.split('|')[0].replace(')', '').replace('(', '')
    logger.info(f'Проверка человеческого запроса: ({query})')
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
    '''Примет название коллекции и два словаря с отчетами экзакта, добавит в коллекцию отформатированную строку'''
    word.append(f'{functions.format_report(old)}|{functions.format_report(new)}\n')


if __name__ == '__main__':
    logger.add('logs.log')
    file_name = input('Путь к файлу: ')  # путь к файлу C:\\Pепозиторий\\datastore-1\\indices\\presets
    old_words = input('Заменяемое слово: ').split()  # слова, которые будет искать скрипт в файле в колонке Query
    new_word = input('Новое слово: ')  # слово, на которое скрипт заменит найденное старое
    new_data, edit_preset, del_preset = [], [], []
    mine()
