import threading
import tkinter as tk
#import ttk

from datetime import datetime
from tkinter import *

class Main_Window(Frame):
    def __init__(self, root): # Constructor
        print("class MainWindow time spent:", datetime.now() - start_time) #Debug

        super().__init__(root)

        self.thread = threading.Thread(target=self.Window_Creation(root)) # Call to the Window_Creation function using multithreading
        self.thread.start()
        self.thread.join()

    def Window_Creation(self, root):
        root.title("Physical Formulas")
        root.configure(background="White")
        root.geometry("600x610")
        root.resizable(False, False)

        print("WindowCreation time spent:", datetime.now() - start_time) #Debug

        root.lbl = Label(root, text="Выберете группу", font=("Arial", 20), bg="White", justify=CENTER)
        root.lbl.pack(fill=X, pady=10)

        root.thread = threading.Thread(target=self.Action_Field_And_Buttons()) # Call to button function using multithreading
        root.thread.start()
        root.thread.join()

        root.mainloop()

    def Action_Field_And_Buttons(self):
        frame = Frame(root)
        frame.pack(pady=0)

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
            Can1.configure(scrollregion=Can1.bbox("all"), width=600, height=550)
        frame_buttons.bind("<Configure>", resize)

        def Create_Buttons_Using_Multithreading():

            #Add files and buttons - here:

            def _Mech_Move():
                from groups_of_formulas import Mechanical_Movement
                Button_TheMain = Button(frame_buttons, text="Механическое движение", font=("Arial", 15), width=32, height=2, command=Mechanical_Movement.start).pack(padx=120, pady=20)

            def _The_Force_Of_Grav():
                from groups_of_formulas import The_force_of_gravity
                Button_TheMain = Button(frame_buttons, text="Сила тяжести", font=("Arial", 15), width=32, height=2, command=The_force_of_gravity.start).pack(padx=120, pady=20)

            def _Pressure():
                from groups_of_formulas import Pressure
                Button_TheMain = Button(frame_buttons, text="Давление", font=("Arial", 15), width=32, height=2, command=Pressure.start).pack(padx=120, pady=20)

            def _Gas_And_Liquid_Pressure():
                from groups_of_formulas import Gas_and_liquid_pressure
                Button_TheMain = Button(frame_buttons, text="Давление газов и жидкостей", font=("Arial", 15), width=32, height=2, command=Gas_and_liquid_pressure.start).pack(padx=120, pady=20)

            def _Work_and_Energy():
                from groups_of_formulas import Work_and_Energy
                Button_TheMain = Button(frame_buttons, text="Работа и Энергия", font=("Arial", 15), width=32, height=2, command=Work_and_Energy.start).pack(padx=120, pady=20)

            #When you create the function, add it here:
            List_Of_Buttons = [_Mech_Move(), _The_Force_Of_Grav(), _Pressure(), _Gas_And_Liquid_Pressure(), _Work_and_Energy()]

            #Distribution of button creation on different threads:
            for Name_Button in range(len(List_Of_Buttons)):
                thread = threading.Thread(target=List_Of_Buttons[Name_Button])
                thread.start()

        Create_Buttons_Using_Multithreading()

if __name__ == "__main__":
    start_time = datetime.now() #Debug

    root = Tk()
    Main_Window(root)
    pass