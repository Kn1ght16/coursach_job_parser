import os
import requests
import json


class MixinYT():
    @classmethod
    def get_service(cls):
        # JobParserApi  переменная окружения
        super_job_key = os.environ['SuperJobAPI']
        request = "vacancies/"
        #request = "vacancies/?town=Москва&keywords[0][программист]&keywords[1][разработчик]&catalogues=56,52,51,48,47,604,42,41,40,546,503,37,36&count=4"
        my_auth_data = {'SuperJobAPI': super_job_key}
        r = requests.get('https://api.superjob.ru/2.0/' + request, headers=my_auth_data)