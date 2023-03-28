from utils.engine_classes import HH, SuperJob
from utils.jobs_classes import sorting, get_top, HHVacancy, SJVacancy


def main():
    print("На каком вебсайте просматривать вакансии? (Введлите цифру)")
    website = int(input(f"1: HeadHunter; 2: SuperJob;\n"))
    key = input(f"Введите ключевое слово.\n")
    top_count = input(f"Введлите нкжное количество вакансий.\n")
    if website == 1:
        hh = HH(key)
        hh.to_json_hh()
        HHVacancy.instantiate_from_json()
        sort_hh = sorting(HHVacancy.vacancies)
        top_hh = get_top(sort_hh, top_count)
        for i in top_hh:
            print(i)
    elif website == 2:
        sj = SuperJob(key)
        sj.to_json_sj()
        SJVacancy.instantiate_from_json()
        sort_sj = sorting(SJVacancy.vacancies)
        top_sj = get_top(sort_sj, top_count)
        for i in top_sj:
            print(i)
    else:
        print("Такого вебсайта нет.")


main()
