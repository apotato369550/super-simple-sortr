import Tkinter as tk
from Tkinter import *
from PIL import ImageTk, Image
import ttk
import random
import numpy
import BubbleSort
import SelectionSort
import InsertionSort
import ShellSort
import QuickSort
import MergeSort
import HeapSort
import CocktailShakerSort
import CombSort
import TimSort
import CountSort
import BogoSort

class SSS(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.max_width = 1000
        self.max_height = 600

        self.title("SSS")
        self.iconbitmap("images//icon.ico")
        self.geometry(str(self.max_width) + "x" + str(self.max_height))
        self.resizable(False, False)

        self.data = []

        self.makeUserInterface()

        self.mainloop()

    def makeUserInterface(self):
        self.main_logo = ImageTk.PhotoImage(Image.open("images//logo.png").resize((200, 200)))

        self.user_interface_frame = Frame(self, width=self.max_width, height=200)
        self.user_interface_frame.grid(row=0, column=0)

        self.main_canvas = Canvas(self, width=self.max_width, height=400, bg="#404040")
        self.main_canvas.grid(row=1, column=0)

        # Control panel and logo
        self.main_logo_label = Label(self.user_interface_frame, image=self.main_logo, bg="#ffffff", relief="groove",
                                     borderwidth=5)
        self.control_panel = Frame(self.user_interface_frame, width=790, height=200, bg="#ffffff", relief="groove",
                                   borderwidth=5)

        self.main_logo_label.grid(row=0, column=0)
        self.control_panel.grid(row=0, column=1)

        # Make from not shrink when widgets are placed inside of it
        self.control_panel.grid_propagate(0)

        # Main title
        self.super_label = Label(self.control_panel, text="Super", bg="#ffffff", font=("courier", 38, "bold"), padx=5)
        self.simpl_label = Label(self.control_panel, text="Simple", bg="#ffffff", font=("courier", 38, "bold"), padx=5)
        self.sortr_label = Label(self.control_panel, text="Sortr", bg="#ffffff", font=("courier", 38, "bold"), padx=5)

        self.super_label.grid(row=0, column=0)
        self.simpl_label.grid(row=1, column=0)
        self.sortr_label.grid(row=2, column=0)

        # Scales for sorting speed, data length, min/max data
        self.speed_scale = Scale(self.control_panel, from_=0.1, to=2.0, length=160, digits=2, resolution=0.1,
                                 orient=HORIZONTAL, label="Speed/Delay (in seconds)", bg="#f2f2f2", relief="groove",
                                 highlightbackground="#e6e6e6", font=("arial", 8))
        self.size_scale = Scale(self.control_panel, from_=20, to=60, length=160, resolution=1, orient=HORIZONTAL,
                                label="Data Size", bg="#f2f2f2", relief="groove", highlightbackground="#e6e6e6",
                                font=("arial", 8), command=self.displayData)
        self.min_scale = Scale(self.control_panel, from_=0, to=10, length=350, resolution=1, orient=HORIZONTAL,
                               label="Minimum Data Value", bg="#f2f2f2", relief="groove", highlightbackground="#e6e6e6",
                               font=("arial", 8), command=self.displayData)
        self.max_scale = Scale(self.control_panel, from_=5, to=100, length=350, resolution=1, orient=HORIZONTAL,
                               label="Maximum Data Value", bg="#f2f2f2", relief="groove", highlightbackground="#e6e6e6",
                               font=("arial", 8), command=self.displayData)

        # grid scales here
        self.speed_scale.grid(row=0, column=1)
        self.size_scale.grid(row=0, column=2)
        self.min_scale.grid(row=1, column=1, columnspan=2, padx=15)
        self.max_scale.grid(row=2, column=1, columnspan=2, padx=15)

        # Algorithm selector
        self.selected_algorithm = StringVar()
        self.selected_algorithm.set("Bubble Sort")
        self.algorithm_menu = ttk.Combobox(self.control_panel,
                                values=["Bubble Sort", "Selection Sort", "Insertion Sort", "ShellSort",
                                        "QuickSort", "Merge Sort", "Heap Sort", "Cocktail Shaker Sort",
                                        "Comb Sort", "TimSort", "Counting Sort", "BogoSort"],
                                font=("courier", 10, "bold"), textvariable=self.selected_algorithm)

        # Grid Algorithm Menu
        self.algorithm_menu.grid(row=0, column=3, rowspan=2)

        # Create start button
        self.sort_button = Button(self.control_panel, text="Sort!", bg="#f2f2f2", relief="groove",
                                  highlightbackground="#e6e6e6", font=("courier", 18, "bold"), command=self.sort)

        # Grid Sort Button
        self.sort_button.grid(row=1, column=3, rowspan=2)

    def generateData(self):
        # call and implement this  method
        minimum_value = int(self.min_scale.get())
        maximum_value = int(self.max_scale.get())
        size = int(self.size_scale.get())

        self.data = []
        for i in range(size):
            self.data.append(random.randrange(minimum_value, maximum_value + 1))

    def drawData(self):
        self.main_canvas.delete("all")

        canvas_width = self.max_width
        canvas_height = 400

        x_width = canvas_width / (len(self.data) + 1)
        offset = 20
        spacing = 5

        normalized_data = self.data / numpy.linalg.norm(self.data)

        for i, height in enumerate(normalized_data):
            x1 = i * x_width + offset + spacing
            y1 = canvas_height - (height * 1.25) * (800 + (len(self.data) + 12))
            x2 = (i + 1) * x_width + offset
            y2 = canvas_height

            self.main_canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white")
            self.main_canvas.create_text(x1 + ((x2 - x1) / 2), y1, anchor=S, text=str(self.data[i]), fill="white", font=("courier", 11))

    def displayData(self, value):
        if int(self.min_scale.get()) > int(self.max_scale.get()):
            return

        self.generateData()
        self.drawData()

    def sort(self):
        algorithm = self.algorithm_menu.get()
        delay = float(self.speed_scale.get())
        print(algorithm)

        algorithms = {
            "Bubble Sort": BubbleSort.BubbleSort,
            "Selection Sort": SelectionSort.SelectionSort,
            "Insertion Sort": InsertionSort.InsertionSort,
            "ShellSort": ShellSort.ShellSort,
            "QuickSort": QuickSort.QuickSort,
            "Merge Sort": MergeSort.MergeSort,
            "Heap Sort": HeapSort.HeapSort,
            "Cocktail Shaker Sort": CocktailShakerSort.CocktailShakerSort,
            "Comb Sort": CombSort.CombSort,
            "TimSort": TimSort.TimSort,
            "Counting Sort": CountSort.CountSort,
            "BogoSort": BogoSort.BogoSort
        }

        algorithms[algorithm](self.data, delay)

SSS()