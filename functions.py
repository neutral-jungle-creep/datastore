'''
DOCSTRING: Модуль c функциями для работы файлами датастора.
'''
import requests
import json
import os
from pathlib import Path


def read(file: str) -> list:
    '''Примет строку - название файла. Вернет список строк из файла без строки заголовка.'''
    with open(file, 'r', encoding='utf-8') as file_input:
        global head
        head = file_input.readline()
        data = file_input.readlines()
    return data


def write(file: Path or str, data: list) -> None:
    '''Примет название файла и список строк с данными. Запишет список построчно в файл.'''
    with open(file, 'w', encoding='utf-8') as file_output:
        file_output.write(head)
        file_output.writelines(data)


def add_lines(file: Path or str, data: list) -> None:
    '''Примет название файла и список строк с данными. Запишет список построчно в конец файла.'''
    with open(file, 'a', encoding='utf-8') as file_output:
        file_output.writelines(data)


def search_word(words: list[str], line: str) -> tuple[bool, str] or bool:
    '''Примет список из слов и строку. Вернет правду и слово из списка, если оно есть в
    человеческом запросе или в квери, иначе вернет ложь.'''
    request = human_request(line).replace(')', '').replace('(', '').split()
    for word in words:
        if word in request:
            return True, word
    return False,


def search_some_words(words: list[str], line):
    '''Примет список из слов и строку. Вернет правду и слова, если они все есть в
    человеческом запросе или в квери, иначе вернет ложь.'''
    pass


def human_request(line: str) -> str:
    '''Примет строку из датастора. Вернет строку, находящуюся в колонке Search Query.'''
    return line.split('|')[0]


def query_arg(line: str) -> str:
    '''Примет строку из датастора. Вернет строку, находящуюся в колонке Miner's args в части query.'''
    miner_args = line.split('|')[6]
    for arg in miner_args.split('--'):
        if 'query=' in arg:
            return arg[arg.index('"') + 1:-1]
    return miner_args


def change_word(o_word: str, n_word: str, line: str) -> str:
    '''Примет заменяемое слово, новое слово и строку. Вернет строку с замененной подстрокой на новую
    в человеческом запросе и квери.'''
    request, query = human_request(line).split(), query_arg(line).split()
    new_request, new_query = [], []

    for word in request:
        if o_word == word.replace(')', '').replace('(', ''):
            new_request.append(word.replace(o_word, n_word))
        else:
            new_request.append(word)

    for word in query:
        if o_word == word:
            new_query.append(n_word)
        else:
            new_query.append(word)

    new_line = line.replace(' '.join(request), ' '.join(new_request)).replace(' '.join(query), ' '.join(new_query))
    return new_line


def format_report(result: dict) -> str:
    '''Примет результат из ручки. Вернет отформатированную строку для формирования отчета'''
    return f'{result["name"]}|{result["query"]}|{result["shardKey"]}'


def make_dir(*args: str) -> None:
    '''Создаст папку, если она не существует.'''
    for name in args:
        try:
            os.mkdir(f'{name}')
        except Exception:
            pass


def format_report_name(file: str, words: list[str]) -> str:
    '''Сформирует имя файла для отчетов.'''
    name, word = '_'.join(file.split('\\')[-3::2]), '_'.join([word for word in words])
    return f'{name}_{word}.csv'[:100]


def request_v2(item: str) -> dict:
    '''Примет строку с человеческим запросом. Вернет отчет по записи из ручки v2.'''
    link = 'http://exactmatch-common.wbxsearch-internal.svc.k8s.wbxsearch-dp/v2/search?'
    query = {"query": item.replace(')', '').replace('(', '')}

    with requests.session() as session:
        session.headers['User-Agent'] = 'insomnia/2022.2.1'
        response = session.get(link, params=query)
        result = json.loads(response.text)
    return result