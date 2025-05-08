"""A. Барометр Фибоначчи."""


def Fibonacci_barometer(n: int):
    """Результат работы барометра."""
    if n in (0, 1):
        return 1
    return Fibonacci_barometer(n - 1) + Fibonacci_barometer(n - 2)


if __name__ == '__main__':
    """Главная фукция."""
    with open('input.txt', 'r') as file_in:
        data = int(file_in.readline())
    with open('output.txt', 'w') as file_out:
        file_out.write(str(Fibonacci_barometer(data)))
