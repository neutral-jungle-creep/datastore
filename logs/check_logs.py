from loguru import logger
import functions


def check_logs():
    data = functions.read('new_logs.txt')
    for line in data:
        pass


def add_archive():
    '''Добавит проверенные строки в конец файла с архивом, сотрет все данные в файле с логами на проверку.'''
    functions.add_lines('archive_logs.txt', data := functions.read('new_logs.txt'))
    logger.debug(f'В файл archive_logs.txt добавлено {len(data)} строк.')
    functions.write('new_logs.txt', [])


def main():
    action = int(input('1 - проверить логи\n0 - переместить проверенное в архив\n'))
    if action:
        check_logs()
    else:
        add_archive()


if __name__ == '__main__':
    main()