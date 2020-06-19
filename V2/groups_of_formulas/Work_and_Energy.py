import tkinter as tk
import threading

from tkinter import *

class Work_and_Energy(Frame):  
    def __init__(self, root): # Constructor
        super().__init__(root)
        self.Window_Creation(root)

    def Window_Creation(self, root):
        root.title("Work and Energy")
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

            def Work_Distance_Strength():
                CheckBut1 = Radiobutton(frame_buttons, text='Работа,\nрасстояние, сила', width=18, height=3, font=("Arial", 15), background="#fafafa", indicatoron=0, variable=choice, value=0)
                CheckBut1.pack()

            def Efficiency():
                CheckBut1 = Radiobutton(frame_buttons, text='КПД', width=18, height=3, font=("Arial", 15), background="#fafafa", indicatoron=0, variable=choice, value=1)
                CheckBut1.pack(pady=10)

            def Potential_energy_Mass_Height():
                CheckBut1 = Radiobutton(frame_buttons, text='П. энергия,\nмасса, высота', width=18, height=3, font=("Arial", 15), background="#fafafa", indicatoron=0, variable=choice, value=2)
                CheckBut1.pack(pady=10)

            def Kinetic_energy_Mass_Height():
                CheckBut1 = Radiobutton(frame_buttons, text='К. энергия,\nмасса, скорость', width=18, height=3, font=("Arial", 15), background="#fafafa", indicatoron=0, variable=choice, value=3)
                CheckBut1.pack(pady=10)

            def Power_work_time():
                CheckBut1 = Radiobutton(frame_buttons, text='Мощность,\nработа, время', width=18, height=3, font=("Arial", 15), background="#fafafa", indicatoron=0, variable=choice, value=4)
                CheckBut1.pack(pady=10)

            List_of_buttons = [Work_Distance_Strength(), Efficiency(), Potential_energy_Mass_Height(), Kinetic_energy_Mass_Height(), Power_work_time()]

            for Name_Button in range(len(List_of_buttons)):
                thread = threading.Thread(target=List_of_buttons[Name_Button])
                thread.start()

        Create_buttons()

def start(): # Program start
    root = Tk()
    Work_and_Energy(root)

if __name__ == '__main__': # DeBug. To run the program, without Calculator.py
    start()