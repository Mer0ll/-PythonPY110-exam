import json
import random

from faker import Faker

import conf


def main(start_pk, stop_pk):
    result = []
    for element in range(start_pk, stop_pk + 1):
        data = {
            'title': get_title(),
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
    print(result_json)


def get_title():
    with open('books.txt', encoding='utf-8') as f:
        books = f.readlines()
        books = [book.strip()[:-1] for book in books]
        return random.choice(books)


def get_year():
    return random.randint(1800, 2022)


def get_pages():
    return random.randint(0, 1000)


def get_isbn13():
    faker = Faker()
    return faker.isbn13()


def get_rating():
    return round(random.uniform(0, 5), 2)


def get_price():
    return round(random.uniform(0, 10000), 2)


def get_author():
    faker = Faker(locale='ru')
    lst = [faker.name() for i in range(5)]
    num = random.randint(1, 3)
    result_lst = [random.choice(lst) for _ in range(num)]
    return result_lst

if __name__ == '__main__':
    start = 1
    stop = 100
    main(start, stop)




"""
lst = {}
        result['pk'] = element
        data = {
            'title': get_title(),
            'year': get_year(),
            'pages': get_pages(),
            'isbn13': get_isbn13(),
            'rating': get_rating(),
            'author': get_author()
        }
        result['fields'] = data
"""