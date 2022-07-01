import enchant
import pandas as pd
import csv
import loguru

file_name = input('file name: ')  # search
word = input('word: ')
df = pd.read_csv(f'{file_name}.csv', delimiter='|')
df['error'] = 0


def word_check(item):
    # проверяет наличие слова в человеческом запросе
    if item != word:
        return True
    return False


def query_check(serie: pd.Series):
    debracket = serie.replace('(', '').replace(')', '')
    debracket: str
    list_from_str = debracket.split()
    result = all(map(word_check, list_from_str))
    if not result:
        loguru.logger.info(f'запрос, не прошедший проверку: {list_from_str}')
    return result


df['error'] = df['Search Query'].apply(query_check)

trunc_df = df.loc[df['error'] == False]
trunc_df.to_csv(f'result_{file_name}.csv', sep='|', quoting=csv.QUOTE_NONE)