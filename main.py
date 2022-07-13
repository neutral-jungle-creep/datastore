'''
DOCSTRING: Принимает путь к файлу с его именем без расширения, список слов, которые нужно заменить,
и строку, на которую нужно их заменить. Если онлайн поиск или допоиск, правит имеющуюся запись, иначе удаляет запись.
Запишет в директорию reports_main отчеты: edit_{old_words} - записи, которые были отредактированы,
del_{old_words} - записи, которые были удалены.
'''
import functions
from loguru import logger
from pathlib import Path


def rewrite_file():
    '''Перепишет файл датастора, запишет файлы: для проверки логов и два отчета.'''
    functions.write(f'{file_name}.csv', new_data)
    logger.debug(f'В файл {file_name} записано {len(new_data)} строк')

    functions.add_lines(Path('logs', 'new_logs.txt'), for_check)

    functions.head = 'name|query|shardKey|new name|new query|new shardKey\n'
    functions.write(Path('reports_main', functions.format_report_name(f'{file_name}_edit', old_words)), edit_preset)
    functions.write(Path('reports_main', functions.format_report_name(f'{file_name}_del', old_words)), del_preset)


def switch_no_brand(v2_result: tuple) -> int:
    query = v2_result[0]["query"]
    if brand:
        if '_t0=' in query:
            return 1
        else:
            return 0
    else:
        if '_t0=' in query or 'brand' in query:
            return 1
        else:
            return 0


def switch_yes_brand(v2_result: tuple) -> int:
    query = v2_result[1]["query"]
    if brand:
        if '_t0=' in query:
            return 1
        else:
            return 0
    else:
        if '_t0=' in query or 'brand' in query:
            return 1
        else:
            return 0


def report_main(word: list, v2_result) -> None:
    '''Примет название коллекции и два словаря с отчетами экзакта, добавит в коллекцию отформатированную строку'''
    word.append(f'{functions.format_report(v2_result[0])}|{functions.format_report(v2_result[1])}\n')


def switch(func, v2_result: tuple):
    result = func(v2_result)
    if result:
        report_main(edit_preset, v2_result)
    else:
        report_main(del_preset, v2_result)
    return result


def v2_report(old_word: str, line: str) -> tuple:
    '''Примет неверное слово и строку из коллекции с данными файла датастора. Вернет результаты,
    полученные из ручки v2 по запросу со старым и новым словом.'''
    query = functions.human_request(line)
    for_check.append(line)
    logger.info(f'Проверка строки: {line}')
    return functions.request_v2(query), functions.request_v2(query.replace(old_word, new_word))


def main() -> None:
    '''Прочитает указанный файл датастора, отредактирует или выключит указанные строки.'''
    functions.make_dir('reports_main', 'logs')
    data = functions.read(f'{file_name}.csv')
    logger.debug(f'Прочитано {len(data)} строк')
    for line in data:
        result_search_word = functions.search_word(old_words, line)
        if result_search_word[0]:
            v2_result = v2_report(result_search_word[1], line)
            if '|yes|' in line:
                if switch(switch_yes_brand, v2_result):
                    new_data.append(line := functions.change_word(result_search_word[1], new_word, line))
                    logger.info(f'Отредактирована строка - {line}')
                else:
                    new_data.append(line := line.replace('|yes|', '|no|'))
                    logger.info(f'Выключена строка - {line}')
            else:
                if switch(switch_no_brand, v2_result):
                    new_data.append(line := functions.change_word(result_search_word[1], new_word, line.replace('|no|',
                                                                                                                '|yes|')))
                    logger.info(f'Отредактирована и включена строка - {line}')
                else:
                    new_data.append(line)
                    logger.info(f'Строка на удаление - {line}')
        else:
            new_data.append(line)
    logger.debug(f'Выключено {len(del_preset)} строк, отредактировано {len(edit_preset)} строк.')
    rewrite_file()


if __name__ == '__main__':
    logger.add('logs.log')
    file_name = input('Путь к файлу: ')  # путь к файлу
    old_words = input('Заменяемое слово: ').split()  # слова, которые будет искать скрипт в файле в колонке Query
    new_word = input('Новое слово: ')  # слово, на которое скрипт заменит найденное старое
    new_data, edit_preset, del_preset, for_check = [], [], [], []
    brand = int(input('Выдается брендом? 1/0 '))
    main()
else:
    print('Модуль не используется как импортируемый!')
