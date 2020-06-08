import tkinter as tk
import threading

from tkinter import *

class The_force_of_gravity(tk.Frame):  
    def __init__(self, root): # Constructor
        super().__init__(root)
        self.Window_Creation(root)

    def Window_Creation(self, root):
        root.title("The force of gravity")
        root.configure(background="White")
        root.geometry("600x450")
        root.resizable(False, False)

        root.mainloop()

def start(): # Program start
    root = tk.Tk()
    The_force_of_gravity(root)