from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError

def main():
    game = Board()
    print(game)

    # Первыми ходят крестики.
    current_player = 'X'
    # Это флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True

    game.display()

    """Основной цикл игры"""
    while running:
        print(f'Ход делает {current_player}')


        """Цикл обработки шага игрока"""
        while True:
            try:
                # Тут пользователь вводит координаты ячейки.
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    # Прверка
                    raise FieldIndexError
                
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    # Прверка
                    raise FieldIndexError
                
                if game.board[row][column] != ' ':
                    # Проверка на занятость
                    raise CellOccupiedError
                
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.\n'
                    'Пожалуйста, введите значения для строки и столбца заново.'
                )
                continue

            except ValueError:
                print(
                    'Буквы вводить нельзя. Только числа.\n'
                    'Пожалуйста, введите значения для строки и столбца заново.'
                )
                continue

            except CellOccupiedError:
                print(
                    'Ячейка занята\n'
                    'Введите другие координаты.'
                )
                continue

            except Exception as e:
                print(f'Возникла ошибка: {e}')
                continue

            else:
                break

        game.make_move(row, column, current_player)
        print('Ход сделан!')
        game.display() 
        # Проверка на выйгрышь.
        if game.check_win(current_player):
            print(f'Победили {current_player}.')
            game.save_result(f'Победили {current_player}.')
            running = False
        # Проверка на ничью.
        elif game.is_board_full():
            print('Ничья!')
            game.save_result('Ничья!')
            running = False
        # Тернарный оператор, через который реализована смена игроков.
        # Если current_player равен X, то новым значением будет O,
        # иначе — новым значением будет X.
        current_player = 'O' if current_player == 'X' else 'X'
    


if __name__ == '__main__':
    main() 

# Использую if __name__ == '__main__'
Board().disprint()