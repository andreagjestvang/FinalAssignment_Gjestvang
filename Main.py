"""
This is the Main.py file. It defines the main-function, that runs the interactive generator.
If Main.py is run alone, the main()-function will be tested.
"""

# Importing functions from Utilities.py
#import pandas as pd
import Utilities as ut
from asciimatics.screen import Screen
import time

def main(): 
    """ doc string: 
    """
    pasvik_summer = ut.MET_data_loader("Pasvik_rain.csv")

    #Making an dictionary to store the information:
    collected_information = {}

    program_choise = ""
    print("Welcome to P-PIG, the Pasvik Precipitation Info Generator! :)\n")
    
    while program_choise != "Q":
        print("Please choose what you want to generate: \n")
        print("- Choose to examine the mean of a specific period (P)")
        print("- Choose to save collected info to file (F)")
        print("- Create a graph (G)")
        print("- Quit Generator (Q) \n")
        
        # Taking input from user
        program_choise = input("Your input: ")
        chosen_list = []
        
        if program_choise == "P" or program_choise == "p":
            #Saving the chosen list [chosen_dataset, chosen_years, mean_per]:
            chosen_list = ut.choose_year_function(pasvik_summer)

            #Updating the dictionary based on chosen year function:
            collected_information.update({str(chosen_list[1]) : float(chosen_list[2])})
            
            print("\nHere are the chosen years from the dataset: ")
            print(chosen_list[0].loc[chosen_list[0]['Chosen'] == True])
            
            print(f"The mean percipitation for your chosen years {chosen_list[1]}:")
            print(f"{chosen_list[2]} mm\n")

        elif program_choise == "F" or program_choise == "f":
            print("The gererator will end when saving to file.")
            print("Do you want to choose more years?")
            sure = input("Yes (Y) or No (N): ")
            if sure == "Y" or sure == "y":
                #Continues the loop if user wants to input more years
                print("Please press P to choose another period. \n")
                continue
            elif sure == "N" or sure == "n":
                print("What do you want to call your file?")
                name = input("")
                #Saving the file with the save_to_file function with the inputted name
                ut.save_to_file_function(collected_information, name)
                print(f"Your information has been stored the file named {name}.csv\n")
                program_choise = "Q"
            else:
                print("You must have written the wrong letter.")
                print("Please write Y for yes, or N for no \n")
       
        elif program_choise == "G" or program_choise == "g":
            print("This stops the generator and returns a graph:")
            #Choose the years user want diplayed in graph
            chosen_list = ut.choose_year_function(pasvik_summer)
            print("What do you want to call your graph-file?")
            name1 = input("Name: ")
            #Creating graph with graph_generator
            ut.graph_generator(chosen_list[0], name1)
            print("\n")
            print("Thank you for using the P-PIG!")
            program_choise = "Q"
            return
        elif program_choise != "Q":
            print(f"You seem to have entered an unvalid input {program_choise}\n")
        
    print("Thank you for using the P-PIG!")
    print("Outro-screen will start in 5 seconds...")
    time.sleep(5)
    #Running end-message using asciimetrics packadge
    Screen.wrapper(ut.finished_screen)

    return


# If runing main directly, run the main-function:
if __name__ == "__main__":
   main()