import requests

from salary import calc_salary

TOWNS = {
    "moscow": 4,
}


def fetch_language_vacancies(api_key, language, count=20, page=0):
    response = requests.get(
        "https://api.superjob.ru/2.33/vacancies/",
        headers={"X-Api-App-Id": api_key},
        params={
            "town": TOWNS["moscow"],
            "keyword": language,
            "count": count,
            "page": page,
        },
    )
    response.raise_for_status()
    return response.json()


def calc_rub_salary(vacancy):
    if vacancy["currency"] != "rub":
        return
    return calc_salary(vacancy["payment_from"], vacancy["payment_to"])
