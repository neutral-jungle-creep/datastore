'''
DOCSTRING: Создает отчет о выдаче человеческого запроса с введенным словом и при его изменении.
Принимает строку с изменяемым словом и со словом на которое требуется заменить.
'''
from loguru import logger
import functions


def main() -> None:
    '''Запишет в файлы результаты выдачи до и после изменения слова в человеческом запросе.'''
    data = functions.read(file_name)
    for line in data[:-1]:
        query = line[1:line.index(')')]
        if functions.search_word(old_word, line):
            request_old = query
            request_new = query.replace(old_word, new_word)
            new_data.append(f'{functions.format_report(functions.request_v2(request_old))}|'
                            f'{functions.format_report(functions.request_v2(request_new))}\n')
    functions.head = 'name|query|shardKey|new name|new query|new shardKey\n'
    functions.write(f'v2_change_{file_name}', new_data)


if __name__ == '__main__':
    logger.add('logs.log')
    file_name = input('Название файла: ')
    old_word = input('Заменяемое слово: ')  # слово, которое будет искать скрипт в файле в колонке Query
    new_word = input('Новое слово: ')  # слово, на которое скрипт заменит найденное старое
    new_data = []
    main()