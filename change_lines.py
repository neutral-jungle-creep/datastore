'''
DOCSTRING: Меняет подстроки на указанные во всем файле.
Принимает название файла без расширения, строку, которую заменить, и строку, на которую заменить.
Если сценарий вызван как импортируемый, возвращает коллекцию строк.
Иначе возвращает файл change_lines_{file_name} с отредактированными строками.
'''
from loguru import logger


def change(word: str, file: str, func=None) -> list:
    '''
    Вернет список строк, в которых подстрока {word} изменена на полученную из консоли.
    Если сценарий запущен как импортируемый модуль, передавать именованный аргумент не требуется.
    '''
    counter_edit = 0
    if func is not None:
        link = f'{file}.csv'
    else:
        link = f'search_word_{file}.csv'
    with open(link, 'r', encoding='utf-8') as file_input:
        global head
        head = file_input.readline()  # первая строка
        for line in file_input.readlines():
            if f'{word} ' in line or f'{word})' in line or f'{word}"' in line:
                change_word(word, line)
                counter_edit += 1
            data.append(line)
    logger.debug(f'Отредактировано {counter_edit} строк')
    if func is not None:
        logger.debug(f'Запуск функции write')
        func(data)
    return data


def change_word(word: str, line: str) -> None:
    '''Добавит отредактированную строку в коллекцию со строками и посчитает ее'''
    new_line = line.replace(f'{word} ', f'{new_word} ').replace(f'{word})',
                                                                f'{new_word})').replace(f'{word}"', f'{new_word}"')
    data.append(new_line)
    logger.info(f'Новая строка - {new_line}')


def write(data: list) -> None:
    '''Если сценарий запущен самостоятельно, запишет файл с измененными строками'''
    with open(f'change_lines_{file_name}.csv', 'w', encoding='utf-8') as file_output:
        file_output.write(head)
        file_output.writelines(data)
        logger.debug(f'В файл change_lines_{file_name} записано {len(data)} строк')


data = []
new_word = input('Правильное слово: ')


if __name__ == '__main__':
    logger.add('logs.log')
    old_word = input('Заменяемое слово: ')
    file_name = input('Название файла: ')
    change(old_word, file_name, write)