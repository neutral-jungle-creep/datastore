'''
DOCSTRING:

'''
import search_word
import change_lines
import del_lines
from loguru import logger


def mine() -> None:
    search_word.main(file)
    change_data = change_lines.main(word, file)
    logger.debug(f'Получено {len(change_data)} строк')

    clean_data = del_lines.main(word, file)
    logger.debug(f'Получено {len(clean_data)} строк')

    write(clean_data, change_data)


def write(clean_data: list, change_data: list) -> None:
    with open(f'main_{file}.csv', 'w', encoding='utf-8') as data:
        data.writelines(clean_data)
        data.writelines(change_data)
        logger.debug(f'В файл main_{file}.csv записано {len(clean_data) + len(change_data)} строк')


if __name__ == '__main__':
    logger.add('logs.log')
    word = search_word.word_for_search
    file = search_word.file_name
    mine()