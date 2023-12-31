import time
import tkinter as tk


class Trolls:
    def __init__(self, x_pos, y_pos) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos

    def __str__(self) -> str:
        return "*"


class Highscore:
    """
    Klass för att visa de 10 bästa tiderna
    """

    def __init__(self) -> None:
        """
        Skapar ett fönster med de 10 bäsa tiderna
        """
        self.window = tk.Tk()
        self.window.geometry("500x1200")
        self.highscores = self.get_highscore()
        # Om det finns fler än 10st tider tas de 10 bästa
        if len(self.highscores) >= 10:
            amount_scores = 10
        else:
            amount_scores = len(self.highscores)
        for i in range(amount_scores):
            # label med tiden
            self.score = tk.Label(self.window, text=f"{self.highscores[i]} sekunder")
            # position av label
            self.score.grid(row=i)

    def get_highscore(self):
        """
        funktion för att ta in tider från highscorefilen och spara i en lista som retuneras
        """
        times = []
        rekord_file = open("rekord.txt", "r")
        for rekord in rekord_file:
            times.append(float(rekord))
        rekord_file.close()
        return times


class Rules:
    """
    Klass för att visa reglerna för användaren
    """

    def __init__(self) -> None:
        """
        Funktion med för att visa regeltext och knapp för att visa highscore eller spela spelet
        """
        self.window = tk.Tk()
        self.window.geometry("1200x500")
        # label som visar reglerna
        self.rules_text = tk.Label(
            self.window,
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
        # position av reglerna
        self.rules_text.grid(row=1, padx=200)
        # knapp för att starta spelet
        self.play = tk.Button(self.window, text="Play", command=self.start_game)
        # position av startknapp
        self.play.grid(row=2)
        # knapp för att visa highscore
        self.highscore = tk.Button(
            self.window, text="Highscores", command=self.start_highscore
        )
        # position av highscoreknapp
        self.highscore.grid(row=3)
        # StringVar för feedvbacktext
        self.feedback = tk.StringVar()
        # label med feedbacktext
        self.feedback_label = tk.Label(
            self.window, textvariable=self.feedback, font=("Times New Roman", 30)
        )
        # position av feedbacktext
        self.feedback_label.grid(row=4)
        self.window.mainloop()

    def start_game(self):
        """
        funktion för att starta spelet
        """
        self.window.destroy()
        Get_size()

    def start_highscore(self):
        """
        Funktion som kollar att highscorefilen finns,
        om filen finns så visas highscoresen,
        om filen saknas så får användaren återkopping
        """
        try:
            open("rekord.txt", "r")
        except:
            self.feedback.set("Inga higscores finns")
        else:
            self.window.destroy()
            Highscore()


class Winner:
    """
    Klass för att visa att användaren vann
    """

    def __init__(self, time_start) -> None:
        """
        Funktion för att visa användaren sin slutgiltiga tid,
        samt en knapp för att börja om
        """
        self.window = tk.Tk()
        self.window.geometry("1200x500")

        # vinnar text
        self.win_text = tk.Label(
            self.window,
            text=("Du vann"),
            font=("Times New Roman", 30),
        )
        # position av text
        self.win_text.grid(row=1)

        # label med vinnar tid
        self.time_label = tk.Label(
            self.window,
            text=(stopwatch(time_start)),
            font=("Times New Roman", 30),
        )
        # position av tid
        self.time_label.grid(row=2)
        # omstart knapp
        self.restart_button = tk.Button(
            self.window, text="Restart", command=self.restart
        )
        # positon av knapp
        self.restart_button.grid(row=3)
        self.window.mainloop()

    def restart(self):
        """
        funktion för att börja om
        """
        self.window.destroy()
        Rules()


class Get_size:
    """
    klass för att grafiskt få in storlek av spelplan
    """

    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.geometry("400x200")
        # StringVar för feedback
        self.feedback_var = tk.StringVar(value="Ange storlek på spelplanen")
        # Inmating för användaren
        self.size_input = tk.Entry(self.window, font=("Times New Roman", 20))
        # positon för inmating
        self.size_input.grid(row=2, column=1, padx=50)
        # Feedback text
        self.feedback_label = tk.Label(self.window, textvariable=self.feedback_var)
        # position av feedbacktext
        self.feedback_label.grid(row=1, column=1, pady=30)
        # knapp för att strata spelet
        self.play = tk.Button(
            self.window, text="Play", command=lambda: self.get_size(True)
        )
        # position av startknapp
        self.play.grid(row=3, column=1)
        # knapp för att starta autosolver:n
        self.brute = tk.Button(
            self.window, text="Solve", command=lambda: self.get_size(False)
        )
        # position av solver kanpp
        self.brute.grid(row=4, column=1)

        self.window.mainloop()

    def get_size(self, play):
        """
        funktion för att kolla att inmatingen är korrekt samt om användaren vill låta datorn lösa boredet
        eller om hen vill spela
        """
        # kollar att det är en int
        try:
            size = int(self.size_input.get())
        except:
            self.feedback_var.set("Värdet måste vara en int")
        else:
            # kollar att planen är innom gränserna för vad som är möjligt grafiskt
            if size < 4:
                self.feedback_var.set("Planen måste minst vara 4x4")
            elif size > 8:
                self.feedback_var.set("Planen får inte plats, updatering kommande")
            else:
                self.window.destroy()

                # om användaren tryckt på playknappen så startas spelet
                # om användren tryck på solve knappen så löses spelet
                if play:
                    GameApp(size)
                else:
                    bruteforce_solve(size)


class Gameboard:
    """
    Klass som håller har alla spelregler i sig och representera spelplanen logiskt
    """

    def __init__(self, size, root) -> None:
        """
        funktion som tar in storlek på planen och fönster roten från en annan klass
        """
        # startar tidtagning
        self.time = time.time()

        # Tillvällig
        A = []
        # Loop för att skapa en tom spelplan
        for i in range(size):
            x = []
            for j in range(size):
                entity = tk.StringVar(value="↟")
                x.append(entity)
            A.append(x)
        # sparar planen i ett klass atribut
        self.gameboard = A
        self.size = size
        # sätter spelrundan till 0
        self.turn = 0
        # sätter över fönster roten till Gameboard klassen
        self.root = root

    def __str__(self) -> str:
        textboard = ""
        for i in range(self.size):
            for j in range(self.size):
                textboard += self.gameboard[i][j].get()
            textboard += "|\n"
        return textboard

    def checksurround(self, x, y, feedback_var):
        """
        Funkiton för att kolla att val av positon är giltig,
        om inte så för användaren feedback
        retunerar True ifall det är godkänt
        """
        # Om positionen är tagen så nollställs rutan
        if self.gameboard[y][x].get() == "*":
            print("Är samma")
            feedback_var.set("Är samma")
            self.undo(x, y, feedback_var)
            return False

        # Kollar om det redan finns ett troll på samma rad
        if "*" in [self.gameboard[y][i].get() for i in range(self.size)]:
            print("samma rad")
            feedback_var.set("samm rad")

            return False

        for i in range(self.size):
            # Kollar om det finns troll på samma kolumn
            if self.gameboard[i][x].get() == "*":
                print("Samma kolumn")
                feedback_var.set("Samma kolumn")

                return False

            # Kollar om det finns troll på diagonalen som går snett ned på höger
            # kollar så att den bara kollar innanför planen
            if (x - y + i < self.size) and (x - y + i >= 0):
                if self.gameboard[i][x - y + i].get() == "*":
                    print("Diago")
                    feedback_var.set("Diago")

                    return False

            # kollar om det finns troll på diagonalen som går snett ned åt vänster
            # kollar så att den bara kollar innanför planen
            if (x + y - i < self.size) and (x + y - i >= 0):
                if self.gameboard[i][x + y - i].get() == "*":
                    print("Diagonal")
                    feedback_var.set("Diagonal")

                    return False
        return True

    def read_coordinate(self, x, y, feedback_var):
        approved_coords = False

        try:
            x = int(x)
            y = int(y)
        except:
            print("Måste vara ett heltal, försök igen22")
            feedback_var.set("Måste vara ett heltal,\n försök igen")
        else:
            if x >= self.size or x < 0 or y >= self.size or y < 0:
                print(
                    f"X kordinaten är inte innom gränserna av {self.size} x {self.size} planen"
                )
                feedback_var.set(
                    f"X kordinaten är utanför\n gränserna av {self.size}x{self.size} planen"
                )
            else:
                approved_coords = True
        if approved_coords:
            return x, y

    def undo(self, x, y, feedback_var):
        """
        funktion för att nollställa en ruta
        """

        if self.turn < 1:
            print("Finns inga steg att ta bort")
            feedback_var.set("Finns inga steg att ta bort")

        else:
            self.turn -= 1
            self.gameboard[y][x].set("↟")

    def update_output(self, x, y, feedback_var):
        print(x, y)
        allowed_input = False
        # x, y = self.read_coordinate(x, y, feedback_var)
        allowed_input = self.checksurround(x, y, feedback_var)
        if allowed_input:
            troll = Trolls(x, y)
            self.gameboard[y][x].set(str(troll))
            self.turn += 1
            allowed_input = False
        if self.turn >= self.size:
            self.root.destroy()
            Winner(self.time)

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
                self.box = tk.Button(
                    self.window,
                    textvariable=self.gameboard.gameboard[i][j],
                    command=lambda y=i, x=j: self.gameboard.update_output(
                        x, y, self.feedback
                    ),
                    width=3,
                    height=1,
                    font=("Times New Roman", 50),
                )
                self.box.grid(row=i, column=j)

        """self.x_pos = tk.Entry(
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
        self.x_pos_label.grid(row=size - 2, column=size + 1, columnspan=2, rowspan=2)"""

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
