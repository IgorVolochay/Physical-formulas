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

        print("- Speed\n- Time\n- Distance")
        answer = input()

        if fuzz.WRatio(answer, "Speed") >= 90:
            print("    Formula: v = S / t  (In meters per second)\n")
            S = float(input("Enter value - S (in meters): "))
            t = float(input("Enter value - t (in seconds): "))

            print( "v = ", S / t, " meter(s) per second")
        
        if fuzz.WRatio(answer, "Time") >= 90:
            print("    Formula: t = S / v (In seconds)")
            S = float(input("Enter value - S (in meters): "))
            v = float(input("Enter value - v (in meters per second): "))

            print( "t = ", S / v, " second(s)")

        if fuzz.WRatio(answer, "Distance") >= 90:
            print("    Formula: S = v * t (In meters)")
            v = float(input("Enter value - v (in meter per seconds): "))
            t = float(input("Enter value - t (in seconds): "))

            print("S = ", v * t, " meter(s)")