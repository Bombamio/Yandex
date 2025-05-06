"""A. Служба доставки. ID: 137888628."""


def min_platforms(data: list, max_weight: int):
    """
    Определяет минимальное количество транспортных платформ,
    необходимое для перевозки всех роботов, описанных в массиве."""
    # Сортируем масив чтобы воспользоваться методом двух указателей.
    data.sort()
    result = 0
    # Используем метод двух указателей.
    left_pointer = 0
    right_pointer = len(data) - 1
    while right_pointer >= left_pointer:
        weight_sum = data[left_pointer] + data[right_pointer]
        if weight_sum > max_weight:
            right_pointer -= 1
            # Увеличиваем счётчик на 1, так-как правый элемент масива
            # не будет использован.
            result += 1
        elif weight_sum <= max_weight:
            # Увеличиваем счётчик на 1, сумма этих элементов нам подходит.
            result += 1
            left_pointer += 1
            right_pointer -= 1
        elif right_pointer == left_pointer:
            # Увеличиваем счётчик на 1 и заканчиваем цикл
            # если остался лишний элемент.
            result += 1
            break
    return result


if __name__ == '__main__':
    """Главная фукция."""
    with open('input.txt', 'r') as file_in:
        a = [int(i) for i in file_in.readline().split()]
        b = int(file_in.readline())
    with open('output.txt', 'w') as file_out:
        file_out.write(str(min_platforms(a, b)))
