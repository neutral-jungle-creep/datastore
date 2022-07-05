from loguru import logger
import requests
import json


def main():
    with open(f'search_word_{file_name}.csv', 'r', encoding='utf-8') as file_input:
        head = file_input.readline()
        for line in file_input.readlines():
            request_old = line[1:line.index(')')]
            request_new = line[1:line.index(')')].replace(old_word, new_word)
            request_v2(request_old)
            request_v2(request_new)


def request_v2(item: str):
    logger.info(f'Проверка человеческого запроса: ({item})')

    link = 'http://exactmatch-common.wbx-search-internal.svc.k8s.dataline/v2/search?'
    query = {"text": item}


if __name__ == '__main__':
    old_word = input('Заменяемое слово: ')
    new_word = input('Новое слово: ')
    file_name = input('Название файла: ')
    main()