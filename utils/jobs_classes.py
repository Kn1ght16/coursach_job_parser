import json


class Vacancy:
    __slots__ = ('name', 'url', 'salary', "comany_name")

    def __init__(self, name, url, salary, comany_name, area):
        self.name = name
        self.url = url
        self.salary = salary
        self.comany_name = comany_name
        self.area = area

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __str__(self):
        return f'Название компании: {self.comany_name}, Название вакансии: {self.name},' \
               f' Зарплата: {self.salary}, Город: {self.area} Ссылка: {self.url}'

    def __repr__(self):
        return f'"comany_name": {self.comany_name}, "name": {self.name},' \
               f' "salary": {self.salary}, "url": {self.url}, "area": {self.area}'


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
    vacancies_dict = {}

    def __init__(self, name, url, salary, comany_name, area):
        super().__init__(name, url, salary, comany_name, area)
        self.count = CountMixin.get_count_of_vacancy

    @classmethod
    def instantiate_from_json(cls):
        hh_file = HHVacancy.file
        iter = 0
        with open(hh_file, 'r', encoding="utf-8") as f:
            file_opened = json.load(f)
            for i in file_opened:
                for item in i:
                    dict_hh = {}
                    name = item.get('name')
                    url = item.get('url')
                    try:
                        salary = item.get('salary').get('from')
                        if salary is None:
                            salary = 0
                    except AttributeError:
                        salary = 0
                    comany_name = item.get("employer").get('name')
                    area = item.get("area").get("name")
                    dict_hh["name"] = name
                    dict_hh["url"] = url
                    dict_hh["salary"] = salary
                    dict_hh["comany_name"] = comany_name
                    dict_hh["area"] = area
                    cls.vacancies_dict[iter] = dict_hh
                    iter += 1
                    instance = HHVacancy(name, url, salary, comany_name, area)
                    cls.vacancies.append(instance)


class SJVacancy(Vacancy):  # add counter mixin
    # SuperJob Vacancy
    file = "vac_list_sj.json"
    vacancies = []
    vacancies_dict = {}

    def __init__(self, name, url, salary, comany_name, area):
        super().__init__(name, url, salary, comany_name, area)
        self.count = CountMixin.get_count_of_vacancy
        self.file = SJVacancy.file

    @classmethod
    def instantiate_from_json(cls):
        sj_file = SJVacancy.file
        iter = 0
        with open(sj_file, 'r', encoding="utf-8") as f:
            file_opened = json.load(f)
            for i in file_opened:
                for item in i:
                    dict_sj = {}
                    name = item.get("profession")
                    url = item.get("link")
                    try:
                        salary = item.get("payment_from")
                        if salary is None:
                            salary = 0
                    except AttributeError:
                        salary = 0
                    comany_name = item.get("firm_name")
                    area = item.get("town").get("title")
                    dict_sj["name"] = name
                    dict_sj["url"] = url
                    dict_sj["salary"] = salary
                    dict_sj["comany_name"] = comany_name
                    dict_sj["area"] = area
                    cls.vacancies_dict[iter] = dict_sj
                    iter += 1
                    instance = SJVacancy(name, url, salary, comany_name, area)
                    cls.vacancies.append(instance)


def sorting(vacancies, numb, website):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    if numb == "1":
        vacancies = sorted(vacancies, reverse=True)
        return vacancies
    else:
        if website == 1:
            vacancies_dict_hh = HHVacancy.vacancies_dict.copy()
            for key, value in HHVacancy.vacancies_dict.items():
                if value['area'] != numb:
                    vacancies_dict_hh.pop(key)
            return vacancies_dict_hh
        else:
            vacancies_dict_sj = SJVacancy.vacancies_dict.copy()
            for key, value in SJVacancy.vacancies_dict.items():
                if value['area'] != numb:
                    vacancies_dict_sj.pop(key)
            return vacancies_dict_sj


def get_top(vacancies, top_count, check_sort):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    if check_sort == "1":
        for i in range(int(top_count)):
            print(vacancies[i])
    else:
        i = 0
        for key, value in vacancies.items():
            if i != int(top_count):
                i += 1
                vac = f"Название компании: {value['comany_name']}, Название вакансии: {value['name']}, Зарплата: {value['salary']}, Город: {value['area']} Ссылка: {value['url']}"
                print(vac)
            else:
                break
