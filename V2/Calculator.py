import threading
import tkinter as tk
import math
#import ttk
from datetime import datetime

from tkinter import *

class MainWindow(tk.Frame):
    def __init__(self, root):
        print("class MainWindow time spent:", datetime.now() - start_time) #Debug

        super().__init__(root)

        self.thread = threading.Thread(target=self.WindowCreation(root))
        self.thread.start()
        self.thread.join()

    def WindowCreation(self, root):
        root.title("Physical Formulas")
        root.configure(background="White")
        root.geometry("600x610")
        root.resizable(False, False)

        print("WindowCreation time spent:", datetime.now() - start_time) #Debug

        root.lbl = tk.Label(root, text="Выберете группу", font=("Arial", 20), bg="White", justify=tk.CENTER)
        root.lbl.pack(fill=tk.X, pady=10)

        root.thread = threading.Thread(target=self.button())
        root.thread.start()
        root.thread.join()

        root.mainloop()

    def button(self):
        frame = tk.Frame(root)
        frame.pack(pady=0)

        # Add a canvas in that frame
        Can1 = tk.Canvas(frame, bg="White")
        Can1.pack(side=LEFT)

        # Link a scrollbar to the canvas
        vsbar = tk.Scrollbar(frame, orient="vertical", command=Can1.yview)
        vsbar.pack()
        Can1.configure(yscrollcommand=vsbar.set)

        def _on_mousewheel(event):
            Can1.yview_scroll(int(-1*(event.delta/120)), "units")
        Can1.bind_all("<MouseWheel>", _on_mousewheel)

        # Create a frame to contain the buttons
        frame_buttons = tk.Frame(Can1, bg="White", relief=tk.GROOVE)
        Can1.create_window((5,5), window=frame_buttons)

        # Bind the buttons frame to a function that fixes the Canvas size
        def resize(event):
            Can1.configure(scrollregion=Can1.bbox("all"), width=600, height=550)
        frame_buttons.bind("<Configure>", resize)

        # Add the buttons to the frame
        Button_TheMain = tk.Button(frame_buttons, text="Механическое движение", font=("Arial", 15), width=32, height=2).pack(padx=120, pady=20)
        Button_TheMain = tk.Button(frame_buttons, text="Сила тяжести", font=("Arial", 15), width=32, height=2).pack(padx=120, pady=20)
        Button_TheMain = tk.Button(frame_buttons, text="Давление", font=("Arial", 15), width=32, height=2).pack(padx=120, pady=20)
        Button_TheMain = tk.Button(frame_buttons, text="Давление газов и жидкостей", font=("Arial", 15), width=32, height=2).pack(padx=120, pady=20)
        Button_TheMain = tk.Button(frame_buttons, text="Работа и Энергия", font=("Arial", 15), width=32, height=2).pack(padx=120, pady=20)

if __name__ == "__main__":
    start_time = datetime.now() #Debug

    root = tk.Tk()
    MainWindow(root)
    pass