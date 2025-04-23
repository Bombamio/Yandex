"""C. Скользящее среднее.py."""


def moving_average(n, q, k):
    """Скользящее среднее."""
    result = []
    for num in range(k, n + 1):
        summa = sum([int(q[num - i - 1]) for i in range(k)])
        result.append(str(summa / k))
    return result


def main():
    """Главная фукция."""
    with open('input.txt', 'r') as file_in:
        a = int(file_in.readline())
        b = file_in.readline().split()
        c = int(file_in.readline())

    with open('output.txt', 'w') as file_out:
        file_out.write(' '.join(moving_average(a, b, c)))


if __name__ == '__main__':
    main()
