"""A. Камни с Марсаю"""


def distribute_samp(len_orders: int,
                    orders: list,
                    len_samples: int,
                    samples: list):
    """Распределяет образцы между заказчиками."""
    for n in samples:
        if len(orders) == 0:
            result = len_orders
            return result
        if n in orders:
            orders.remove(n)
        else:
            while n != 0:
                n -= 1
                if n in orders:
                    orders.remove(n)
                    break
    result = len_orders - len(orders)
    return result


if __name__ == '__main__':
    """Главная фукция."""
    len_orders = int(input())
    orders = [int(i) for i in input().split()]
    len_samples = int(input())
    samples = [int(i) for i in input().split()]
    print(str(distribute_samp(len_orders, orders, len_samples, samples)))
