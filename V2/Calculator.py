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
        self.thread1 = threading.Thread(target=self.WindowCreation(root))
        self.thread1.start()
        self.thread1.join()

    def WindowCreation(self, root):
        root.title("Physical Formulas")
        root.geometry("600x610")
        root.resizable(False, False)

        print("WindowCreation time spent:", datetime.now() - start_time) #Debug

        root.mainloop()

if __name__ == "__main__":
    start_time = datetime.now() #Debug

    root = tk.Tk()
    MainWindow(root)
    pass