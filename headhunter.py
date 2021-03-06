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
    if vacancy["salary"] is None or vacancy["salary"]["currency"] != "RUR":
        return
    return calc_salary(vacancy["salary"]["from"], vacancy["salary"]["to"])


def collect_languages_statistic(languages):
    languages_statistic = {}
    for language in languages:
        salaries = []
        vacancies = fetch_all_language_vacancies(language)
        for vacancy in vacancies:
            salary = calc_rub_salary(vacancy)
            if salary:
                salaries.append(salary)
        average_salary = 0
        if salaries:
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
