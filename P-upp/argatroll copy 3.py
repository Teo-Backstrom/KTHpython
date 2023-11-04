import time


class Trolls:
    def __init__(self, x_pos, y_pos) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos

    def __str__(self) -> str:
        return "|*"


class Gameboard:
    def __init__(self, size) -> None:
        A = []
        for i in range(size):
            x = []
            for j in range(size):
                x.append("|_")
            A.append(x)
        self.gameboard = A
        self.size = size
        self.turn = 0

    def __str__(self) -> str:
        textboard = ""
        for i in range(self.size):
            for j in range(self.size):
                textboard += self.gameboard[i][j]
            textboard += "|\n"
        return textboard

    def checksurround(self, x):
        if self.gameboard[self.turn][x] == "|*":
            print("Är samma")
            return False

        if "|*" in self.gameboard[self.turn]:
            print("samma rad")
            return False

        for i in range(self.size):
            if self.gameboard[i][x] == "|*":
                print("Samma kolumn")
                return False

            if (x - self.turn + i < self.size) and (x - self.turn + i >= 0):
                if self.gameboard[i][x - self.turn + i] == "|*":
                    print("Diago")
                    return False

            if x + self.turn - i < self.size:
                # här behlvs inte extra koll pga den kollar ned åt hög och kommer då bara kolla nedåt och inte hitta något för att man börjar uppeifårn ioch ned när man lägger ut troll
                if self.gameboard[i][x + self.turn - i] == "|*":
                    print("Diagonal")
                    return False
        return True

    def read_coordinate(self):
        approved_coords = False

        while not approved_coords:
            x_coord = input(
                f"Skriv in X kordinat för rad {self.turn + 1} eller skriv undo: "
            )
            if x_coord.lower() == "undo":
                approved_coords = True
            else:
                try:
                    x_coord = int(x_coord) - 1
                except:
                    print("Måste vara ett helttal, försök igen22")
                else:
                    if x_coord >= self.size or x_coord < 0:
                        print(
                            f"X kordinaten är inte innom gränserna av {self.size} x {self.size} planen"
                        )
                    else:
                        approved_coords = True

        return x_coord

    def undo(self):
        if self.turn < 1:
            print("Finns inga steg att ta bort")
        else:
            self.turn -= 1
            for x in range(self.size):
                self.gameboard[self.turn][x] = "|_"


def gameplay(board):
    allowed_input = False
    print(board)
    while board.turn < board.size:
        while not allowed_input:
            choice = board.read_coordinate()
            if choice == "undo":
                board.undo()
                print(board)
            else:
                print(board.turn)
                allowed_input = board.checksurround(choice)

        troll = Trolls(choice, board.turn)
        board.gameboard[board.turn][choice] = str(troll)
        print(board)
        board.turn += 1
        allowed_input = False

    print("Du vann")


def stopwatch(time_start):
    time_result = time.time() - time_start
    mins = time_result // 60
    sec = time_result % 60
    print(f"{mins} minuter : {sec} sekunders")
    return f"{mins} minuter : {sec} sekunders"


def save_to_file(time):
    rekord_file = open("rekord.txt", "a")
    rekord_file.write(time + "\n")
    rekord_file.close()


def bruteforce_solve():
    game = Gameboard(8)
    rows = [0] * game.size
    allowed_input = False
    print(game)
    while game.turn < game.size:
        allowed_input = game.checksurround(rows[game.turn])
        if not allowed_input:
            game = Gameboard(8)
            rows[game.size - 1] += 1
            while True:
                kkk = True
                for i in range(game.size):
                    if rows[i] > game.size - 1:
                        rows[i - 1] += 1
                        rows[i] = 0
                        kkk = False
                if kkk:
                    break

        print(rows)

        troll = Trolls(rows[game.turn], game.turn)
        game.gameboard[game.turn][rows[game.turn]] = str(troll)
        print(game)
        game.turn += 1
        allowed_input = False
    print(
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
    )


time_start = time.time()
board = Gameboard(5)
gameplay(board)
final_time = stopwatch(time_start)
save_to_file(final_time)
# bruteforce_solve()