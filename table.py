from terminaltables import SingleTable


def prepare_language_table(language_statistic):
    table_rows = [
        ("Язык программирования", "Вакансий найдено",
         "Вакансий обработано", "Средняя зарплата"),
    ]
    for language, statistic in language_statistic.items():
        table_rows.append(
            (language, statistic["vacancies_found"],
             statistic["vacancies_processed"], statistic["average_salary"])
        )
    return table_rows


def generate_language_table(table_data, table_title):
    table = SingleTable(table_data)
    table.title = table_title
    table.justify_columns[1] = "right"
    table.justify_columns[2] = "right"
    table.justify_columns[3] = "right"
    return table.table
