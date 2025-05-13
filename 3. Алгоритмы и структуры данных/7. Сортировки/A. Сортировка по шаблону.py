"""A. Сортировка по шаблону."""


def sort(
        len_data: int,
        data: list[int],
        len_template: int,
        template: list[int]):
    """Сортировка вставками."""
    n = 0
    for i in range(len_template):
        for j in range(len_data):
            if data[j] != template[i]:
                continue
            current = data[j]
            data[j] = data[n]
            data[n] = current
            n += 1
    for i in range(n + 1, len_data):
        current = data[i]
        prev = i - 1
        while prev >= n and data[prev] > current:
            data[prev + 1] = data[prev]
            prev -= 1
        data[prev + 1] = current
    return [str(i) for i in data]


if __name__ == '__main__':
    """Главная фукция."""
#    with open('input.txt', 'r') as file_in:
#        len_data = int(file_in.readline())
#        data = [n for n in file_in.readline().split()]
#        len_template = int(file_in.readline())
#        template = [n for n in file_in.readline().split()]
#    with open('output.txt', 'w') as file_out:
#        file_out.write(' '.join(sort(len_data, data, len_template, template)))
    len_data = int(input())
    data = [int(i) for i in input().split()]
    len_template = int(input())
    template = [int(i) for i in input().split()]

    print(' '.join(sort(len_data, data, len_template, template)))
