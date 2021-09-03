def calc_salary(min_salary, max_salary):
    if min_salary == 0 and max_salary == 0:
        return
    if min_salary == 0:
        return max_salary * 0.8
    if max_salary == 0:
        return min_salary * 1.2
    return (min_salary + max_salary) / 2
