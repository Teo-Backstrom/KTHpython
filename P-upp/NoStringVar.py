import time
import tkinter as tk


class Trolls:
    def __init__(self, x_pos, y_pos) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos

    def __str__(self) -> str:
        return "*"


class Rules:
    def __init__(self) -> None:
        self.popup = tk.Tk()
        self.popup.geometry("1200x500")
        self.rules_text = tk.Label(
            self.popup,
            text=(
                "Som vi alla vet så finns det många troll som bor i skogen och vissa av dessa troll\n"
                + "kan vara ganska arga. Det är därför viktigt att trollen inte kan se n˚agra andra arga troll för då böjar de bråka.\n"
                + " Detta är inte ett lika stort problem som man skulle kunna tro då troll är ganska dumma. De är väldigt bundna till naturen\n"
                + "och tittar bara i de fyra väderstrecken samt diagonalerna mellan väderstrecken, sydöst,sydväst, osv\n"
                + "Reglerna för spelet är ganska enkla. Det ska finnas:\n"
                + "• Ett troll per rad.\n"
                + "• Ett troll per kolumn.\n"
                + "• Inga troll får finnas på samma diagonal.\n"
            ),
            font=("Times New Roman", 14),
        )
        self.rules_text.grid(row=1, padx=200)
        self.ok = tk.Button(self.popup, text="Ok", command=self.start)
        self.ok.grid(row=2)
        self.popup.mainloop()

    def start(self):
        self.popup.destroy()
        Popup()


class Popup:
    def __init__(self) -> None:
        self.popup = tk.Tk()
        self.popup.geometry("400x200")
        self.feedback_var = tk.StringVar(value="Ange storlek på spelplanen")
        self.size_input = tk.Entry(self.popup, font=("Times New Roman", 20))
        self.size_input.grid(row=2, column=1, padx=50)
        self.feedback_label = tk.Label(self.popup, textvariable=self.feedback_var)
        self.feedback_label.grid(row=1, column=1, pady=30)
        self.ok = tk.Button(self.popup, text="Ok", command=self.get_size)
        self.ok.grid(row=3, column=1)
        self.popup.mainloop()

    def get_size(self):
        try:
            size = int(self.size_input.get())
        except:
            self.feedback_var.set("Värdet måste vara en int")
        else:
            if size < 4:
                self.feedback_var.set("Planen måste minst vara 4x4")
            elif size > 8:
                self.feedback_var.set("Planen får inte plats, updatering kommer snart")
            else:
                self.popup.destroy()
                # GameApp(size)
                bruteforce_solve(size)


class Gameboard:
    def __init__(self, size) -> None:
        A = []
        for i in range(size):
            x = []
            for j in range(size):
                # entity = tk.StringVar(value="↟")
                x.append("↟")
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

    def checksurround(self, x, feedback_var):
        if self.gameboard[self.turn][x] == "*":
            print("Är samma")
            feedback_var.set("Är samma")
            return False

        if "*" in [self.gameboard[self.turn][i] for i in range(self.size)]:
            print("samma rad")
            feedback_var.set("samm rad")

            return False

        for i in range(self.size):
            if self.gameboard[i][x] == "*":
                print("Samma kolumn")
                feedback_var.set("Samma kolumn")

                return False

            if (x - self.turn + i < self.size) and (x - self.turn + i >= 0):
                if self.gameboard[i][x - self.turn + i] == "*":
                    print("Diago")
                    feedback_var.set("Diago")

                    return False

            if x + self.turn - i < self.size:
                if self.gameboard[i][x + self.turn - i] == "*":
                    print("Diagonal")
                    feedback_var.set("Diagonal")

                    return False
        return True

    def read_coordinate(self, x_coord, feedback_var):
        approved_coords = False

        try:
            x_coord = int(x_coord) - 1
        except:
            print("Måste vara ett heltal, försök igen22")
            feedback_var.set("Måste vara ett heltal,\n försök igen")
        else:
            if x_coord >= self.size or x_coord < 0:
                print(
                    f"X kordinaten är inte innom gränserna av {self.size} x {self.size} planen"
                )
                feedback_var.set(
                    f"X kordinaten är utanför\n gränserna av {self.size}x{self.size} planen"
                )
            else:
                approved_coords = True
        if approved_coords:
            return x_coord

    def undo(self, feedback_var):
        if self.turn < 1:
            print("Finns inga steg att ta bort")
            feedback_var.set("Finns inga steg att ta bort")

        else:
            self.turn -= 1
            for x in range(self.size):
                self.gameboard[self.turn][x] = "↟"

    def update_output(self, x_pos_entry, feedback_var):
        allowed_input = False
        choice = self.read_coordinate(x_pos_entry.get(), feedback_var)
        allowed_input = self.checksurround(choice, feedback_var)
        if allowed_input:
            troll = Trolls(choice, self.turn)
            self.gameboard[self.turn][choice] = str(troll)
            self.turn += 1
            allowed_input = False
        if self.turn >= self.size:
            print("Du vann")
            feedback_var.set("Du vann")


class GameApp:
    def __init__(self, size) -> None:
        self.window = tk.Tk()
        self.window.geometry(str(300 * size) + "x" + str(200 * size))
        self.feedback = tk.StringVar()
        self.gameboard = Gameboard(size)

        for i in range(size):
            for j in range(size):
                self.box = tk.Label(
                    self.window,
                    text=self.gameboard.gameboard[i][j],
                    width=4,
                    height=2,
                    font=("Times New Roman", 50),
                )
                self.box.grid(row=i, column=j)

        self.x_pos = tk.Entry(
            self.window, font=("Times New Roman", 20), justify="center"
        )
        self.x_pos.grid(row=size - 1, column=size + 1, columnspan=2)

        self.ok = tk.Button(
            self.window,
            text="OK",
            command=lambda: [
                self.gameboard.update_output(self.x_pos, self.feedback),
                self.update_game(size),
            ],
            font=("Times New Roman", 20),
        )
        self.ok.grid(row=size, column=size + 2)

        self.undo_button = tk.Button(
            self.window,
            text="UNDO",
            command=lambda: [
                self.gameboard.undo(self.feedback),
                self.update_game(size),
            ],
            font=("Times New Roman", 20),
        )
        self.undo_button.grid(row=size, column=size + 1)

        self.x_pos_label = tk.Label(
            self.window, text="Ange X kordinat", font=("Times New Roman", 20)
        )
        self.x_pos_label.grid(row=size - 2, column=size + 1, columnspan=2, rowspan=2)

        self.feedback_label = tk.Label(
            self.window, textvariable=self.feedback, font=("Times New Roman", 20)
        )
        self.feedback_label.grid(row=size - 3, column=size + 1, columnspan=2, rowspan=2)

        self.window.mainloop()

    def update_game(self, size):
        for i in range(size):
            for j in range(size):
                self.box = tk.Label(
                    self.window,
                    text=self.gameboard.gameboard[i][j],
                    width=4,
                    height=2,
                    font=("Times New Roman", 50),
                )
                self.box.grid(row=i, column=j)


"""def bruteforce_solve(size):
    root = tk.Tk()
    game = Gameboard(size, root)
    rows = [0] * size
    allowed_input = False
    while game.turn < size:
        allowed_input = game.checksurround(rows[game.turn], tk.StringVar())
        if not allowed_input:
            game = Gameboard(size, root)
            rows[size - 1] += 1
            while True:
                kkk = True
                for i in range(size):
                    if rows[i] > size - 1:
                        rows[i - 1] += 1
                        rows[i] = 0
                        kkk = False
                if kkk:
                    break

        print(rows)

        # troll = Trolls(rows[game.gameboard.turn], game.gameboard.turn)
        game.gameboard[game.turn][rows[game.turn]].set("*")
        game.turn += 1
        allowed_input = False
    print(
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
    )

    GameApp(size, game)
"""


def bruteforce_solve(size):
    game = Gameboard(size)
    rows = [0] * game.size
    allowed_input = False
    print(game)
    while game.turn < game.size:
        allowed_input = game.checksurround(rows[game.turn])
        if not allowed_input:
            game = Gameboard(size)
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
    app = GameApp(size)
    app.gameboard = game.gameboard
    app.update_game(size)


if __name__ == "__main__":
    Rules()
