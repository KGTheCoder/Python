import tkinter as tk 
import random 

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")

        self.grid_main = tk.Frame (
            self, bg = Game.Color_grid, bd=3, width=600, height=600
        )
        self.grid_main.grid(pady=(100,0))

        self.GUI_maker()
        self.start_game()

        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)

        self.mainloop()

        Color_grid = "#b8afa9"
        Color_EmptyCell = "#ffd5b5"
        Font_ScoreLabel = ("Verdana", 24)
        Font_Score = ("Helvetica", 48, "bold")
        Font_GameOver = ("Helvetica", 48, "bold")
        Font_Color_GameOver = "#ffffff"
        Winner_BG = "#ffcc00"
        Loser_BG = "#a39489"

        Color_Cells = {
            2: "#fcefe6",
            4: "#f2e8cb",
            8: "#f5b682",
            16: "#f29446",
            32: "#ff775c",
            64: "#e64c2e",
            128: "#ed3291",
            256: "#fce130",
            512: "#ffdb4a",
            1024: "#f0b922",
            2048: "#fad74d",
        }

        Color_CellNumber = {
            2: "#695c57",
            4: "#695c57",
            8: "#ffffff",
            16: "ffffff",
            32: "ffffff",
            64: "ffffff",
            128: "ffffff",
            256: "ffffff",
            512: "ffffff",
            2048: "ffffff"
        }

        Fonts_CellNumber = {
            2: ("Helvetica", 55, "bold"),
            4: ("Helvetica", 55, "bold"),
            8: ("Helvetica", 55, "bold"),
            16: ("Helvetica", 50, "bold"),
            32: ("Helvetica", 50, "bold"),
            64: ("Helvetica", 50, "bold"),
            128: ("Helvetica", 45, "bold"),
            256: ("Helvetica", 45, "bold"),
            512: ("Helvetica", 45, "bold"),
            1024: ("Helvetica", 40, "bold"),
            2048: ("Helvetica", 40, "bold")
        }

    def GUI_maker(self):
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                frame_cells = tk.Frame(
                    self.grid_main,
                    bg=Game.Color_EmptyCell,
                    width=150,
                    height=150
                )
                frame_cells.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.grid_main, bg=Game.Color_EmptyCell)
                cell_data = {"frame":frame_cells, "number": cell_number}

                cell_number.grid(row=i, column=j)
                row.append(cell_data)
            self.cells.append(row)

            frame_score = tk.Frame(self)
            frame_score.place(relx=0.5, y=60, anchor="center")
            tk.Label(
                frame_score,
                text="Score",
                font=Game.Font_ScoreLabel
            ).grid(row=0)
            self.label_score = tk.Label(frame_score, text="0", font=Game.Font_Score)
            self.label_score.grid(row=1)
