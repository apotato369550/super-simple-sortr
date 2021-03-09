import Tkinter as tk
from Tkinter import *
import numpy


class Algorithms(tk.Toplevel):
    def __init__(self, **kw):
        Toplevel.__init__(self, **kw)

        self.max_width = 1200
        self.max_height = 850

        self.title("Sort")
        self.iconbitmap("images//icon.ico")
        self.geometry(str(self.max_width) + "x" + str(self.max_height))
        self.resizable(False, False)

        self.main_canvas = Canvas(self, width=self.max_width, height=self.max_height, bg="#404040")
        self.main_canvas.pack()


    def drawData(self, data, colors):
        try:
            self.main_canvas.delete("all")
        except:
            print "..."

        canvas_width = self.max_width
        canvas_height = self.max_height

        x_width = canvas_width / (len(data) + 1)
        offset = 20
        spacing = 5

        normalized_data = data / numpy.linalg.norm(data)

        for i, height in enumerate(normalized_data):
            x1 = i * x_width + offset + spacing
            y1 = canvas_height - (height * 2) * (800 + (len(data) * 15))
            x2 = (i + 1) * x_width + offset
            y2 = canvas_height

            self.main_canvas.create_rectangle(x1, y1, x2, y2, fill=colors[i], outline=colors[i])
            self.main_canvas.create_text(x1 + ((x2 - x1) / 2), y1, anchor=S, text=str(data[i]), fill="white", font=("courier", 11))





