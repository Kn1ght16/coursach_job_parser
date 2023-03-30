from utils.engine_classes import HH, SuperJob
from utils.jobs_classes import sorting, get_top, HHVacancy, SJVacancy


def main():
    print("На каком вебсайте просматривать вакансии? (Введлите цифру)")
    website = int(input(f"1: HeadHunter; 2: SuperJob;\n"))
    key = input(f"Введите ключевое слово.\n")
    top_count = input(f"Введлите нужное количество вакансий.\n")
    check_sort = input(f'По какому признаку сортировать? 1: По Заработной плте; 2: По городу;\n')
    if check_sort == "2":
        check_sort = input(f"По какому городу?\n")
    if website == 1:
        hh = HH(key)
        hh.to_json_hh()
        HHVacancy.instantiate_from_json()
        sort_hh = sorting(HHVacancy.vacancies, check_sort, website)
        get_top(sort_hh, top_count, check_sort)
    elif website == 2:
        sj = SuperJob(key)
        sj.to_json_sj()
        SJVacancy.instantiate_from_json()
        sort_sj = sorting(SJVacancy.vacancies, check_sort, website)
        get_top(sort_sj, top_count, check_sort)
    else:
        print("Такого вебсайта нет.")


main()
