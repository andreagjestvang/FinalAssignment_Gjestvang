# P-PIG: the Pasvik Precipitation Information Generator

Welcome to the interactive rain-information for Pasvik weather station

Or the rather dashing name: *P-PIG*!

## Motivation for analysis
As I have no specific master thesis yet, I decided to look into relevant weather-data for Pasvik, 
where I'm most likley writing my thesis on lichen growth. We will look into lichen growth during the last 15, 10, 5 and 0 years, and therefore require to look into the amount of rain that has fallen during different periods of time. That is why I chose to focus on the ability to choose and store a user-decided period of years, and creating a script depending on user input.

As lichen-growth is most dependent on the precipitation during summer, this generator focuses on summer-measurments from the months april-september.

Data has been downloaded from Norsk KlimeserviceSenter, Metrologiske institutt: https://seklima.met.no/observations/

## Running the generator
The Main.py file is the executer of the generator. Keeping the four files (Main.py, Utilities.py, Pasvik_rain.csv and README.md) in the same folder, run the Main.py file in terminal or from preferred IDE.

### Dependencies
- altair
- asciimatics
- pandas
- pathlib
- time

## Short Pipeline description
The pipeline is a while-loop that will run and store selected information for the user. 
For each loop, the user will be asked to choose one of the following selections:
- Choose to examine the mean of a specific period (P)
- Choose to save collected info to file (F)
- Create a graph (G)
- Quit Generator (Q)

(P): The generator will ask user for a period of years in the format YYYY seperated by ",". The selected rows of years will be shown from the dataset, and mean rainfall over the chosen years will be given.

(F): Saving to file, will create a file with all periods choosen by user during the run-time of the generator. User will be given the choise to name the file. The previos information will be deleted, and the generator will continue.

(G): Creating a graph, will ask user to select a period of years and then it will create a .png file with a bar-chart of rainfall from 2009-2023. The selected years will be highlighted in a different color than the rest of the years. The generator will continue.

(Q): An option to quit the generator. 

Following functions has been created that is used in the pipeline: 
- MET_data_loader(MET_data_csv): Loading MET .csv file with rainfall data
- is_valid_function(): Getting and validatoing user input
- choose_year_function(dataset): Modifying dataset according to chosen years
- graph_generator(chosen_dataset,name): Generate .png graph-file
- save_to_file_function(information_dict, name_csv): Generate .csv information-file
- finished_screen(screen): Creating an ending message

For further documentation of the functions, go to Utilities.py.


...
