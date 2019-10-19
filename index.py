import math
import time

import numpy

while True:

    form = input("\nPlease, enter the name of the formula \n(or enter the \"help\" to view the available formulas):\n")

    if form == "help": #Shows available formulas
        print("  Available formulas:")
        print("- The main\n")

    if form == "The main" or "the main":
        print("- Speed\n- Time\n- Distance")