from itertools import count

import requests

from salary import calc_salary

AREAS = {
    "moscow": 1,
}


def fetch_language_vacancies(language, per_page=20, page=0):
    response = requests.get(
        "https://api.hh.ru/vacancies",
        params={
            "area": AREAS["moscow"],
            "text": language,
            "per_page": per_page,
            "page": page,
        }
    )
    response.raise_for_status()
    return response.json()


def calc_rub_salary(vacancy):
    salary = vacancy["salary"]
    if salary is None or salary["currency"] != "RUR":
        return
    min_salary = 0 if salary["from"] is None else salary["from"]
    max_salary = 0 if salary["to"] is None else salary["to"]
    return calc_salary(min_salary, max_salary)


def collect_languages_statistic(languages):
    languages_statistic = {}
    for language in languages:
        vacancies = fetch_all_language_vacancies(language)
        salaries = [
            calc_rub_salary(vacancy) for vacancy in vacancies
            if calc_rub_salary(vacancy) is not None
        ]
        average_salary = int(sum(salaries) / len(salaries))
        languages_statistic[language] = {
            "vacancies_found": len(vacancies),
            "vacancies_processed": len(salaries),
            "average_salary": average_salary
        }
    return languages_statistic


def fetch_all_language_vacancies(language):
    all_vacancies = []
    for page in count():
        vacancies = fetch_language_vacancies(
            language, per_page=100, page=page
        )
        all_vacancies.extend(vacancies["items"])
        if page == vacancies["pages"] - 1:
            break
    return all_vacancies
