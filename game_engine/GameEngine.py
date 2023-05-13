from tkinter import *

from configs import Resolutions
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
        OPTIONS = Resolutions.OPTIONS

        variable = StringVar(self.window)
        variable.set(OPTIONS[0])

        def show_selected_option():
            print("Opção selecionada:", variable.get())

        Radiobutton(self.window, text=OPTIONS[0], variable=variable, value=OPTIONS[0], command=show_selected_option).pack()
        Radiobutton(self.window, text=OPTIONS[1], variable=variable, value=OPTIONS[1], command=show_selected_option).pack()
        Radiobutton(self.window, text=OPTIONS[2], variable=variable, value=OPTIONS[2], command=show_selected_option).pack()



