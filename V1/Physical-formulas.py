import math
import tkinter as tk

from tkinter import *
import ttk

class Main(tk.Frame):

    def __init__(self, root):
        super().__init__(root)

    def openChildMechDv(self):
        ChildMechDv()

    def openChildForsT(self):
        ChildForsT()

    def openChildDav(self):
        ChildDav()

    def openChildDavG(self):
        ChildDavG()

    def openChildRabEn(self):
        ChildRabEn()

    def button_lvl1(self):
        frame = tk.Frame(root)
        frame.pack()

        Button_TheMain = tk.Button(frame, text="Механическое движение", font=("Arial", 15), width=24, height=2, command=self.openChildMechDv)
        Button_TheMain.pack(fill=tk.X, pady=20)
        Button_TheMain = tk.Button(frame, text="Сила тяжести", font=("Arial", 15), width=24, height=2, command=self.openChildForsT)
        Button_TheMain.pack(fill=tk.X, pady=20)
        Button_TheMain = tk.Button(frame, text="Давление", font=("Arial", 15), width=24, height=2, command=self.openChildDav)
        Button_TheMain.pack(fill=tk.X, pady=20)
        Button_TheMain = tk.Button(frame, text="Давление газов и жидкостей", font=("Arial", 15), width=24, height=2, command=self.openChildDavG)
        Button_TheMain.pack(fill=tk.X, pady=20)
        Button_TheMain = tk.Button(frame, text="Работа и Энергия", font=("Arial", 15), width=24, height=2, command=self.openChildRabEn)
        Button_TheMain.pack(fill=tk.X, pady=20)
        
class ChildMechDv(tk.Toplevel, tk.Frame):

    def __init__(self):
        super().__init__(root)
        self.init_childlvl1()
        
    def init_childlvl1(self):
        def Button_CheckBox():
            def lbl1():
                def calc():
                    try:
                        S = float(inputS.get())
                    except:
                        S = 0
                    try:
                        t = float(inputt.get())
                    except:
                        t = 0
                    try:
                        v = float(inputv.get())
                    except:
                        v = 0

                    if v == 0:
                        v = S / t
                        inputv.set(v)

                    if t == 0:
                        t = S / v
                        inputt.set(t)

                    if S == 0:
                        S = t * v
                        inputS.set(S)
                
                lbl = Label(self, text="ʋ = S / t\nS = ʋ * t\nt = S / ʋ", font=("Arial", 17))
                lbl.place(x=370, y=30)

                inputS = StringVar()
                lblS = Label(self, text="S (в метрах)", font=("Arial", 10))
                lblS.place(x=270, y=139)
                self.entry_S = ttk.Entry(self, textvariable=inputS)
                self.entry_S.place(x=355, y=140)

                inputt = StringVar() #переменная
                lblS = Label(self, text="t (в секундах)", font=("Arial", 10)) #текст
                lblS.place(x=262, y=179)
                self.entry_t = ttk.Entry(self, textvariable=inputt) #поле для ввода информации
                self.entry_t.place(x=355, y=180)

                inputv = StringVar()
                lblS = Label(self, text="ʋ (в метрах/секунда)", font=("Arial", 10))
                lblS.place(x=220, y=219)
                self.entry_v = ttk.Entry(self, textvariable=inputv)
                self.entry_v.place(x=355, y=220)

                ButtonEnter = ttk.Button(self, text="=", command=calc)
                ButtonEnter.place(x=381, y=260)

            if var.get() == 0:
                return lbl1()

        var = IntVar()
        var.set(0)

        self.title("Physical Formulas. Mechanical Movement")
        self.geometry("600x430")
        self.resizable(False, False)

        frame = tk.Frame(root)
        frame.pack()

        CheckBut1 = Radiobutton(self, text='Скорость, \nрасстояние, время', font=("Arial", 17), background="#fafafa", indicatoron=0, variable=var, value=0, command=Button_CheckBox)
        CheckBut1.place(x=0, y=0)

        self.grab_set()
        self.focus_set()

class ChildForsT(tk.Toplevel): #Сила тяжести
    def __init__(self): #Создание окна группы "Сила тяжести"
        super().__init__(root)
        self.init_childlvl1()
    
    #Окно:
    def init_childlvl1(self):

        def Button_CheckBox():
            def lbl1():
                
                def calc():
                    try:
                        m = float(inputm.get())
                    except:
                        m = 0
                    try:
                        g = float(inputg.get())
                    except:
                        g = 0
                    try:
                        F = float(inputF.get())
                    except:
                        F = 0
                    
                    if F == 0:
                        F = m * g
                        inputF.set(F)
                    if m == 0:
                        m = F / g
                        inputm.set(m)
                    if g == 0:
                        g = F / m
                        inputg.set(g)

                can = Canvas(self, width=400, height=600, bg='grey94')
                can.place(x=220, y=0)

                lbl = Label(self, text="F = m * g\nm = F / g\ng = F / m", font=("Arial", 17))
                lbl.place(x=370, y=30)

                inputm = StringVar()
                lblS = Label(self, text="m (в Кг)", font=("Arial", 10))
                lblS.place(x=298, y=139)
                self.entry_S = ttk.Entry(self, textvariable=inputm)
                self.entry_S.place(x=355, y=140)

                inputg = StringVar()
                lblS = Label(self, text="g (в ньютонах)", font=("Arial", 10))
                lblS.place(x=258, y=179)
                self.entry_t = ttk.Entry(self, textvariable=inputg)
                self.entry_t.place(x=355, y=180)

                inputF = StringVar()
                lblS = Label(self, text="F (в ньютонах)", font=("Arial", 10))
                lblS.place(x=258, y=219)
                self.entry_S = ttk.Entry(self, textvariable=inputF)
                self.entry_S.place(x=355, y=220)

                ButtonEnter = ttk.Button(self, text="=", command=calc)
                ButtonEnter.place(x=381, y=260)

            def lbl2():
                
                def calc():
                    try:
                        m = float(inputm.get())
                    except:
                        m = 0
                    try:
                        g = float(inputg.get())
                    except:
                        g = 0
                    try:
                        P = float(inputP.get())
                    except:
                        P = 0
                    
                    if P == 0:
                        P = m * g
                        inputP.set(P)
                    if m == 0:
                        m = P / g
                        inputm.set(m)
                    if g == 0:
                        g = P / m
                        inputg.set(g)

                can = Canvas(self, width=400, height=600, bg='grey94')
                can.place(x=220, y=0)

                lbl = Label(self, text="P = m * g\nm = P / g\ng = P / m", font=("Arial", 17))
                lbl.place(x=370, y=30)

                inputm = StringVar()
                lblS = Label(self, text="m (в Кг)", font=("Arial", 10))
                lblS.place(x=298, y=139)
                self.entry_S = ttk.Entry(self, textvariable=inputm)
                self.entry_S.place(x=355, y=140)

                inputg = StringVar()
                lblS = Label(self, text="g (в ньютонах)", font=("Arial", 10))
                lblS.place(x=258, y=179)
                self.entry_t = ttk.Entry(self, textvariable=inputg)
                self.entry_t.place(x=355, y=180)

                inputP = StringVar()
                lblS = Label(self, text="P (в ньютонах)", font=("Arial", 10))
                lblS.place(x=258, y=219)
                self.entry_S = ttk.Entry(self, textvariable=inputP)
                self.entry_S.place(x=355, y=220)

                ButtonEnter = ttk.Button(self, text="=", command=calc)
                ButtonEnter.place(x=381, y=260)

            def lbl3():
                
                def calc():
                    try:
                        m = float(inputm.get())
                    except:
                        m = 0
                    try:
                        V = float(inputV.get())
                    except:
                        V = 0
                    try:
                        ρ = float(inputρ.get())
                    except:
                        ρ = 0

                    if ρ == 0:
                        ρ = m / V
                        inputρ.set(ρ)
                    if V == 0:
                        V = m / ρ
                        inputV.set(V)
                    if m == 0:
                        m = ρ * V
                        inputm.set(m)

                can = Canvas(self, width=400, height=600, bg='grey94')
                can.place(x=220, y=0)

                lbl = Label(self, text="ρ = m / V\nV = m / ρ\nm = ρ * V", font=("Arial", 17))
                lbl.place(x=370, y=30)

                inputm = StringVar()
                lblS = Label(self, text="m (в Кг)", font=("Arial", 10))
                lblS.place(x=298, y=139)
                self.entry_S = ttk.Entry(self, textvariable=inputm)
                self.entry_S.place(x=355, y=140)

                inputV = StringVar()
                lblS = Label(self, text="V (в метр^3)", font=("Arial", 10))
                lblS.place(x=273, y=179)
                self.entry_t = ttk.Entry(self, textvariable=inputV)
                self.entry_t.place(x=355, y=180)

                inputρ = StringVar()
                lblS = Label(self, text="ρ (в Кг/метр^2)", font=("Arial", 10))
                lblS.place(x=260, y=219)
                self.entry_S = ttk.Entry(self, textvariable=inputρ)
                self.entry_S.place(x=355, y=220)

                ButtonEnter = ttk.Button(self, text="=", command=calc)
                ButtonEnter.place(x=381, y=260)

            if var.get() == 0:
                return lbl1()
            if var.get() == 1:
                return lbl2()
            if var.get() == 3:
                return lbl3()

        var = IntVar()
        var.set(0)

        self.title("Physical Formulas. Gravity")
        self.geometry("600x430")
        self.resizable(False, False)

        frame = tk.Frame(root)
        frame.pack()

        CheckBut1 = Radiobutton(self, text='Сила тяжести \nмасса, гравитация', background="#fafafa" , font=("Arial", 17), width=15, height=2, indicatoron=0, variable=var, value=0, command=Button_CheckBox)
        CheckBut1.place(x=0, y=0)
        CheckBut2 = Radiobutton(self, text='Вес \nмасса, гравитация', background="#fafafa" , font=("Arial", 17), width=15, height=2, indicatoron=0, variable=var, value=1, command=Button_CheckBox)
        CheckBut2.place(x=0, y=120)
        CheckBut3 = Radiobutton(self, text='Плотность\nобъём, масса', background="#fafafa" , font=("Arial", 17), width=15, height=2, indicatoron=0, variable=var, value=3, command=Button_CheckBox)
        CheckBut3.place(x=0, y=240)


        #Фокусировка на дочернем окне:
        self.grab_set()
        self.focus_set()

class ChildDav(tk.Toplevel): #Давление
    def __init__(self): #Создание окна группы "Давление"
        super().__init__(root)
        self.init_childlvl1()
    
    #Окно:
    def init_childlvl1(self):

        def Button_CheckBox():
            def lbl1():
                
                def calc():
                    try:
                        F = float(inputF.get())
                    except:
                        F = 0
                    try:    
                        S = float(inputS.get())
                    except:
                        S = 0
                    try:
                        p = float(inputp.get())
                    except:
                        p = 0

                    if p == 0:
                        p = F / S
                        inputp.set(p)
                    if F == 0:
                        F = p * S
                        inputF.set(F)
                    if S == 0:
                        S = F / p
                        inputS.set(S)

                can = Canvas(self, width=400, height=600, bg='grey94')
                can.place(x=220, y=0)

                lbl = Label(self, text="p = F / S\nF = p * S\nS = F / p", font=("Arial", 17))
                lbl.place(x=370, y=30)
                
                inputF = StringVar()
                lblS = Label(self, text="F (в ньютонах)", font=("Arial", 10))
                lblS.place(x=257, y=139)
                self.entry_S = ttk.Entry(self, textvariable=inputF)
                self.entry_S.place(x=355, y=140)

                inputS = StringVar()
                lblS = Label(self, text="S (в метр^2)", font=("Arial", 10))
                lblS.place(x=273, y=179)
                self.entry_t = ttk.Entry(self, textvariable=inputS)
                self.entry_t.place(x=355, y=180)

                inputp = StringVar()
                lblS = Label(self, text="p (в паскалях)", font=("Arial", 10))
                lblS.place(x=260, y=219)
                self.entry_S = ttk.Entry(self, textvariable=inputp)
                self.entry_S.place(x=355, y=220)

                ButtonEnter = ttk.Button(self, text="=", command=calc)
                ButtonEnter.place(x=381, y=260)

            if var.get() == 0:
                return lbl1()

        var = IntVar()
        var.set(0)

        self.title("Physical Formulas. Pressure")
        self.geometry("600x430")
        self.resizable(False, False)

        frame = tk.Frame(root)
        frame.pack()

        CheckBut1 = Radiobutton(self, text='Давление,\nсила, площадь', background="#fafafa" , font=("Arial", 18), width=15, height=2, indicatoron=0, variable=var, value=0, command=Button_CheckBox)
        CheckBut1.place(x=0, y=0)


        #Фокусировка на дочернем окне:
        self.grab_set()
        self.focus_set()

class ChildDavG(tk.Toplevel): #Давление газов и жидкостей
    def __init__(self): #Создание окна группы "Давление газов и жидкостей"
        super().__init__(root)
        self.init_childlvl1()
    
    #Окно:
    def init_childlvl1(self):
        def Button_CheckBox():
            #l = Label(self, width=5, height=1)
            def lbl1():
                
                def calc():
                    try:
                        g = float(inputg.get())
                    except:
                        g = 0
                    try:
                        ρ = float(inputρ.get())
                    except:
                        ρ = 0
                    try:
                        h = float(inputh.get())
                    except:
                        h = 0
                    try:
                        p = float(inputp.get())
                    except:
                        p = 0

                    if p == 0:
                        p = g*ρ*h
                        inputp.set(p)
                    if g == 0:
                        g = p / (h * ρ)
                        inputg.set(g)
                    if ρ == 0:
                        ρ = p / (g * h)
                        inputρ.set(ρ)
                    if h == 0:
                        h = p / (g * ρ)
                        inputh.set(h)

                can = Canvas(self, width=400, height=600, bg='grey94')
                can.place(x=220, y=0)

                lbl = Label(self, text="p = g * ρ * h\ng = p / (h * ρ)\nρ = p / (g * h)\nh = p / (g * ρ)", font=("Arial", 17))
                lbl.place(x=350, y=10)
                
                inputg = StringVar()
                #inputS.set(1)
                lblS = Label(self, text="g (в ньютонах)", font=("Arial", 10))
                lblS.place(x=257, y=139)
                self.entry_S = ttk.Entry(self, textvariable=inputg)
                self.entry_S.place(x=355, y=140)

                inputρ = StringVar()
                #inputt.set(1)
                lblS = Label(self, text="ρ (в Кг/метр^3)", font=("Arial", 10))
                lblS.place(x=257, y=179)
                self.entry_t = ttk.Entry(self, textvariable=inputρ)
                self.entry_t.place(x=355, y=180)

                inputh = StringVar()
                #inputt.set(1)
                lblS = Label(self, text="h (в метрах)", font=("Arial", 10))
                lblS.place(x=273, y=219)
                self.entry_t = ttk.Entry(self, textvariable=inputh)
                self.entry_t.place(x=355, y=220)

                inputp = StringVar()
                lblS = Label(self, text="p (в паскалях)", font=("Arial", 10))
                lblS.place(x=260, y=259)
                self.entry_S = ttk.Entry(self, textvariable=inputp)
                self.entry_S.place(x=355, y=260)

                ButtonEnter = ttk.Button(self, text="=", command=calc)
                ButtonEnter.place(x=381, y=300)

            def lbl2():
                
                def calc():
                    try:
                        ρ = float(inputρ.get())
                    except:
                        ρ = 0
                    try:
                        g = float(inputg.get())
                    except:
                        g = 0
                    try:
                        V = float(inputV.get())
                    except:
                        V = 0
                    try:
                        F = float(inputF.get())
                    except:
                        F = 0
                    
                    if F == 0:
                        F = ρ * g * V
                        inputF.set(F)
                    if ρ == 0:
                        ρ = F / (g * V)
                        inputρ.set(ρ)
                    if g == 0:
                        g = F / (ρ * V)
                        inputg.set(g)
                    if V == 0:
                        V = F / (g * ρ)
                        inputV.set(V)

                can = Canvas(self, width=400, height=600, bg='grey94')
                can.place(x=220, y=0)

                lbl = Label(self, text="F = ρ * g * V\nρ = F / (g * V)\ng = F / (ρ * V)\nV = F / (g * ρ)", font=("Arial", 17))
                lbl.place(x=350, y=10)

                inputρ = StringVar()
                #inputt.set(1)
                lblS = Label(self, text="ρ (в Кг/метр^3)", font=("Arial", 10))
                lblS.place(x=257, y=139)
                self.entry_t = ttk.Entry(self, textvariable=inputρ)
                self.entry_t.place(x=355, y=140)

                inputg = StringVar()
                #inputS.set(1)
                lblS = Label(self, text="g (в ньютонах)", font=("Arial", 10))
                lblS.place(x=257, y=179)
                self.entry_S = ttk.Entry(self, textvariable=inputg)
                self.entry_S.place(x=355, y=180)

                inputV = StringVar()
                #inputt.set(1)
                lblS = Label(self, text="V (в метрах^3)", font=("Arial", 10))
                lblS.place(x=259, y=219)
                self.entry_t = ttk.Entry(self, textvariable=inputV)
                self.entry_t.place(x=355, y=220)

                inputF = StringVar()
                lblS = Label(self, text="F (в ньютонах)", font=("Arial", 10))
                lblS.place(x=257, y=259)
                self.entry_S = ttk.Entry(self, textvariable=inputF)
                self.entry_S.place(x=355, y=260)

                ButtonEnter = ttk.Button(self, text="=", command=calc)
                ButtonEnter.place(x=381, y=300)

            if var.get() == 0:
                return lbl1()
            if var.get() == 1:
                return lbl2()

        var = IntVar()
        var.set(0)

        self.title("Physical Formulas. Pressure")
        self.geometry("600x430")
        self.resizable(False, False)

        frame = tk.Frame(root)
        frame.pack()

        CheckBut1 = Radiobutton(self, text='Дав. жидкости', background="#fafafa" , font=("Arial", 18), width=15, height=2, indicatoron=0, variable=var, value=0, command=Button_CheckBox)
        CheckBut1.place(x=0, y=0)
        CheckBut2 = Radiobutton(self, text='Закон Архимеда', background="#fafafa" , font=("Arial", 18), width=15, height=2, indicatoron=0, variable=var, value=1, command=Button_CheckBox)
        CheckBut2.place(x=0, y=120)


        #Фокусировка на дочернем окне:
        self.grab_set()
        self.focus_set()










class ChildRabEn(tk.Toplevel): #Работа и Энергия
    def __init__(self): #Создание окна группы "Работа и Энергия"
        super().__init__(root)
        self.init_childlvl1()
    
    #Окно:
    def init_childlvl1(self):
        def Button_CheckBox():
            #l = Label(self, width=5, height=1)
            def lbl1():
                
                def calc():
                    try:
                        F = float(inputF.get())
                    except:
                        F = 0
                    try:
                        S = float(inputS.get())
                    except:
                        S = 0
                    try:
                        A = float(inputA.get())
                    except:
                        A = 0

                    if A == 0:
                        A = F * S
                        inputA.set(A)
                    if F == 0:
                        F = A / S
                        inputF.set(F)
                    if S == 0:
                        S = A / F
                        inputS.set(S)
                    

                can = Canvas(self, width=400, height=600, bg='grey94')
                can.place(x=220, y=0)

                lbl = Label(self, text="А = F * S\nF = A / S\nS = A / F", font=("Arial", 17))
                lbl.place(x=370, y=30)

                inputF = StringVar()
                lblS = Label(self, text="F (в ньютонах)", font=("Arial", 10))
                lblS.place(x=257, y=139)
                self.entry_S = ttk.Entry(self, textvariable=inputF)
                self.entry_S.place(x=355, y=140)

                inputS = StringVar()
                lblS = Label(self, text="S (в метрах)", font=("Arial", 10))
                lblS.place(x=271, y=179)
                self.entry_t = ttk.Entry(self, textvariable=inputS)
                self.entry_t.place(x=355, y=180)

                inputA = StringVar()
                lblS = Label(self, text="A (в джоулях)", font=("Arial", 10))
                lblS.place(x=260, y=219)
                self.entry_S = ttk.Entry(self, textvariable=inputA)
                self.entry_S.place(x=355, y=220)

                ButtonEnter = ttk.Button(self, text="=", command=calc)
                ButtonEnter.place(x=381, y=260)

            def lbl2():
                
                def calc():
                    try:
                        Ap = float(inputAp.get())
                    except:
                        Ap = 0
                    try:
                        Av = float(inputAv.get())
                    except:
                        Av = 0
                    try:
                        ɳ = float(inputɳ.get())
                    except:
                        ɳ = 0

                    if ɳ == 0:
                        ɳ = Ap / Av * 100
                        inputɳ.set(ɳ)
                    if Ap == 0:
                        Ap = ɳ / Av * 100
                        inputAp.set(Ap)
                    if Av == 0:
                        Av = ɳ / Ap * 100
                        inputAv.set(Av)

                can = Canvas(self, width=400, height=600, bg='grey94')
                can.place(x=220, y=0)

                lbl = Label(self, text="ɳ = А(П) / А(В) * 100%\nA(П) = ɳ / A(В) * 100\nA(В) = ɳ / A(П) * 100", font=("Arial", 17))
                lbl.place(x=290, y=30)

                inputAp = StringVar()
                lblS = Label(self, text="A (полезная работа)", font=("Arial", 10))
                lblS.place(x=225, y=139)
                self.entry_S = ttk.Entry(self, textvariable=inputAp)
                self.entry_S.place(x=355, y=140)

                inputAv = StringVar()
                lblS = Label(self, text="A (вся работа)", font=("Arial", 10))
                lblS.place(x=259, y=179)
                self.entry_t = ttk.Entry(self, textvariable=inputAv)
                self.entry_t.place(x=355, y=180)

                inputɳ = StringVar()
                lblS = Label(self, text="ɳ (в процентах)", font=("Arial", 10))
                lblS.place(x=253, y=219)
                self.entry_S = ttk.Entry(self, textvariable=inputɳ)
                self.entry_S.place(x=355, y=220)

                ButtonEnter = ttk.Button(self, text="=", command=calc)
                ButtonEnter.place(x=381, y=260)
                
            def lbl3():
                
                def calc():
                    try:
                        m = float(inputm.get())
                    except:
                        m = 0
                    try:
                        g = float(inputg.get())
                    except:
                        g = 0
                    try:
                        h = float(inputh.get())
                    except:
                        h = 0
                    try:
                        E = float(inputE.get())
                    except:
                        E = 0

                    if E == 0:
                        E = m * g * h
                        inputE.set(E)
                    if m == 0:
                        m = E / (g * h)
                        inputm.set(m)
                    if g == 0:
                        g = E / (m * h)
                        inputg.set(g)
                    if h == 0:
                        h = E / (g * m)
                        inputh.set(h)

                can = Canvas(self, width=400, height=600, bg='grey94')
                can.place(x=220, y=0)

                lbl = Label(self, text="E(П) = m * g * h\nm = E(П) / (g * h)\ng = E(П) / (m * h)\nh = E(П) / (g * m)", font=("Arial", 17))
                lbl.place(x=325, y=10)
                
                inputm = StringVar()
                lblS = Label(self, text="m (в Кг)", font=("Arial", 10))
                lblS.place(x=298, y=139)
                self.entry_t = ttk.Entry(self, textvariable=inputm)
                self.entry_t.place(x=355, y=140)

                inputg = StringVar()
                lblS = Label(self, text="g (в ньютонах)", font=("Arial", 10))
                lblS.place(x=258, y=179)
                self.entry_S = ttk.Entry(self, textvariable=inputg)
                self.entry_S.place(x=355, y=180)

                inputh = StringVar()
                lblS = Label(self, text="h (в метрах)", font=("Arial", 10))
                lblS.place(x=272, y=219)
                self.entry_t = ttk.Entry(self, textvariable=inputh)
                self.entry_t.place(x=355, y=220)

                ButtonEnter = ttk.Button(self, text="=", command=calc)
                ButtonEnter.place(x=381, y=300)

                inputE = StringVar()
                lblS = Label(self, text="E (в джоулях)", font=("Arial", 10))
                lblS.place(x=260, y=259)
                self.entry_S = ttk.Entry(self, textvariable=inputE)
                self.entry_S.place(x=355, y=260)

            def lbl4():
                
                def calc():
                    try:
                        m = float(inputm.get())
                    except:
                        m = 0
                    try:
                        ʋ = float(inputʋ.get())
                    except:
                        ʋ = 0
                    try:
                        E = float(inputE.get())
                    except:
                        E = 0

                    if E == 0:
                        E = m * ʋ ** 2 / 2
                        inputE.set(E)
                    if m == 0:
                        m = E / (ʋ ** 2 / 2)
                        inputm.set(m)
                    if ʋ == 0:
                        ʋ = math.sqrt((E / m) * 2)
                        inputʋ.set(ʋ)


                can = Canvas(self, width=400, height=600, bg='grey94')
                can.place(x=220, y=0)

                lbl = Label(self, text="Е(К) = m * ʋ^2 / 2\nm = E(К) / (ʋ^2 / 2)\nʋ = √(E(К) / m) * 2", font=("Arial", 17))
                lbl.place(x=310, y=30)

                inputm = StringVar()
                lblS = Label(self, text="m (в Кг)", font=("Arial", 10))
                lblS.place(x=298, y=139)
                self.entry_S = ttk.Entry(self, textvariable=inputm)
                self.entry_S.place(x=355, y=140)

                inputʋ = StringVar()
                lblS = Label(self, text="ʋ (в мертр/секунда)", font=("Arial", 10))
                lblS.place(x=227, y=179)
                self.entry_t = ttk.Entry(self, textvariable=inputʋ)
                self.entry_t.place(x=355, y=180)

                inputE = StringVar()
                lblS = Label(self, text="E (в джоулях)", font=("Arial", 10))
                lblS.place(x=260, y=219)
                self.entry_S = ttk.Entry(self, textvariable=inputE)
                self.entry_S.place(x=355, y=220)

                ButtonEnter = ttk.Button(self, text="=", command=calc)
                ButtonEnter.place(x=381, y=260)

            def lbl5():
                
                def calc():
                    try:
                        A = float(inputA.get())
                    except:
                        A = 0
                    try:
                        t = float(inputt.get())
                    except:
                        t = 0
                    try:
                        N = float(inputN.get())
                    except:
                        N = 0

                    if N == 0:
                        N = A / t
                        inputN.set(N)
                    if A == 0:
                        A = N * t
                        inputA.set(A)
                    if t == 0:
                        t = A / N
                        inputt.set(t)

                can = Canvas(self, width=400, height=600, bg='grey94')
                can.place(x=220, y=0)

                lbl = Label(self, text="N = A / t\nA = N * t\nt = A / N", font=("Arial", 17))
                lbl.place(x=370, y=30)

                inputA = StringVar()
                lblS = Label(self, text="A (в джоулях)", font=("Arial", 10))
                lblS.place(x=261, y=139)
                self.entry_S = ttk.Entry(self, textvariable=inputA)
                self.entry_S.place(x=355, y=140)

                inputt = StringVar()
                lblS = Label(self, text="t (в секундах)", font=("Arial", 10))
                lblS.place(x=262, y=179)
                self.entry_t = ttk.Entry(self, textvariable=inputt)
                self.entry_t.place(x=355, y=180)

                inputN = StringVar()
                lblS = Label(self, text="N (в Вт)", font=("Arial", 10))
                lblS.place(x=298, y=219)
                self.entry_S = ttk.Entry(self, textvariable=inputN)
                self.entry_S.place(x=355, y=220)

                ButtonEnter = ttk.Button(self, text="=", command=calc)
                ButtonEnter.place(x=381, y=260)

            if var.get() == 0:
                return lbl1()
            if var.get() == 1:
                return lbl2()
            if var.get() == 2:
                return lbl3()
            if var.get() == 3:
                return lbl4()
            if var.get() == 4:
                return lbl5()

        var = IntVar()
        var.set(0)

        self.title("Physical Formulas. Action and energy")
        self.geometry("600x600")
        self.resizable(False, False)

        frame = tk.Frame(root)
        frame.pack()

        CheckBut1 = Radiobutton(self, text='Работа,\nрасстояние, сила', background="#fafafa" , font=("Arial", 18), width=15, height=2, indicatoron=0, variable=var, value=0, command=Button_CheckBox)
        CheckBut1.place(x=0, y=0)
        CheckBut2 = Radiobutton(self, text='КПД', background="#fafafa" , font=("Arial", 18), width=15, height=2, indicatoron=0, variable=var, value=1, command=Button_CheckBox)
        CheckBut2.place(x=0, y=120)
        CheckBut3 = Radiobutton(self, text='П. энергия,\nмасса, высота', background="#fafafa" , font=("Arial", 18), width=15, height=2, indicatoron=0, variable=var, value=2, command=Button_CheckBox)
        CheckBut3.place(x=0, y=240)
        CheckBut3 = Radiobutton(self, text='К. энергия\nмасса, скорость', background="#fafafa" , font=("Arial", 18), width=15, height=2, indicatoron=0, variable=var, value=3, command=Button_CheckBox)
        CheckBut3.place(x=0, y=360)
        CheckBut3 = Radiobutton(self, text='Мощность,\nработа, время', background="#fafafa" , font=("Arial", 18), width=15, height=2, indicatoron=0, variable=var, value=4, command=Button_CheckBox)
        CheckBut3.place(x=0, y=480)


        #Фокусировка на дочернем окне:
        self.grab_set()
        self.focus_set()

#Основной код:
if __name__ == "__main__": 
    
    root = tk.Tk() #Присвоение значения переменной root
    app = Main(root) #Обращение к классу Main

    root.title("Physical Formulas")
    root.geometry("600x610")
    root.resizable(False, False)

    lbl = tk.Label(root, text="Выберете группу", font=("Arial", 25), justify=tk.CENTER)
    lbl.pack(fill=tk.X, pady=20)

    app.button_lvl1() #Создание кнопок


    root.mainloop() #Цикл