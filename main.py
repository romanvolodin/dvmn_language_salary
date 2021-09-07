from environs import Env

import superjob as sj
import headhunter as hh

from table import generate_language_table, prepare_language_table


def main():
    languages = (
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

    env = Env()
    env.read_env()
    api_key = env.str("SUPERJOB_API_KEY")

    hh_statistic = hh.collect_languages_statistic(languages)
    sj_statistic = sj.collect_languages_statistic(api_key, languages)
    hh_table = generate_language_table(
        prepare_language_table(hh_statistic), "HeadHunter Москва"
    )
    sj_table = generate_language_table(
        prepare_language_table(sj_statistic), "SuperJob Москва"
    )
    print(hh_table)
    print(sj_table)


if __name__ == "__main__":
    main()
