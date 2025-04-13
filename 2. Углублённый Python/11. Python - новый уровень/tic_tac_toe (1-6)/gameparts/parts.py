class Board:
    """Класс, который описывает игровое поле."""

    # Новый атрибут.
    field_size = 3

    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)] for _ in range(self.field_size)
        ]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_board_full(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == ' ':
                    return False
        return True
    
    def check_win(self, player):
        for i in range(self.field_size):
            if (all([self.board[i][j] == player for j in range(self.field_size)]) or
                all([self.board[j][i] == player for j in range(self.field_size)])):
                return True
        
        if (all([self.board[i][i] == player for i in range(self.field_size)]) or
                all([self.board[i][self.field_size - 1 - i] == player for i in range(self.field_size)])):
            return True
        
        return False
    
    def save_result(self, result):
        """Сохранение результатов всех игр в отдельный файл."""

        # Открытие файла в режиме добавления.
        with open('results.txt', 'a', encoding='utf-8') as file:
            file.write(result)

    # Переопределяем метод __str__.
    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
    

    def disprint(self):
        if __name__ == '__main__':
            print('Использую if __name__ == __main__')