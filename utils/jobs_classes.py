import json
from engine_classes import HH


class Vacancy:
    __slots__ = ('comany_name', 'url', 'salary', 'requirement')

    def __init__(self, comany_name, url, salary, requirement):
        self.comany_name = comany_name
        self.url = url
        self.salary = salary
        self.requirement = requirement

    def __str__(self):
        return f'Вакансия: {self.comany_name}. URL: {self.url}, Зарплата: {self.salary}, Описание: {self.requirement}'

    def __repr__(self):
        return f'Вакансия: {self.comany_name}. URL: {self.url}, Зарплата: {self.salary}, Описание: {self.requirement}'


class CountMixin:

    @property
    def get_count_of_vacancy(self):
        """Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла."""

        pass



class HHVacancy(Vacancy):  # add counter mixin
    #HeadHunter Vacancy
    def __init__(self, name, url, salary, requirement):
        super().__init__()
        self.comany_name = name
        self.url = url
        self.salary = salary
        self.requirement = requirement

    def __str__(self):
        return f'HH: {self.comany_name}, зарплата: {self.salary} руб/мес'


class SJVacancy(Vacancy):  # add counter mixin
    #SuperJob Vacancy

    def __str__(self):
        return f'SJ: {self.comany_name}, зарплата: {self.salary} руб/мес'


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    data_sort =[]
    if vacancies == "vac_list_hh.json":
        with open(vacancies, 'r', encoding="utf-8") as f:
            data = json.load(f)
        data_sort = sorted([d for d in data[0] if
                            'salary' in d and d['salary'] and 'from' in d['salary'] and d['salary'][
                                'from'] is not None], key=lambda x: x['salary']['from'], reverse=True)
    else:
        with open(vacancies, 'r', encoding="utf-8") as f:
            data = json.load(f)
        data_sort = sorted(data[0], key=lambda x: x['payment_from'], reverse=True)
    with open("sort_" + vacancies, 'w') as f:
        json.dump(data_sort, f, indent=4)


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    sorted_list = sorted(vacancies, key=lambda x: x.salary, reverse=True)
    top_count = min(top_count, len(sorted_list))
    new_list = []
    for i in range(top_count):
        new_list.append(sorted_list[i])
    return new_list
