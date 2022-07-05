'''
DOCSTRING: Создает отчет о выдаче человеческого запроса с введенным словом и при его изменении.
Принимает строку с изменяемым словом и со словом на которое требуется заменить.
'''
from loguru import logger
import requests
import json


def main() -> None:
    '''Запишет в файлы результаты выдачи до и после изменения слова в человеческом запросе.'''
    new_word = input('Новое слово: ')
    with open(f'search_word_{file_name}.csv', 'r', encoding='utf-8') as file_input:
        file_input.readline()
        for line in file_input.readlines():
            query = line[1:line.index(')')]
            if old_word in query.split():
                request_old = query
                request_new = query.replace(old_word, new_word)
                data.append(f'{request_v2(request_old)}|{request_v2(request_new)}\n')
        write()


def write() -> None:
    '''Запишет сформированный отчет в файл.'''
    with open(f'v2_search_change_{file_name}.csv', 'w', encoding='utf-8') as file_output:
        file_output.write(new_head)
        file_output.writelines(data)
        logger.debug(f'Проверено {len(data)} строк со словом {old_word}')


def request_v2(item: str) -> str:
    '''Вернет строку с отчетом по записи.'''
    logger.info(f'Проверка человеческого запроса: ({item})')

    link = 'http://exactmatch-common.wbx-search-internal.svc.k8s.dataline/v2/search?'
    query = {"query": item}

    with requests.session() as session:
        session.headers['User-Agent'] = 'insomnia/2022.2.1'
        response = session.get(link, params=query)
        result = json.loads(response.text)
        logger.debug(f'Результат: {result}')
    return f'{result["name"]}|{result["query"]}|{result["shardKey"]}'


data = []
new_head = 'name|query|shardKey|newname|newquery|newshardKey\n'


if __name__ == '__main__':
    logger.add('logs.log')
    old_word = input('Заменяемое слово: ')
    file_name = input('Название файла: ')
    main()