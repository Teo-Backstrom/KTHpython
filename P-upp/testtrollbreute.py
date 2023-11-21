import time
import tkinter as tk


class Trolls:
    def __init__(self, x_pos, y_pos) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos

    def __str__(self) -> str:
        return "*"


class Highscore:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.geometry("500x1200")
        self.highscores = self.get_highscore()
        if len(self.highscores) >= 10:
            amount_scores = 10
        else:
            amount_scores = len(self.highscores)
        for i in range(amount_scores):
            self.score = tk.Label(
                self.window,
                text= f"{self.highscores[i]} sekunder"
            )
            self.score.grid(row=i)


    def get_highscore(self):
        times = []
        rekord_file = open("rekord.txt", "r")
        for rekord in rekord_file:
            times.append(float(rekord))
        rekord_file.close()
        return times


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
        self.ok = tk.Button(self.popup, text="Play", command=self.start_game)
        self.ok.grid(row=2)
        self.highscore = tk.Button(
            self.popup, text="Highscores", command=self.start_highscore
        )
        self.highscore.grid(row=3)
        self.feedback = tk.StringVar()
        self.feedback_label = tk.Label(self.popup, textvariable=self.feedback, font=("Times New Roman", 30))
        self.feedback_label.grid(row=4)
        self.popup.mainloop()

    def start_game(self):
        self.popup.destroy()
        Popup()

    def start_highscore(self):
        try:
            open("rekord.txt", "r")
        except:
            self.feedback.set("Inga higscores finns")
        else:
            self.popup.destroy()
            Highscore()


class Popup:
    def __init__(self) -> None:
        self.popup = tk.Tk()
        self.popup.geometry("400x200")
        self.feedback_var = tk.StringVar(value="Ange storlek på spelplanen")
        self.size_input = tk.Entry(self.popup, font=("Times New Roman", 20))
        self.size_input.grid(row=2, column=1, padx=50)
        self.feedback_label = tk.Label(self.popup, textvariable=self.feedback_var)
        self.feedback_label.grid(row=1, column=1, pady=30)
        self.play = tk.Button(
            self.popup, text="Play", command=lambda: self.get_size(True)
        )
        self.play.grid(row=3, column=1)
        self.brute = tk.Button(
            self.popup, text="Solve", command=lambda: self.get_size(False)
        )
        self.brute.grid(row=4, column=1)
        self.popup.mainloop()

    def get_size(self, play):
        try:
            size = int(self.size_input.get())
        except:
            self.feedback_var.set("Värdet måste vara en int")
        else:
            if size < 4:
                self.feedback_var.set("Planen måste minst vara 4x4")
            elif size > 8:
                self.feedback_var.set("Planen får inte plats, updatering kommande")
            else:
                self.popup.destroy()
                if play:
                    GameApp(size)
                else:
                    bruteforce_solve(size)


class Gameboard:
    def __init__(self, size, root) -> None:
        self.time = time.time()
        A = []
        for i in range(size):
            x = []
            for j in range(size):
                entity = tk.StringVar(value="↟")
                x.append(entity)
            A.append(x)
        self.gameboard = A
        self.size = size
        self.turn = 0
        self.root = root  # Pass the Tkinter root to the Gameboard class

    def __str__(self) -> str:
        textboard = ""
        for i in range(self.size):
            for j in range(self.size):
                textboard += self.gameboard[i][j].get()
            textboard += "|\n"
        return textboard

    def checksurround(self, x, feedback_var):
        if self.gameboard[self.turn][x].get() == "*":
            print("Är samma")
            feedback_var.set("Är samma")
            return False

        if "*" in [self.gameboard[self.turn][i].get() for i in range(self.size)]:
            print("samma rad")
            feedback_var.set("samm rad")

            return False

        for i in range(self.size):
            if self.gameboard[i][x].get() == "*":
                print("Samma kolumn")
                feedback_var.set("Samma kolumn")

                return False

            if (x - self.turn + i < self.size) and (x - self.turn + i >= 0):
                if self.gameboard[i][x - self.turn + i].get() == "*":
                    print("Diago")
                    feedback_var.set("Diago")

                    return False

            if x + self.turn - i < self.size:
                if self.gameboard[i][x + self.turn - i].get() == "*":
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
                self.gameboard[self.turn][x].set("↟")

    def update_output(self, x_pos_entry, feedback_var):
        allowed_input = False
        choice = None
        choice = self.read_coordinate(x_pos_entry.get(), feedback_var)
        if choice != None:
            allowed_input = self.checksurround(choice, feedback_var)
        if allowed_input:
            troll = Trolls(choice, self.turn)
            self.gameboard[self.turn][choice].set(str(troll))
            self.turn += 1
            allowed_input = False
        if self.turn >= self.size:
            print("Du vann")
            feedback_var.set("Du vann")
            time.sleep(3)
            self.root.destroy()
            
            save_to_file(stopwatch(self.time))



class GameApp:
    def __init__(self, size) -> None:
        self.window = tk.Tk()
        self.window.geometry(str(300 * size) + "x" + str(200 * size))
        self.feedback = tk.StringVar()
        self.gameboard = Gameboard(
            size, self.window
        )  # Pass the Tkinter root to the Gameboard instance
        """if gaming != None:
            self.gameboard = gaming"""
        for i in range(size):
            for j in range(size):
                self.box = tk.Label(
                    self.window,
                    textvariable=self.gameboard.gameboard[i][j],
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
            command=lambda: self.gameboard.update_output(self.x_pos, self.feedback),
            font=("Times New Roman", 20),
        )
        self.ok.grid(row=size, column=size + 2)

        self.undo_button = tk.Button(
            self.window,
            text="UNDO",
            command=lambda: self.gameboard.undo(self.feedback),
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


def bruteforce_solve(size):
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

    for i in range(size):
        for j in range(size):
            box = tk.Label(
                root,
                textvariable=game.gameboard[i][j],
                width=4,
                height=2,
                font=("Times New Roman", 50),
            )
            box.grid(row=i, column=j)
    root.mainloop()


def stopwatch(time_start):
    time_result = time.time() - time_start
    """mins = time_result // 60
    sec = time_result % 60
    print(f"{mins} minuter : {sec} sekunders")
    return f"{mins} minuter : {sec} sekunders"""
    time_result = round(time_result, 2)
    return time_result


def save_to_file(time):
    times = []
    try:
        rekord_file = open("rekord.txt", "r")
        for rekord in rekord_file:
            times.append(float(rekord))
        rekord_file.close()

    except:
        print("Inga gamla rekord")
    times.append(float(time))
    times.sort()
    rekord_file = open("rekord.txt", "w")
    for rekord in times:
        rekord_file.write(str(rekord) + "\n")
    rekord_file.close()


if __name__ == "__main__":
    Rules()
