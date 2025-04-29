"""A. Неправильные горы."""


def valid_mountain_array(heights):
    """Поиск «правильных гор»."""
    len_heights = len(heights)
    last_height = -1
    lower = 0
    heigher = 0
    for num in range(len_heights):
        if heights[num] > last_height and lower != 0:
            return False
        elif heights[num] > last_height:
            last_height = heights[num]
            heigher += 1
        elif heights[num] < last_height:
            last_height = heights[num]
            lower += 1
        elif heights[num] == last_height:
            return False
    if lower == 0 or heigher == 1:
        return False
    return True

def main():
    """Главная фукция."""
    with open('input.txt', 'r') as file_in:
        a = [int(i) for i in file_in.readline().split()]

    with open('output.txt', 'w') as file_out:
        file_out.write(str(valid_mountain_array(a)))


if __name__ == '__main__':
    main()
