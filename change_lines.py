'''
DOCSTRING: Меняет подстроки на указанные во всем файле.
Принимает название файла без расширения, строку, которую заменить, и строку, на которую заменить.
Возвращает файл change_lines_{file_name} с отредактированными строками.
'''
from loguru import logger
import functions


def main(o_word: str, n_world: str) -> None:
    '''Запишет в файл change_lines_{file_name} коллекцию из строк в которых подстрока {word},
     если она есть, изменена на полученную из консоли.'''
    counter_edit = 0
    data = functions.read(file_name)
    for line in data:
        if f'{o_word} ' in line or f'{o_word})' in line or f'{o_word}"' in line:  # чтобы скрипт не менял context
            new_data.append(functions.change_word(o_word, n_world, line))
            counter_edit += 1
        else:
            new_data.append(line)
    logger.debug(f'Отредактировано {counter_edit} строк')
    functions.write(f'change_lines_{file_name}', new_data)


if __name__ == '__main__':
    logger.add('logs.log')
    file_name = input('Название файла: ')
    old_word = input('Заменяемое слово: ')  # слово, которое будет искать скрипт в файле в колонке Query
    new_word = input('Новое слово: ')  # слово, на которое скрипт заменит найденное старое
    new_data = []
    main(old_word, new_word)