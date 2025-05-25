class Game:
    def __init__(self):
        self.turn = 'X'
        self.winner = None
        self.tie = False
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def play_game(self):
        print("Shall we play a game?")
        self.print_board()

        while not self.winner and not self.tie:
            print(f"It’s player {self.turn}’s turn!")
            move = self.get_move()
            self.board[move] = self.turn
            self.print_board()
            self.check_game_status()
            if not self.winner and not self.tie:
                self.switch_turn()

        if self.winner:
            print(f"Player {self.winner} wins!")
        else:
            print("It's a tie!")

    def print_board(self):
        b = self.board
        print(f"""
        A   B   C
    1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        -----------
    2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        -----------
    3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def get_move(self):
        valid_keys = self.board.keys()
        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            if move not in valid_keys:
                print("Invalid format! Try again using format like A1, B2...")
            elif self.board[move] is not None:
                print("That cell is already taken! Choose another one.")
            else:
                return move

    def check_game_status(self):
        b = self.board
        lines = [
            # Rows
            ['a1', 'b1', 'c1'],
            ['a2', 'b2', 'c2'],
            ['a3', 'b3', 'c3'],
            # Columns
            ['a1', 'a2', 'a3'],
            ['b1', 'b2', 'b3'],
            ['c1', 'c2', 'c3'],
            # Diagonals
            ['a1', 'b2', 'c3'],
            ['a3', 'b2', 'c1'],
        ]

        for line in lines:
            if b[line[0]] == b[line[1]] == b[line[2]] and b[line[0]] is not None:
                self.winner = b[line[0]]
                return

        if all(b[cell] is not None for cell in b):
            self.tie = True

    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'


if __name__ == "__main__":
    game = Game()
    game.play_game()
