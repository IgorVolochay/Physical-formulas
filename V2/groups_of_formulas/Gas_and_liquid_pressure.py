import tkinter as tk
import threading

from tkinter import *

class Gas_and_liquid_pressure(Frame):  
    def __init__(self, root): # Constructor
        super().__init__(root)
        self.Window_Creation(root)

    def Window_Creation(self, root):
        root.title("Gas and liquid pressure")
        root.configure(background="White")
        root.geometry("600x450")
        root.resizable(False, False)

        self.Scroll_panel(root)

        root.mainloop()

    def Scroll_panel(self, root):
        frame = Frame(root)
        frame.pack(side=LEFT)

        # Add a canvas in that frame
        Can1 = Canvas(frame, bg="White")
        Can1.pack(side=LEFT)

        # Link a scrollbar to the canvas
        vsbar = Scrollbar(frame, orient="vertical", command=Can1.yview)
        vsbar.pack()
        Can1.configure(yscrollcommand=vsbar.set)

        def on_mousewheel(event): # Mouse scroll function
            Can1.yview_scroll(int(-1*(event.delta/120)), "units")
        Can1.bind_all("<MouseWheel>", on_mousewheel)

        # Create a frame to contain the buttons
        frame_buttons = Frame(Can1, bg="White", relief=GROOVE)
        Can1.create_window((5,5), window=frame_buttons)

        # Bind the buttons frame to a function that fixes the Canvas size
        def resize(event):
            Can1.configure(scrollregion=Can1.bbox("all"), width=200, height=550)
        frame_buttons.bind("<Configure>", resize)

        def Create_buttons():
            choice = IntVar()

            def Fluid_pressure():
                CheckBut1 = Radiobutton(frame_buttons, text='Дав. жидкости', width=18, height=3, font=("Arial", 15), background="#fafafa", indicatoron=0, variable=choice, value=0)
                CheckBut1.pack()

            def Archimedes_law():
                CheckBut1 = Radiobutton(frame_buttons, text='Закон Архимеда', width=18, height=3, font=("Arial", 15), background="#fafafa", indicatoron=0, variable=choice, value=1)
                CheckBut1.pack(pady=10)

            List_of_buttons = [Fluid_pressure(), Archimedes_law()]

            for Name_Button in range(len(List_of_buttons)):
                thread = threading.Thread(target=List_of_buttons[Name_Button])
                thread.start()

        Create_buttons()

def start(): # Program start
    root = Tk()
    Gas_and_liquid_pressure(root)

if __name__ == '__main__': # DeBug. To run the program, without Calculator.py
    start()