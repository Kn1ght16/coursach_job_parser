import os
import requests
import json
from abc import ABC, abstractmethod
from connector import Connector


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name: str):
        """ Возвращает экземпляр класса Connector """
        connector = Connector(file_name)
        return connector


class HH(Engine):
    API_HH = 'https://api.hh.ru/vacancies/'

    # Москва id 1, СПБ id 2, Белгород id 1

    def __init__(self, key):
        self.page = 0
        self.key = key
        self.params = {'area': 113, 'page': 0, 'per_page': 100, 'text': f'{self.key}', 'experience': 'noExperience'}
        self.name = self.get_request()[0]['name']
        self.url = self.get_request()[0]['alternate_url']
        self.salary = self.get_request()[0]['salary']['from']
        self.requirement = self.get_request()[0]['snippet']['requirement']

    def get_request(self):
        r = requests.get(url=self.API_HH, params=self.params).json()['items']
        return r

    def to_json_hh(self):
        json_list = []
        for i in range(5):
            self.page = i
            r = requests.get(url=self.API_HH, params=self.params).json()['items']
            json_list.append(r)
        with open("vac_list_hh.json", "w", encoding="utf-8") as file:
            json.dump(json_list, file, ensure_ascii=False)


class SuperJob(Engine):
    API_SJ = os.getenv('SuperJobAPI')

    def __init__(self, key):
        self.town = ""
        self.page = 0
        self.count = 100
        self.key = key
        self.params = {'keywords': self.key, "town": self.town, "count": self.count}

    def get_request(self):
        r = requests.get('https://api.superjob.ru/2.0/vacancies/', headers={'X-Api-App-Id': self.API_SJ},
                         params=self.params).json()['objects']
        return r

    def to_json_sj(self):
        json_list = []
        for i in range(5):
            self.page = i
            r = requests.get(f'https://api.superjob.ru/2.0/vacancies/?page={self.page}&keyword={self.key}',
                             headers={'X-Api-App-Id': self.API_SJ},
                             params=self.params).json()['objects']
            json_list.append(r)
        with open("vac_list_sj.json", "w", encoding="utf-8") as file:
            json.dump(json_list, file, ensure_ascii=False)
