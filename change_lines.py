'''
DOCSTRING: Меняет подстроки на указанные во всем файле.
Принимает название файла без расширения, строку, которую заменить, и строку, на которую заменить.
Возвращает файл с отредактированными строками.
'''
from loguru import logger


def change(word: str, file: str, func=None) -> list:
    '''Вернет список строк, в которых подстрока {word} изменена на полученную из консоли.'''
    data = []
    new_word = input('Слово на которое заменить: ')
    with open(f'search_word_{file}.csv', 'r', encoding='utf-8') as file_input:
        global head
        head = file_input.readline()  # первая строка
        for line in file_input.readlines():
            new_line = line.replace(f'{word} ', f'{new_word} ').replace(f'{word})', f'{new_word})').replace(f'{word}"', f'{new_word}"')
            data.append(new_line)
            logger.info(f'Новая строка - {new_line}')
    logger.debug(f'Отредактировано {len(data)} строк')
    if func is not None:
        logger.debug(f'Запуск функции write')
        func(data)
    return data


def write(data: list) -> None:
    '''Если скрипт запущен самостоятельно, запишет файл с измененными строками'''
    with open(f'result_change_lines_{file_name}.csv', 'w', encoding='utf-8') as file_output:
        file_output.write(head)
        file_output.writelines(data)
        logger.debug(f'В файл result_change_lines_{file_name} записано {len(data)} строк')


if __name__ == '__main__':
    old_word = input('Слово, которое заменить: ')
    file_name = input('Название файла: ')
    change(old_word, file_name, write)