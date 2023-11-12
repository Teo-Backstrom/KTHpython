import time
import tkinter as tk


class Trolls:
    def __init__(self, x_pos, y_pos) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos

    def __str__(self) -> str:
        return "🧍🏿"


class Gameboard:
    def __init__(self, size, root) -> None:
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
        if self.gameboard[self.turn][x].get() == "|*":
            print("Är samma")
            feedback_var.set("Är samma")
            return False

        if "|*" in [self.gameboard[self.turn][i].get() for i in range(self.size)]:
            print("samma rad")
            feedback_var.set("samm rad")

            return False

        for i in range(self.size):
            if self.gameboard[i][x].get() == "|*":
                print("Samma kolumn")
                feedback_var.set("Samma kolumn")

                return False

            if (x - self.turn + i < self.size) and (x - self.turn + i >= 0):
                if self.gameboard[i][x - self.turn + i].get() == "|*":
                    print("Diago")
                    feedback_var.set("Diago")

                    return False

            if x + self.turn - i < self.size:
                if self.gameboard[i][x + self.turn - i].get() == "|*":
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
                self.gameboard[self.turn][x].set("|_")

    def update_output(self, x_pos_entry, feedback_var):
        allowed_input = False
        choice = self.read_coordinate(x_pos_entry.get(), feedback_var)
        allowed_input = self.checksurround(choice, feedback_var)
        if allowed_input:
            troll = Trolls(choice, self.turn)
            self.gameboard[self.turn][choice].set(str(troll))
            self.turn += 1
            allowed_input = False
        if self.turn >= self.size:
            print("Du vann")
            feedback_var.set("Du vann")


class GameApp:
    def __init__(self, size) -> None:
        self.window = tk.Tk()
        self.window.geometry("1200x900")

        self.gameboard = Gameboard(
            size, self.window
        )  # Pass the Tkinter root to the Gameboard instance

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

        self.feedback = tk.StringVar()
        self.feedback_label = tk.Label(
            self.window, textvariable=self.feedback, font=("Times New Roman", 20)
        )
        self.feedback_label.grid(row=size - 2, column=size + 1, columnspan=2)

        self.window.mainloop()


if __name__ == "__main__":
    GameApp(5)
