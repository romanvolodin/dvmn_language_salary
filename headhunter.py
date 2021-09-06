from itertools import count

import requests

from salary import calc_salary


def fetch_language_vacancies(language, per_page=20, page=0):
    moscow = 1
    response = requests.get(
        "https://api.hh.ru/vacancies",
        params={
            "area": moscow,
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
    min_salary = salary["from"] if salary["from"] else 0
    max_salary = salary["to"] if salary["to"] else 0
    return calc_salary(min_salary, max_salary)


def collect_languages_statistic(languages):
    languages_statistic = {}
    for language in languages:
        vacancies = fetch_all_language_vacancies(language)
        salaries = [
            calc_rub_salary(vacancy) for vacancy in vacancies
            if calc_rub_salary(vacancy)
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
