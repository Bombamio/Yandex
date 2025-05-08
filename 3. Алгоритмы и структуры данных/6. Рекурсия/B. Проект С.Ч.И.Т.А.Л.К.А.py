"""B. Проект С.Ч.И.Т.А.Л.К.А."""


def casting(N: int | list, K: int):
    """Кастинг Астронавтов."""
    if isinstance(N, int):
        N = [n for n in range(1, N + 1)]
    K_pop = K
    if len(N) != 1:
        if len(N) < K:
            K_pop = K % len(N)
            if K_pop == 0:
                K_pop = len(N)
        del_num = N[K_pop - 1]
        sort_N = N[:K_pop - 1]
        if len(sort_N) > 0:
            del N[:K_pop - 1]
            N.extend(sort_N)
        N.remove(del_num)
        casting(N, K)
    return N[0]


if __name__ == '__main__':
    """Главная фукция."""
    with open('input.txt', 'r') as file_in:
        N = int(file_in.readline())
        K = int(file_in.readline())
    with open('output.txt', 'w') as file_out:
        file_out.write(str(casting(N, K)))
