import requests


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
    min_salary = vacancy["payment_from"]
    max_salary = vacancy["payment_to"]
    if min_salary == 0 and max_salary == 0:
        return
    if min_salary == 0:
        return max_salary * 0.8
    if max_salary == 0:
        return min_salary * 1.2
    return (min_salary + max_salary) / 2
