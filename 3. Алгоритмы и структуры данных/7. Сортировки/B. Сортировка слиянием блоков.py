"""B. Сортировка слиянием блоков."""


def block_merger(len_data, data):
    """Находит максимальное количество блоков для сортировки."""
    result = 0
    search_mas = set()
    data_mas = set()
    for n in range(len_data):
        search_mas.add(n)
        data_mas.add(data[n])
        if search_mas == data_mas:
            result += 1
            search_mas = set()
            data_mas = set()
    return result


if __name__ == '__main__':
    """Главная фукция."""
    len_data = int(input())
    data = [int(i) for i in input().split()]
    print(str(block_merger(len_data, data)))
