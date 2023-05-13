from tkinter import Tk

from models.utils.Dimension import Dimension


class GameEngine:
    def __init__(self, title: str, resizable: bool, geometry: Dimension):
        self.title = title
        self.resizable = resizable
        self.geometry = geometry

        self.window = Tk()

    def createWindow(self):
        self.window.title(self.title)

        self.window.resizable(height=self.resizable, width=self.resizable)
        self.window.geometry(self.geometry.getGeometry())

        self.window.mainloop()

    def dimensionGeometry(self):
        valueRadioButton = Tk.IntVar()

        Tk.Label(self.window,
                 text="Dimenção",
                 justify=Tk.LEFT,
                 padx=20
                 ).pack()

        Tk.Radiobutton(self.window,
                       text="700x720",
                       padx=20,
                       variable=valueRadioButton,
                       value=1
                       ).pack(anchor=Tk.W)