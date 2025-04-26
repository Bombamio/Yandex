"""A. Удаление дубликатов."""


def removing_duplicates(mas_len, mas):
    """Удаление дубликатов."""
    new_mas = []
    for el in mas:
        if el not in new_mas:
            new_mas.append(el)
    for _ in range(mas_len - len(new_mas)):
        new_mas.append('_')
    return ' '.join(new_mas)


def main():
    """Главная фукция."""
    with open('input.txt', 'r') as file_in:
        a = int(file_in.readline())
        b = file_in.readline().split()

    with open('output.txt', 'w') as file_out:
        file_out.write(str(removing_duplicates(a, b)))


if __name__ == '__main__':
    main()
