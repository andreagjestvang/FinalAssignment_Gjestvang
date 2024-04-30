"""
This is the Main.py file. It defines the main-function, that runs the interactive generator.
If Main.py is run alone, the main()-function will be tested.
"""

# Importing functions from Utilities.py
import pandas as pd
from pathlib import Path
import Utilities as ut

lpi_short = pd.read_csv("LivingPlanet.csv")
print(lpi_short)


lpi_long = pd.read_csv("LPD2022_public/LPD2022_public.csv")
print(lpi_long)







"""
def main(): 
    #emission = pd.read_csv(Path("KlimagassData.csv"), sep=";")
    
    choise = ""
    print("Welcome to the Norwegian wetland info generator :)")
    print("What info do you want to be displayed?")
    
    while choise != "Q":
        print("Statistics (S)\nGraph (G)\nHello Message (H)\nPress Q for quit")
        choise = input("Choise: ")
        if choise == "S":
            print("This is some statistics:")
        elif choise == "H":
            print("You wanted a hello message:)")
        elif choise == "G":
            print("This stops the generator and returns a graph:")
            chart = ut.graph_generator()
            choise = "Q"
            return chart
    print("You pressed Q, and quit the Wetland info generator")
    print("Thank you!")

    return
"""


# If runing main directly, run the main-function:
#if __name__ == "__main__":
#   main()