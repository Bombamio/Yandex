"""A. Количество чисел, меньших, чем заданное."""


def substring_search(data):
    """Поиск подстроки."""
    result = 0
    mas = []
    for element in data:
        if element not in mas:
            mas.append(element)
        else:
            result = max(result, len(mas))
            while element in mas:
                mas.pop(0)
            mas.append(element)
    result = max(result, len(mas))
    return result


if __name__ == '__main__':
    """Главная фукция."""
    with open('input.txt', 'r') as file_in:
        a = [i for i in file_in.readline()]
        if a[-1] == '\n':
            a.pop()

    with open('output.txt', 'w') as file_out:
        file_out.write(str(substring_search(a)))