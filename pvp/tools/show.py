from json import loads as json_loads
from functools import singledispatch
from pathlib import Path
from pprint import pprint


__all__ = ['show_vacancies', 'show_vacancies_from_json']


@singledispatch
def show_vacancies(vacancies):
    """
    декоратор из functools
    :param vacancies:
    """
    raise TypeError(f'! Value type > {vacancies.__class__} < is not correct !')


@show_vacancies.register
def _(vacancies: dict):
    for v in vacancies.values():
        pprint(v, indent=4)


@show_vacancies.register
def _(vacancies: list):
    for v in vacancies:
        pprint(v, indent=4)


def show_vacancies_from_json(file_path: str | Path):
    """
    Load and show saved vacancies.
    :param file_path:
    """
    with open(file_path) as f:
        data: list[dict, ...] = json_loads(f.read())

    for v in data:
        pprint(v, indent=4)
