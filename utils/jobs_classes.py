import json


class Vacancy:
    __slots__ = ('name', 'url', 'salary', "comany_name")

    def __init__(self, name, url, salary, comany_name):
        self.name = name
        self.url = url
        self.salary = salary
        self.comany_name = comany_name

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __str__(self):
        return f'Название компании: {self.comany_name}, Название вакансии: {self.name},' \
               f' Зарплата: {self.salary}, Ссылка: {self.url}'

    def __repr__(self):
        return f'name: {self.comany_name}, name: {self.name}, salary: {self.salary}, url: {self.url}'


class CountMixin:

    @property
    def get_count_of_vacancy(self, website):
        """Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла."""
        if website == 1:
            file = "vac_list_hh.json"
        else:
            file = "vac_list_sj.json"
        with open(file, 'r') as f:
            my_file = json.load(f)
            for i in my_file:
                for item in i:
                    self.count += 1
        return self.count


class HHVacancy(Vacancy, CountMixin):  # add counter mixin
    # HeadHunter Vacancy
    file = "vac_list_hh.json"
    vacancies = []

    def __init__(self, name, url, salary, comany_name):
        super().__init__(name, url, salary, comany_name)
        self.count = CountMixin.get_count_of_vacancy

    @classmethod
    def instantiate_from_json(cls):
        hh_file = HHVacancy.file
        with open(hh_file, 'r', encoding="utf-8") as f:
            file_opened = json.load(f)
            for i in file_opened:
                for item in i:
                    name = item.get('name')
                    url = item.get('url')
                    try:
                        salary = item.get('salary').get('from')
                        if salary is None:
                            salary = 0
                    except AttributeError:
                        salary = 0
                    comany_name = item.get("employer").get('name')
                    instance = HHVacancy(name, url, salary, comany_name)
                    cls.vacancies.append(instance)


class SJVacancy(Vacancy):  # add counter mixin
    # SuperJob Vacancy
    file = "vac_list_sj.json"
    vacancies = []

    def __init__(self, name, url, salary, comany_name):
        super().__init__(name, url, salary, comany_name)
        self.count = CountMixin.get_count_of_vacancy
        self.file = SJVacancy.file

    @classmethod
    def instantiate_from_json(cls):
        sj_file = SJVacancy.file
        with open(sj_file, 'r', encoding="utf-8") as f:
            file_opened = json.load(f)
            for i in file_opened:
                for item in i:
                    name = item.get("profession")
                    url = item.get("link")
                    try:
                        salary = item.get("payment_from")
                        if salary is None: c = 0
                    except AttributeError:
                        salary = 0
                    comany_name = item.get("firm_name")
                    instance = SJVacancy(name, url, salary, comany_name)
                    cls.vacancies.append(instance)


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    vacancies = sorted(vacancies, reverse=True)
    return vacancies


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    top_counts = []
    for i in range(int(top_count)):
        top_counts.append(vacancies[i])
    return top_counts
