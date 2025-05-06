"""A. Количество чисел, меньших, чем заданное."""


def larger_number(main_mas: list):
    """Проверка на большее число."""
    result = []
    for f_num in main_mas:
        larger = 0
        for s_num in main_mas:
            if f_num - s_num > 0:
                larger += 1
        result.append(str(larger))
    return result


def larger_num(main_mas: list):
    """Проверка на большее число."""
    result = []
    s_mas = main_mas.copy()
    s_mas.sort()
    for num in main_mas:
        n = 0
        for _ in range(s_mas.index(num)):
            n += 1
        result.append(str(n))
    return result


def larger_n(main_mas: list):
    """Проверка на большее число."""
    result = []
    s_mas = main_mas.copy()
    s_mas.sort()
    for num in main_mas:
        n = s_mas.index(num)
        result.append(str(n))
    return result
    


if __name__ == '__main__':
    """Главная фукция."""
    with open('input.txt', 'r') as file_in:
        a = [int(i) for i in file_in.readline().split()]

    with open('output.txt', 'w') as file_out:
        file_out.write(' '.join(larger_n(a)))