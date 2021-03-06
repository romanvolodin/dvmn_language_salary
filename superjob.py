from itertools import count

import requests

from salary import calc_salary


def fetch_language_vacancies(api_key, language, count=20, page=0):
    moscow = 4
    all_time = 0
    response = requests.get(
        "https://api.superjob.ru/2.33/vacancies/",
        headers={"X-Api-App-Id": api_key},
        params={
            "town": moscow,
            "keyword": language,
            "count": count,
            "page": page,
            "period": all_time,
        },
    )
    response.raise_for_status()
    return response.json()


def calc_rub_salary(vacancy):
    if vacancy["currency"] != "rub":
        return
    return calc_salary(vacancy["payment_from"], vacancy["payment_to"])


def collect_languages_statistic(api_key, languages):
    languages_statistic = {}
    for language in languages:
        salaries = []
        vacancies = fetch_all_language_vacancies(api_key, language)
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


def fetch_all_language_vacancies(api_key, language):
    all_vacancies = []
    for page in count():
        vacancies = fetch_language_vacancies(
            api_key, language, count=100, page=page
        )
        all_vacancies.extend(vacancies["objects"])
        if not vacancies["more"]:
            break
    return all_vacancies
