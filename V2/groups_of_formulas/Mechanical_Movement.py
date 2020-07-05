import tkinter as tk
import threading

from tkinter import *
from tkinter import ttk

class Mechanical_Movement(Frame):  
    def __init__(self, root): # Constructor
        super().__init__(root)
        self.Window_Creation(root)
        
    def Window_Creation(self, root):
        root.title("Mechanical movement")
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
            def Speed_time_distance(frame_buttons):
                
                def Selection_check():
                    if choice.get() == 0:
                        Speed_time_distance_area()

                choice = IntVar()

                CheckBut1 = Radiobutton(frame_buttons, text='Скорость, \nрасстояние, время', width=18, height=3, font=("Arial", 15), background="#ffffff", indicatoron=0, variable=choice, value=0, command=Selection_check).pack()

            List_of_buttons = [Speed_time_distance(frame_buttons)]

            for Name_Button in range(len(List_of_buttons)):
                thread = threading.Thread(target=List_of_buttons[Name_Button])
                thread.start()
            
        def Speed_time_distance_area():
            def calculator():
                pass
            lbl = Label(root, text="ʋ = S / t\nS = ʋ * t\nt = S / ʋ", font=("Arial", 17), background="#ffffff")
            lbl.place(x=370, y=20)

            lbl = Label(root, text="Введите известные значения:", font=("Arial", 13), fg="gray", background="#ffffff")
            lbl.place(x=300, y=120)

            inputS = StringVar()
            lblS = Label(root, text="S (в метрах)", font=("Arial", 10), background="#ffffff")
            lblS.place(x=272, y=169)
            entry_S = ttk.Entry(root, textvariable=inputS)
            entry_S.place(x=355, y=170)

            inputt = StringVar()
            lblS = Label(root, text="t (в секундах)", font=("Arial", 10), background="#ffffff")
            lblS.place(x=264, y=209)
            entry_t = ttk.Entry(root, textvariable=inputt)
            entry_t.place(x=355, y=210)

            inputv = StringVar()
            lblS = Label(root, text="ʋ (в метрах/секунда)", font=("Arial", 10), background="#ffffff")
            lblS.place(x=222, y=249)
            entry_v = ttk.Entry(root, textvariable=inputv)
            entry_v.place(x=355, y=250)

            ButtonEnter = ttk.Button(root, text="=", command=calculator)
            ButtonEnter.place(x=381, y=290)
            pass
        Create_buttons()

def start(): # Program start
    root = Tk()
    Mechanical_Movement(root)
    
if __name__ == '__main__': # DeBug. To run the program, without Calculator.py
    start()