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
    человеческом запросе или в квери, иначе вернет ложь'''
    request, query = human_request(line), query_arg(line)
    for word in words:
        if word in request or word in query:
            return True, word
    return False,


def search_some_words(words: list[str], line):
    ''''''


def human_request(line: str) -> list[str]:
    '''Примет строку из датастора. Вернет список слов находящихся в Search Query.'''
    return line.split('|')[0].replace(')', '').replace('(', '').split()


def query_arg(line: str) -> list[str]:
    '''Примет строку из датастора. Вернет список слов, находящихся в Miner's args query.'''
    miner_args = line.split('|')[6].split()
    try:
        for arg in miner_args:
            if '--query=' in arg:
                return arg[arg.index('"'):-1].split()
    except Exception:
        return miner_args


def change_word(o_word: str, n_word: str, line: str) -> str:
    '''Примет заменяемое слово, новое слово и строку. Вернет строку с замененной подстрокой на новую.'''
    new_line = line.replace(f'{o_word} ', f'{n_word} ').replace(f'{o_word})',
                                                                f'{n_word})').replace(f'{o_word}"', f'{n_word}"')
    return new_line


def format_report(result: dict) -> str:
    '''Примет результат из ручки. Вернет отформатированную строку для формирования отчета'''
    return f'{result["name"]}|{result["query"]}|{result["shardKey"]}'


def del_lines(word: list, data: list) -> list:
    '''Примет строку - слово, строки с которым в человеческом запросе нужно удалить из датастора.
    Вернет коллекцию строк.'''
    new_data = []
    counter_del = 0
    for line in data:
        if not search_word(word, line):
            new_data.append(line)
        else:
            counter_del += 1
    return new_data


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