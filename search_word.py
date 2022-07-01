'''
DOCSTRING: Ищет записи с введенным словом в человеческом запросе.
Принимает название файла без расширения.
Возвращает файл found_words_{file_name}.csv, содержащий только выбранные строки.
'''
import pandas as pd
import csv
from loguru import logger


def word_check(item: str) -> bool:
    '''Вернет правду, если проверяемая строка равна введенной.'''
    return item == word_for_search


def query_check(item: str) -> bool:
    '''Вернет правду, если в проверяемом списке есть введенное слово.'''
    item = item.replace('(', '').replace(')', '').split()
    result = any(map(word_check, item))
    if result:
        logger.info(f'запрос, прошедший проверку: {item}')
    return result


def search(file: str) -> None:
    '''Запишет в файл с именем 'result_{file_name}.csv строки с введенным словом.'''
    df = pd.read_csv(f'{file}.csv', delimiter='|')
    df['word'] = 0

    df['word'] = df['Search Query'].apply(query_check)

    trunc_df = df.loc[df['word'] == True]
    trunc_df = trunc_df.drop('word', axis=1)
    trunc_df['PresetID'] = trunc_df['PresetID'].astype(int)
    trunc_df.to_csv(f'found_words_{file}.csv', sep='|', quoting=csv.QUOTE_NONE, index=False)


file_name = input('file name: ')  # название файла (presets)
word_for_search = input('word: ')  # слово, которое будет искать скрипт в файле в колонке Query
# search(file_name)