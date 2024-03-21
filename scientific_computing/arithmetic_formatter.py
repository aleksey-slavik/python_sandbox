MAX_PROBLEMS_COUNT = 5
MAX_NUMBER_LENGTH = 4
LINE_CHAR = '-'
SPACE_BETWEEN_PROBLEMS = 4


def is_digit_checker(number_str):
    return number_str.isdigit()


def number_len_checker(number_str):
    return len(number_str) <= MAX_NUMBER_LENGTH


def calculate_result(number1, operator, number2):
    if operator == '+':
        return int(number1) + int(number2)
    elif operator == '-':
        return int(number1) - int(number2)
    else:
        raise


def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > MAX_PROBLEMS_COUNT:
        return "Error: Too many problems."

    numbers1 = list(map(lambda x: x.split()[0], problems))
    operators = list(map(lambda x: x.split()[1], problems))
    numbers2 = list(map(lambda x: x.split()[2], problems))

    if not all([operator == '+' or operator == '-' for operator in operators]):
        return "Error: Operator must be '+' or '-'."

    if not all(map(is_digit_checker, numbers1)) or not all(map(is_digit_checker, numbers2)):
        return "Error: Numbers must only contain digits."

    if not all(map(number_len_checker, numbers1)) or not all(map(number_len_checker, numbers2)):
        return "Error: Numbers cannot be more than four digits."

    first_row = ''
    second_row = ''
    line_row = ''
    result_row = ''
    separator = ' ' * SPACE_BETWEEN_PROBLEMS

    for i in range(len(problems)):
        problem_width = max(len(numbers1[i]), len(numbers2[i])) + 2
        first_row += numbers1[i].rjust(problem_width) + separator
        second_row += operators[i] + ' ' + numbers2[i].rjust(problem_width - 2) + separator
        line_row += LINE_CHAR * problem_width + separator
        result_row += str(calculate_result(numbers1[i], operators[i], numbers2[i])).rjust(problem_width) + separator

    if show_answers:
        return '\n'.join((first_row[:-SPACE_BETWEEN_PROBLEMS],
                          second_row[:-SPACE_BETWEEN_PROBLEMS],
                          line_row[:-SPACE_BETWEEN_PROBLEMS],
                          result_row[:-SPACE_BETWEEN_PROBLEMS]))
    else:
        return '\n'.join((first_row[:-SPACE_BETWEEN_PROBLEMS],
                          second_row[:-SPACE_BETWEEN_PROBLEMS],
                          line_row[:-SPACE_BETWEEN_PROBLEMS]))


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
