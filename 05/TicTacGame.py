import numpy as np


class TicTacGame:
    def __init__(self):
        self.size = 3
        self.board = np.array([
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']])
        self.first_player_name = ''
        self.second_player_name = ''
    
    def start_game(self):
        self.print_rules()
        self.get_players_names()
        result = 'continue game'

        step = 0
        while(True):
            self.show_board()

            result = self.check_finish_game()
            if result != 'continue game':
                break
            
            if step % 2 == 0:
                self.make_step(self.first_player_name, 'x')
            else:
                self.make_step(self.second_player_name, 'o')
            
            step ^= 1

            self.show_board()
        
        self.print_winer(result)

    def print_rules(self):
        rules = [
            'Обозначения исползуещиеся в игре',
            '. - пустое поле',
            'x - крестик',
            'o - нолик',
            '\n',
            'Первый игрок играет за - x, второй за o',
            'На каждом ходу игроку надо ввести координаты клетки,',
            'в которую он делает ход.',

            'Координаты: номер столбца и номер строки,',
            'разделенные пробелом. Значения координат от 1 до 3.',
        ]

        print('\n'.join(rules))
    
    def get_players_names(self):
        print('Введите в следующей строке имя первого игрока:')
        self.first_player_name = input()

        print('Введите в следующей строке имя второго игрока:')
        self.second_player_name = input()
    
    def show_board(self):
        board_str = '  '
        
        for i in range(self.size):
            board_str += str(i + 1) + ' '
        board_str += '\n  ______\n'
        
        for row in range(self.size):
            board_str += f'{row + 1}|'
        
            for col in range(self.size):
                board_str += str(self.board[row][col]) + ' '
            
            board_str += '|\n'
            if row < self.size - 1:
                board_str += ' |      |\n'
        
        board_str += '  ------\n'
        
        print(board_str)

    def check_finish_game(self):
        # проверяем горизонтали
        result = self.check_lines(self.board)

        if result != 'no winer':
            return result
        
        transpose_board = self.board.transpose()

        # проверяем вертикали
        result = self.check_lines(transpose_board)
        if result != 'no winer':
            return result
        
        # проверяем диагонали
        result = self.check_diagonal()
        if result != 'no winer':
            return result

        # проверяем заполнение полей
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == '.':
                    return 'continue game'
        
        return 'dead heat'

    def check_lines(self, arr):
        for row in range(self.size):

            if arr[row][0] != '.':
                cur_char = arr[row][0]
                cnt = 1

                for col in range(1, self.size):
                    if arr[row][col] == cur_char:
                        cnt += 1
                    else:
                        break
                
                if cnt == 3:
                    return cur_char + ' win'

        return 'no winer'

    def check_diagonal(self):
        row, col = 0, 0
        cur_char = self.board[row][col]
        cnt = 0
        
        if cur_char != '.':
            while(row < self.size):
                if cur_char == self.board[row][col]:
                    cnt += 1
                else:
                    break
                row += 1
                col += 1
            if cnt == 3:
                return cur_char + ' win'

        row, col = 0, self.size - 1
        cur_char = self.board[row][col]
        cnt = 0
        if cur_char != '.':
            while(row < self.size):
                if cur_char == self.board[row][col]:
                    cnt += 1
                else:
                    break
                row += 1
                col -= 1
            if cnt == 3:
                return cur_char + ' win'
        
        return 'no winer'

    def print_winer(self, result):
        if result == 'x win':
            print(self.first_player_name + ' выйграл!!!')
        elif result == 'o win':
            print(self.second_player_name + ' выйграл!!!')
        else:
            print('ничья')

    def make_step(self, plaeyr_name, cur_char):
        print(plaeyr_name + ' твой ход,',
              'введите номер ряда и колонны через пробел')
        step = input()

        while(not self.validate_input(step)):
            print('введите номер ряда и колонны через пробел')
            step = input()

        self.make_step_on_board(step, cur_char)
  
    def make_step_on_board(self, step, cur_char):
        row, col = map(lambda x: int(x) - 1, step.split(' '))
        self.board[row][col] = cur_char

    def validate_input(self, step):
        coordinates = step.split(' ')
        
        if len(coordinates) != 2:
            print('введено неверное количество координат')
            return False
        
        if not coordinates[0].isdigit() or not coordinates[1].isdigit():
            print('введен неверный формат данных,',
                  f'координаты должны быть целым числом от 1 до {self.size}')
            return False
        
        row, col = int(coordinates[0]) - 1, int(coordinates[1]) - 1
        if row < 0 or row > self.size - 1 or col < 0 or col > self.size - 1:
            print(f'координаты должны быть числом от 1 до {self.size}')
            return False

        if self.board[row][col] != '.':
            print('в эту позицию уже был сделан ход,\
                   введите другие координаты')
            return False
        return True


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
