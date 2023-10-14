class TrollGame:
    def __init__(self):
        print("Välkommen till Trollspelet!")
        self.board_size = int(input("Ange storleken på brädet (minst 4x4): "))

        if self.board_size < 4:
            print("Ogiltig brädstorlek. Minsta tillåtna storlek är 4x4.")
            return

        self.board = [
            ["_" for _ in range(self.board_size)] for _ in range(self.board_size)
        ]
        self.row = 0

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def is_safe(self, row, col):
        for i in range(len(self.board)):
            if self.board[i][col] == "*" or self.board[row][i] == "*":
                return False
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if (i + j == row + col) or (i - j == row - col):
                    if self.board[i][j] == "*":
                        return False
        return True

    def place_troll(self, col):
        if self.row == self.board_size:
            return True
        if 1 <= col <= self.board_size and self.board[self.row][col - 1] == "_":
            if self.is_safe(self.row, col - 1):
                self.board[self.row][col - 1] = "*"
                self.row += 1
                return True
            else:
                print("Det är inte säkert att placera ett troll där.")
        else:
            print("Ogiltigt kolumnnummer eller kolumnen är redan upptagen.")
        return False

    def play_game(self):
        print("Så här ser brädet ut:")
        self.print_board()

        while self.row < self.board_size:
            col_input = input(
                f"Placera ett troll på rad {self.row + 1}, ange kolumnnummer eller 'undo': "
            )
            if col_input == "undo":
                if self.row > 0:
                    # Ångra det senaste draget om möjligt
                    prev_row = self.row - 1
                    prev_col = self.board[prev_row].index("*")
                    self.board[prev_row][prev_col] = "_"
                    self.row = prev_row
                else:
                    print("Inget att ångra ännu.")
            else:
                try:
                    col = int(col_input)
                    if self.place_troll(col):
                        self.print_board()
                except ValueError:
                    print("Ogiltigt input. Ange ett kolumnnummer eller 'undo'.")

        print("Här är brädet med trollen:")
        self.print_board()


if __name__ == "__main__":
    game = TrollGame()
    game.play_game()
