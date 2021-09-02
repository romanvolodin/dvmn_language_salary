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
