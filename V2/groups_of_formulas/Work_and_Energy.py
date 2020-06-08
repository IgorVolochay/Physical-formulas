import tkinter as tk
import threading

from tkinter import *

class Work_and_Energy(tk.Frame):  
    def __init__(self, root): # Constructor
        super().__init__(root)
        self.Window_Creation(root)

    def Window_Creation(self, root):
        root.title("Work and Energy")
        root.configure(background="White")
        root.geometry("600x450")
        root.resizable(False, False)

        root.mainloop()

def start(): # Program start
    root = tk.Tk()
    Work_and_Energy(root)