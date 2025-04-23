"""B. Застёжка-молния.py."""


def array_merging(a, b, c):
    """Объединение."""
    result = []
    for num in range(a):
        result.extend([b[num], c[num]])
    return result


def main():
    """Главная фукция."""
    with open('input.txt', 'r') as file_in:
        a = int(file_in.readline())
        b = file_in.readline().split()
        c = file_in.readline().split()

    with open('output.txt', 'w') as file_out:
        file_out.write(' '.join(array_merging(a, b, c)))


if __name__ == '__main__':
    main()
