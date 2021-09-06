from environs import Env

import superjob as sj
import headhunter as hh

from table import print_language_table


def main():
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

    env = Env()
    env.read_env()
    api_key = env.str("SUPERJOB_API_KEY")

    hh_statistic = hh.collect_languages_statistic(LANGUAGES)
    sj_statistic = sj.collect_languages_statistic(api_key, LANGUAGES)
    print_language_table(hh_statistic, "HeadHunter Москва")
    print_language_table(sj_statistic, "SuperJob Москва")


if __name__ == "__main__":
    main()
