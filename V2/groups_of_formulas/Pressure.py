import tkinter as tk
import threading

from tkinter import *

class Pressure(Frame):  
    def __init__(self, root): # Constructor
        super().__init__(root)
        self.Window_Creation(root)

    def Window_Creation(self, root):
        root.title("Pressure")
        root.configure(background="White")
        root.geometry("600x450")
        root.resizable(False, False)

        root.mainloop()

def start(): # Program start
    root = Tk()
    Pressure(root)