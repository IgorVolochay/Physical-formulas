import tkinter as tk
import threading

from tkinter import *

class Mechanical_Movement(tk.Frame):  
    def __init__(self, root):
        super().__init__(root)
        self.Window_Creation(root)

    def Window_Creation(self, root):
        root.title("Mechanical movement")
        root.configure(background="White")
        root.geometry("600x450")
        root.resizable(False, False)

        root.mainloop()

def start():
    root = tk.Tk()
    Mechanical_Movement(root)