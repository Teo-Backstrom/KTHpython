class Troll:
    def __init__(self, x_pos, y_pos) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos


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

    def __str__(self) -> str:
        textboard = ""
        for i in range(self.size):
            for j in range(self.size):
                textboard += self.gameboard[i][j]
            textboard += "|\n"
        return textboard


def checksurround(y, x, A, n):
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
    print_board(A, n)

    """val = input("Val")"""
    x, y = read_coordinate(n)
    while True:
        """y, x = coordinate_refin(val)"""

        while checksurround(y, x, A, n):
            """val = input("Val")
            y, x = val.split(" ")
            y = int(y) - 1
            x = int(x) - 1"""
            x, y = read_coordinate(n)

        A[y][x] = "|*"

        print_board(A, n)
        """val = input("Val")"""


# main()


def test():
    game = Gameboard(4)
    print(game)


test()
