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

    def gameplay(self):
        allowed_input = False
        print(self)
        while self.turn < self.size:
            while not allowed_input:
                choice = self.read_coordinate()
                if choice == "undo":
                    self.undo()
                    print(self)
                else:
                    print(self.turn)
                    allowed_input = self.checksurround(choice)

            troll = Trolls(choice, self.turn)
            self.gameboard[self.turn][choice] = str(troll)
            print(self)
            self.turn += 1
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


"""def checksurround(y, x, A, n):
    if A[y][x] == "|*":
        print("Är samma")
        return True

    if "|*" in A[y]:
        print("samma rad")
        return True

    for i in range(n):
        if A[i][x] == "|*":
            print("Samma kolumn")
            return True

        if x - y + i < n:
            if A[i][x - y + i] == "|*":
                print("Diago")
                return True
        if x + y - i < n:
            if A[i][x + y - i] == "|*":
                print("Diagonal")
                return True
    return False


def print_board(matrix, size):
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end="")
        print("|")


def initiate_matrix(size):
    A = []
    for i in range(size):
        x = []
        for j in range(size):
            x.append("|_")
        A.append(x)
    return A


def coordinate_refin(coordinate):
    y, x = coordinate.split(" ")
    y = int(y) - 1
    x = int(x) - 1
    return y, x


def read_coordinate(size):
    approved_coords = False
    coordinates = [None, None]
    coord_name = ["X", "Y"]
    for count in range(len(coord_name)):
        while not approved_coords:
            coordinates[count] = input(f"Skriv in {coord_name[count]} kordinat")
            try:
                coordinates[count] = int(coordinates[count]) - 1
            except:
                print("Måste vara ett helttal, försök igen")
            else:
                if coordinates[count] >= size or coordinates[count] < 0:
                    print(
                        f"{coord_name[count]} kordinaten är inte innom gränserna av {size} x {size} planen"
                    )
                else:
                    approved_coords = True
    x, y = coordinates
    return x, y


def main():
    n = 5
    A = initiate_matrix(n)
    print_board(A, n)"""

# """val = input("Val")"""
# x, y = read_coordinate(n)
# while True:
# y, x = coordinate_refin(val)

# while checksurround(y, x, A, n):
# val = input("Val")
# y, x = val.split(" ")
# y = int(y) - 1
# x = int(x) - 1
# x, y = read_coordinate(n)

# A[y][x] = "|*"

# print_board(A, n)
# val = input("Val")


# main()


"""def test():
    game = Gameboard(4)
    print(game)

    game.read_coordinate()
    while game.turn < game.size:

        while game.checksurround()"""

time_start = time.time()
test = Gameboard(5)
test.gameplay()
final_time = stopwatch(time_start)
save_to_file(final_time)
