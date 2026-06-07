def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for problem in problems:
        parts = problem.split(' ')
        first = parts[0]
        operator = parts[1]
        second = parts[2]
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not first.isdigit() or not second.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    top_row = []
    bottom_row = []
    dash_row = []
    answer_row = []

    for problem in problems:
        parts = problem.split(' ')
        first = parts[0]
        operator = parts[1]
        second = parts[2]
        width = max(len(first), len(second)) + 2
        if operator == '+':
            answer = str(int(first) + int(second))
        else:
            answer = str(int(first) - int(second))
        top_row.append(first.rjust(width))
        bottom_row.append(operator + second.rjust(width - 1))
        dash_row.append('-' * width)
        answer_row.append(answer.rjust(width))

    arranged = '    '.join(top_row) + '\n'
    arranged += '    '.join(bottom_row) + '\n'
    arranged += '    '.join(dash_row)
    if show_answers:
        arranged += '\n' + '    '.join(answer_row)
    return arranged

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
