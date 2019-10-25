import math
import time

import numpy
from fuzzywuzzy import fuzz

while True:

    form = input("\nPlease, enter the name of the formula \n(or enter the \"help\" to view the available formulas):\n")

    if form == "help": #Shows available formulas
        print("  Available formulas:")
        print("- The main\n")

    if fuzz.WRatio(form, "The main") >= 90:

        print("- Speed\n- Time\n- Distance\n\n- Force of gravity\n- Weight\n- Mass\n- Density")
        answer = input()

        #first group:
        if fuzz.WRatio(answer, "Speed") >= 90: #Speed
            print("    Formula: v = S / t  (In meters per second)\n")
            S = float(input("Enter value - S (in meters): "))
            t = float(input("Enter value - t (in seconds): "))

            print( "v = ", S / t, " meter(s) per second")
        
        if fuzz.WRatio(answer, "Time") >= 90: #Time
            print("    Formula: t = S / v (In seconds)")
            S = float(input("Enter value - S (in meters): "))
            v = float(input("Enter value - v (in meters per second): "))

            print( "t = ", S / v, " second(s)")

        if fuzz.WRatio(answer, "Distance") >= 90: #Distance
            print("    Formula: S = v * t (In meters)")
            v = float(input("Enter value - v (in meter per seconds): "))
            t = float(input("Enter value - t (in seconds): "))

            print("S = ", v * t, " meter(s)")

        #Second group:
        if fuzz.WRatio(answer, "Force of gravity") >= 90: #Force of gravity
            print("    Formula: F = m * g (in newton)")
            m = float(input("Enter value - m (in kilogram): "))
            g = float(input("Enter value - g (on earth - 9.8): "))

            print("F = ", m * g, " newton(s)")

        if fuzz.WRatio(answer, "Weight") >= 90: #Whight
            print("    Formula: P = m * g (in newton)")
            m = float(input("Enter value - m (in kilogram): "))
            g = float(input("Enter value - g (on earth - 9.8): "))

            print("P = ", m * g, " newton(s)")

        if fuzz.WRatio(answer, "Mass") >= 90: #Mass
            print("    Formula: m = P / g")
            P = float(input("Enetr value - P (in newton): "))
            g = float(input("Enter value - g (on earth - 9.8): "))

            print("m = ", P / g, " kilogram(s)")

        if fuzz.WRatio(answer, "Density") >= 90: #Density
            print("    Formula: ρ = m / V (in kilogram/meter³)")
            m = float(input("Enter value - m (in kilogram)"))
            V = float(input("Enter value - V (in meter³)"))

            print("ρ = ", m / V, " kilogram/meter³")