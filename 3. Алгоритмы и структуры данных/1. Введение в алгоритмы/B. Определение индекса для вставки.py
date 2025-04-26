"""B. Определение индекса для вставки."""


def index_definition(mas, find_num):
    """Определение индекса для вставки."""
    for index, item in enumerate(mas):
        if find_num == int(item):
            return str(index)
        elif index == 0 and find_num < int(item):
            return str(index)
        elif int(mas[index - 1]) < find_num < int(item):
            return str(index)
        
    return str(len(mas))


def main():
    """Главная фукция."""
    with open('input.txt', 'r') as file_in:
        a = file_in.readline().split()
        b = int(file_in.readline())

    with open('output.txt', 'w') as file_out:
        file_out.write(str(index_definition(a, b)))


if __name__ == '__main__':
    main()
