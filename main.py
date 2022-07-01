import search_word
from loguru import logger


file = search_word.file_name
word = search_word.word_for_search
new_data = []
counter_del = 0
search_word.search(file)

with open(f'{file}.csv', 'r', encoding='utf-8') as data:
    head = data.readline()
    logger.info(f'Первая строка = {head}')
    for line in data.readlines():
        query = line[1:line.index(')')].split()
        if word not in query:
            new_data.append(line)
        else:
            logger.info(f'Человеческий запрос с выбранным словом = {query}')
            logger.info(f'Удаленная строка - {line}')
            counter_del += 1


print(len(new_data), counter_del, sep='\n')

