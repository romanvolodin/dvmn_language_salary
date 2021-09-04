from terminaltables import SingleTable


def prepare_table_data(language_statistic):
    table_data = [
        ("Язык программирования", "Вакансий найдено",
         "Вакансий обработано", "Средняя зарплата"),
    ]
    for language, statistic in language_statistic.items():
        table_data.append(
            (language, statistic["vacancies_found"],
             statistic["vacancies_processed"], statistic["average_salary"])
        )
    return table_data


def generate_language_table(table_data, table_title):
    table = SingleTable(table_data)
    table.title = table_title
    table.justify_columns[1] = 'right'
    table.justify_columns[2] = 'right'
    table.justify_columns[3] = 'right'
    return table.table


def print_language_table(language_statistic, table_title):
    table = generate_language_table(
        prepare_table_data(language_statistic), table_title
    )
    print(table)
