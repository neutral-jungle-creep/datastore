from loguru import logger
import requests
import json


def main() -> None:
    old_word = input('Заменяемое слово: ')
    with open(f'search_word_{file_name}.csv', 'r', encoding='utf-8') as file_input:
        file_input.readline()
        for line in file_input.readlines():
            request_old = line[1:line.index(')')]
            request_new = line[1:line.index(')')].replace(old_word, new_word)
            old_data.append(request_v2(request_old) + '\n')
            new_data.append(request_v2(request_new) + '\n')
        write()


def write() -> None:
    with open(f'v2_search_old_{file_name}.csv',
              'w', encoding='utf-8') as old_data_output, open(f'v2_search_new_{file_name}.csv',
                                                              'w', encoding='utf-8') as new_data_output:
        old_data_output.write(new_head)
        new_data_output.write(new_head)
        old_data_output.writelines(old_data)
        new_data_output.writelines(new_data)


def request_v2(item: str) -> str:
    logger.info(f'Проверка человеческого запроса: ({item})')

    link = 'http://exactmatch-common.wbx-search-internal.svc.k8s.dataline/v2/search?'
    query = {"query": item}

    with requests.session() as session:
        session.headers['User-Agent'] = 'insomnia/2022.2.1'
        response = session.get(link, params=query)
        result = json.loads(response.text)
        logger.debug(f'Результат: {result}')
    return '|'.join([value for value in result.values()])


old_data = []
new_data = []
new_head = 'name|query|shardKey|filters\n'


if __name__ == '__main__':
    logger.add('logs.log')
    new_word = input('Новое слово: ')
    file_name = input('Название файла: ')
    main()