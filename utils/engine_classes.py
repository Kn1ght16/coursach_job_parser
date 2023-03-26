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
    API = 'https://api.hh.ru/vacancies/'

    def __init__(self, key):
        self.key = key
        self.params = {'area': 113, 'page': 1, 'per_page': 1, 'text': f'{self.key}'}
        self.name = self.get_request()['items'][0]['name']
        self.url = self.get_request()['items'][0]['alternate_url']
        self.salary = self.get_request()['items'][0]['salary']['from']
        self.requirement = self.get_request()['items'][0]['snippet']['requirement']

    def get_request(self):
        r = requests.get(url=self.API, params=self.params).json()
        return r


class SuperJob(Engine):
    def get_request(self):
        pass


