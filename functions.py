'''
DOCSTRING: Модуль c функциями для работы файлами датастора.
'''
import requests
import json
import os
from typing import Union
from pathlib import Path


def read(file: str) -> list:
    '''Примет строку - название файла. Вернет список строк из файла без строки заголовка.'''
    with open(f'{file}.csv', 'r', encoding='utf-8') as file_input:
        global head
        head = file_input.readline()
        data = file_input.readlines()
    return data


def write(file: Path or str, data: list) -> None:
    '''Примет название файла и список строк с данными. Запишет список построчно в файл.'''
    with open(file, 'w', encoding='utf-8') as file_output:
        file_output.write(head)
        file_output.writelines(data)


def search_word(words: list[str], line: str) -> Union[bool, str] or bool:
    '''Примет список из слов и строку. Вернет правду и слово из списка, если оно есть в человеческом запросе,
    иначе вернет ложь'''
    query = line.split('|')[0].split()
    for word in words:
        if word in query or word+')' in query or '('+word in query or '('+word+')' in query:
            return True, word
    return False,


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


def make_dir(name: str) -> None:
    '''Создаст папку, если она не существует.'''
    try:
        os.mkdir(f'{name}')
    except Exception:
        pass


def request_v2(item: str) -> dict:
    '''Примет строку с человеческим запросом. Вернет отчет по записи из ручки v2.'''
    link = 'http://exactmatch-common.wbxsearch-internal.svc.k8s.wbxsearch-dp/v2/search?'
    query = {"query": item.replace(')', '').replace('(', '')}

    with requests.session() as session:
        session.headers['User-Agent'] = 'insomnia/2022.2.1'
        response = session.get(link, params=query)
        result = json.loads(response.text)
    return result