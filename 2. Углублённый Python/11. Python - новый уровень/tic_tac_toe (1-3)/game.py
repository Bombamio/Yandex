from gameparts import Board

def main():
    game = Board()
    print(game)
    game.display()

    # Тут пользователь вводит координаты ячейки.
    row = int(input('Введите номер строки: '))
    column = int(input('Введите номер столбца: '))


    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display() 
    


if __name__ == '__main__':
    main() 

# Использую if __name__ == '__main__'
Board().disprint()