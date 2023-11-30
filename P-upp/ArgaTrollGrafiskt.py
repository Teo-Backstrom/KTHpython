import time
import tkinter as tk


# Teo Bäckström CMAST1
class Highscore:
    """
    Klass för att visa de 10 bästa tiderna
    """

    def __init__(self) -> None:
        """
        Skapar ett fönster med de 10 bäsa tiderna
        """
        self.window = tk.Tk()

        self.highscores = self.get_highscore()
        # Om det finns fler än 10st tider tas de 10 bästa
        if len(self.highscores) >= 10:
            amount_scores = 10
        else:
            amount_scores = len(self.highscores)
        for i in range(amount_scores):
            # etikett med tiden
            self.score = tk.Label(
                self.window,
                text=f"{i + 1}:a     {self.highscores[i]} sekunder",
                font=("Times New Roman", 25),
            )
            # position av etikett
            self.score.grid(row=i, padx=100, pady=10)

        # knapp för att stänga ned fönstret och öppna huvudmenyn
        self.restart = tk.Button(
            self.window,
            text="Huvudmeny",
            command=lambda: [self.window.destroy(), Rules()],
            font=("Times New Roman", 20),
        )
        # position av knapp
        self.restart.grid(row=11, pady=20)

    def get_highscore(self):
        """
        funktion för att ta in tider från highscorefilen och spara i en lista som retuneras
        retunerar: (List) times
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
        # etikett som visar reglerna
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
        self.play = tk.Button(self.window, text="Spela", command=self.start_game)
        # position av startknapp
        self.play.grid(row=2)
        # knapp för att visa highscore
        self.highscore = tk.Button(
            self.window, text="Rekord", command=self.start_highscore
        )
        # position av highscoreknapp
        self.highscore.grid(row=3)
        # StringVar för feedvbacktext
        self.feedback = tk.StringVar()
        # etikett med feedbacktext
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
        Tar in time_start(Time) vid början av spelet så skillnaden kan räknas ut
        """
        self.window = tk.Tk()

        # vinnar text
        self.win_text = tk.Label(
            self.window,
            text=("Du vann"),
            font=("Times New Roman", 30),
        )
        # position av text
        self.win_text.grid(row=1, pady=10)

        # etikett med vinnar tid
        self.time_label = tk.Label(
            self.window,
            text=(f"Din tid: {stopwatch(time_start)} sekunder"),
            font=("Times New Roman", 30),
        )
        # position av tid
        self.time_label.grid(row=2, padx=30)
        # omstart knapp
        self.restart_button = tk.Button(
            self.window, text="Starta om", command=self.restart
        )
        # positon av knapp
        self.restart_button.grid(row=3, pady=40)
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
        # Använder lambda för att kunna skicka med parametrar till funktionen https://pythonprogramming.net/passing-functions-parameters-tkinter-using-lambda/
        self.play = tk.Button(
            self.window, text="Spela", command=lambda: self.get_size(True)
        )
        # position av startknapp
        self.play.grid(row=3, column=1)
        # knapp för att starta autosolver:n
        self.brute = tk.Button(
            self.window, text="Auto-Lös", command=lambda: self.get_size(False)
        )
        # position av solver kanpp
        self.brute.grid(row=4, column=1)

        self.window.mainloop()

    def get_size(self, play):
        """
        funktion för att kolla att inmatingen är korrekt samt om användaren vill låta datorn lösa boredet
        eller om hen vill spela
        Input: (bool) play: Står för om spelaren vill spela eller inte
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
            elif size > 10:
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
    Klass som har alla spelregler i sig och representerar spelplanen logiskt
    """

    def __init__(self, size, root) -> None:
        """
        funktion som tar in storlek på planen och fönster roten från en annan klass
        och initserar en tom spelplan
        """
        # startar tidtagning
        self.time = time.time()

        # Tillvällig
        empty_gameboard = []
        # Loop för att skapa en tom spelplan
        for i in range(size):
            x = []
            for j in range(size):
                entity = tk.StringVar(value="↟")
                x.append(entity)
            empty_gameboard.append(x)
        # sparar planen i ett klass atribut
        self.gameboard = empty_gameboard
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

        Input: (int) x: x position
                (int) y: y position
                (StringVar) feedback_var: text för feedback till användaren

        """
        # Om positionen är tagen så nollställs rutan
        if self.gameboard[y][x].get() == "*":
            feedback_var.set("Nollställd")
            self.undo(x, y)
            return False

        # Kollar om det redan finns ett troll på samma rad
        if "*" in [self.gameboard[y][i].get() for i in range(self.size)]:
            feedback_var.set("Raden är upptagen")

            return False

        for i in range(self.size):
            # Kollar om det finns troll på samma kolumn
            if self.gameboard[i][x].get() == "*":
                feedback_var.set("Kolumnen är upptagen")

                return False

            # Kollar om det finns troll på diagonalen som går snett ned på höger
            # kollar så att den bara kollar innanför planen
            if (x - y + i < self.size) and (x - y + i >= 0):
                if self.gameboard[i][x - y + i].get() == "*":
                    feedback_var.set("Diagonalen är upptagen")

                    return False

            # kollar om det finns troll på diagonalen som går snett ned åt vänster
            # kollar så att den bara kollar innanför planen
            if (x + y - i < self.size) and (x + y - i >= 0):
                if self.gameboard[i][x + y - i].get() == "*":
                    feedback_var.set("Diagonalen är upptagen")

                    return False
        return True

    def undo(self, x, y):
        """
        funktion för att nollställa en ruta

        Input: (int) x: x-position
                (int) y: y-position
        """
        # tar minus ett steg
        self.turn -= 1
        self.gameboard[y][x].set("↟")

    def update_output(self, x, y, feedback_var):
        """
        funktion för att att kalla på alla funktioner så det blir ett spel

        Input: (int) x: x position
                (int) y: y position
                (StringVar) feedback_var: feedback text till användaren
        """
        allowed_input = False
        # kollar ifall input är godkänt
        allowed_input = self.checksurround(x, y, feedback_var)

        # ifall det är kodkänt så skapas ett troll på rätt position
        if allowed_input:
            self.gameboard[y][x].set("*")
            # ett steg läggs till i räknaren
            self.turn += 1
            allowed_input = False

        # har koll ifall alla troll är utplaserade
        if self.turn >= self.size:
            # sparar tiden
            save_to_file(stopwatch(self.time))

            self.root.destroy()
            # Startar vinnar skärmen
            Winner(self.time)


class GameApp:
    """
    klass som står för det gafiska gränssnittet till spelet
    """

    def __init__(self, size) -> None:
        """
        Funkiton som skapar GUI:n och tar in storleken på planen (size, int)
        """
        self.window = tk.Tk()
        self.window.geometry(str(250 * size) + "x" + str(150 * size))
        # StringVar för feedback
        self.feedback = tk.StringVar()
        # Skapar en instans av Gameboard med rätt storlek och skickar över fönster-roten
        self.gameboard = Gameboard(size, self.window)

        # Loop för att skapa det kvadratiska spelbrädet av kanppar
        for i in range(size):
            for j in range(size):
                # En knapp som representarar en låda som kan vara tom eller ett troll
                self.box = tk.Button(
                    self.window,
                    textvariable=self.gameboard.gameboard[i][j],
                    # Sätter positionen av knappen som en input för funktionen
                    command=lambda y=i, x=j: self.gameboard.update_output(
                        x, y, self.feedback
                    ),
                    width=3,
                    height=1,
                    font=("Times New Roman", 50),
                )
                # Position av låda
                self.box.grid(row=i, column=j)

        # feedback text
        self.feedback_label = tk.Label(
            self.window, textvariable=self.feedback, font=("Times New Roman", 20)
        )
        # Position av feedbacktext
        self.feedback_label.grid(row=size - 3, column=size, rowspan=4, padx=10)

        self.instructions = tk.Label(
            self.window,
            text="Klicka på ↟ för att plasera ut troll\nKlicka på * för att ångra val",
            font=("Times New Roman", 20),
        )
        self.instructions.grid(row=1, column=size, padx=20)
        self.window.mainloop()


def bruteforce_solve(size):
    """
    Funktion för att automatiskt lösa alla spelbärden

    Input: (int) size: Storleken på planen
    """
    window = tk.Tk()
    # Skapar en ny instans av gameboardklassen
    game = Gameboard(size, window)
    # skapar en tom lista som står för troll positioner för vaje rad
    rows = [0] * size
    allowed_input = False
    # körs till planen är löst
    while game.turn < size:
        # kollar om förutbestämd position är tillåten
        allowed_input = game.checksurround(rows[game.turn], game.turn, tk.StringVar())
        # Om inte så skapas en ny instans av Gameboard och trollpositionen itterar systematiskt 1 steg
        if not allowed_input:
            game = Gameboard(size, window)
            rows[size - 1] += 1
            while True:
                # ifall positionen är utanför planen så flyttas raden över ett steg och raden under börjar om
                end_of_row = True
                # behöver kolla fler gånger ifall en kedjereaktion har börjat
                for i in range(size):
                    if rows[i] > size - 1:
                        rows[i - 1] += 1
                        rows[i] = 0
                        end_of_row = False
                if end_of_row:
                    break

        # Ifall positionen är godkänd så sätts trollet ut
        game.gameboard[game.turn][rows[game.turn]].set("*")
        # Räkaren går ett steg
        game.turn += 1
        allowed_input = False
    # Skriver ut den lösta spelplanen grafiskt
    for i in range(size):
        for j in range(size):
            box = tk.Label(
                window,
                textvariable=game.gameboard[i][j],
                width=3,
                height=1,
                font=("Times New Roman", 50),
            )
            box.grid(row=i, column=j)
    restart = tk.Button(
        window,
        text="Huvudmeny",
        command=lambda: [window.destroy(), Rules()],
        font=("Times New Roman", 20),
    )
    restart.grid(row=size + 1, columnspan=size, pady=20)

    window.mainloop()


def stopwatch(time_start):
    """
    Funktion för att räkna ut och retunera speltiden

    Input: (Time) time_start: starttiden av spelet
    """
    time_result = time.time() - time_start
    # avrundar till 2 decimaler
    time_result = round(time_result, 2)
    return time_result


def save_to_file(time):
    """
    funktion för att spara ned tiden i en fil

    Input: (float) time: speltiden
    """
    times = []
    # Ifall rekordfilen finns så läggs de gamla rekorden i en lista
    try:
        rekord_file = open("rekord.txt", "r")
        for rekord in rekord_file:
            times.append(float(rekord))
        rekord_file.close()

    except:
        # ger återkopping til användaren
        print("Inga gamla rekord")

    # lägger in nya tiden i listan
    times.append(float(time))
    # Sorterar tiderna i listan
    times.sort()
    # Öppnar filen för skrivning
    rekord_file = open("rekord.txt", "w")
    # skriver ned alla tider i filen och stänger den
    for rekord in times:
        rekord_file.write(str(rekord) + "\n")
    rekord_file.close()


if __name__ == "__main__":
    Rules()
