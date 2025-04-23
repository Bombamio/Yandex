"""A. A+B."""


def sum_two_num(a, b):
    """Сумма."""
    return a + b


def main():
    """Главная фукция."""
    with open('input.txt', 'r') as file_in:
        a = int(file_in.readline())
        b = int(file_in.readline())

    with open('output.txt', 'w') as file_out:
        file_out.write(str(sum_two_num(a, b)))


if __name__ == '__main__':
    main()
