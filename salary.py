def calc_salary(min_salary, max_salary):
    if min_salary and max_salary:
        return (min_salary + max_salary) / 2
    if max_salary:
        return max_salary * 0.8
    if min_salary:
        return min_salary * 1.2
