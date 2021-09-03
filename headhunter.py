import requests


AREAS = {
    "moscow": 1,
}

LANGUAGES = (
    "JavaScript",
    "Python",
    "Java",
    "TypeScript",
    "C#",
    "PHP",
    "C++",
    "C",
    "Ruby",
)


def fetch_language_vacancies(language):
    response = requests.get(
        "https://api.hh.ru/vacancies",
        params={"area": AREAS["moscow"], "text": language},
    )
    response.raise_for_status()
    return response.json()


def count_language_vacancies(languages):
    counted_vacancies = {}
    for language in languages:
        try:
            vacancies = fetch_language_vacancies(language)
            counted_vacancies[language] = vacancies["found"]
        except requests.exceptions.HTTPError:
            counted_vacancies[language] = None
    return counted_vacancies


def calc_rub_salary(vacancy):
    salary = vacancy["salary"]
    if salary is None or salary["currency"] != "RUR":
        return
    min_salary = salary.get("from", None)
    max_salary = salary.get("to", None)
    if min_salary is None:
        return max_salary * 0.8
    if max_salary is None:
        return min_salary * 1.2
    return (min_salary + max_salary) / 2


def collect_languages_statistic(languages):
    languages_statictic = {}
    for language in languages:
        vacancies = fetch_language_vacancies(language)
        salaries = [
            calc_rub_salary(vacancy) for vacancy in vacancies["items"]
            if calc_rub_salary(vacancy) is not None
        ]
        average_salary = int(sum(salaries) / len(salaries))
        languages_statictic[language] = {
            "vacancies_found": vacancies["found"],
            "vacancies_processed": len(salaries),
            "average_salary": average_salary
        }
    return languages_statictic
