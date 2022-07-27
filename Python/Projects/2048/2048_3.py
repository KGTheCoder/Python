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