from loguru import logger


def change(word: str) -> list:
    '''Вернет список строк, в которых подстрока {word} изменена на полученную из консоли'''
    data = []
    new_word = input('Слово на которое заменить: ')
    with open('search_word_presets.csv', 'r', encoding='utf-8') as search_word_presets:
        head = search_word_presets.readline()  # первая строка
        for line in search_word_presets.readlines():
            new_line = line.replace(word, new_word)
            data.append(new_line)
            logger.info(f'Новая строка - {new_line}')
    logger.debug(f'Отредактировано {len(data)} строк')
    return data


if __name__ == '__main__':
    old_word = input('Слово, которое заменить: ')
    change(old_word)