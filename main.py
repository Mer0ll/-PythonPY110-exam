import json
import random

from faker import Faker

import conf


def main(start_pk: int, stop_pk: int):
    """
    A function that returns a list of dictionaries as a file result.json
    :param start_pk: countdown start, from file conf.py
    :param stop_pk: stop count, from file conf.py
    :return: creates a file result.json
    """
    title_list = get_title_list()
    result = []
    for element in range(start_pk, stop_pk + 1):
        data = {
            'title': get_random_title(title_list),
            'year': get_year(),
            'pages': get_pages(),
            'isbn13': get_isbn13(),
            'rating': get_rating(),
            'author': get_author()
        }
        lst = {
            'model': conf.MODEL,
            'pk': element,
            'fields': data,
        }
        result.append(lst)

    result_json = json.dumps(result, indent=4, ensure_ascii=False)
    get_result_json_file(result_json)


def get_title_list() -> list:
    with open('books.txt', encoding='utf-8') as f:
        books = f.readlines()
        books = [book.strip()[:-1] for book in books]
        return books


def get_random_title(lst: list) -> str:
    return random.choice(lst)


def get_year() -> int:
    return random.randint(1800, 2022)


def get_pages():
    return random.randint(0, 1000)


def get_isbn13() -> str:
    faker = Faker()
    return faker.isbn13()


def get_rating() -> float:
    return round(random.uniform(0, 5), 2)


def get_price() -> float:
    return round(random.uniform(0, 10000), 2)


def get_author() -> list:
    faker = Faker(locale='ru')
    lst = [faker.name() for _ in range(5)]
    num = random.randint(1, 3)
    result_lst = [random.choice(lst) for _ in range(num)]
    return result_lst


def get_result_json_file(file: json) -> None:
    with open('result.json', 'w', encoding='utf-8') as f:
        f.write(file)


if __name__ == '__main__':
    main(conf.START, conf.STOP)
