from utils.engine_classes import HH, SuperJob
from utils.connector import Connector
from utils.jobs_classes import sorting, get_top, Vacancy

hh_vac = HH('python')
hh_vac.to_json_hh()
sorting("vac_list_hh.json")

sj_vac = SuperJob('python')
sj_vac.to_json_sj()
sorting("vac_list_sj.json")

#Connector.merge_json()