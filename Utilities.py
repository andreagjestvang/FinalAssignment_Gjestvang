# The utilities file with all functions in this analysis
import pandas as pd
import altair as alt
from pathlib import Path

from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene

def MET_data_loader(MET_data_csv):
    """Taking a csv file from the Norwegian Metrological Institue and returning a dataframe containing only
    summer precipitation measures.

    Args:
        MET_data_csv (csv file): name of a csv-file to be loaded

    Returns:
        dataframe: a dataframe including only summer-temperatures of the csv file
    """
    pasvik_rain = pd.read_csv(Path(MET_data_csv), sep=";", decimal=",")

    #Splitting into month and year
    pasvik_rain[["Måned", "År"]] = pasvik_rain["Tid(norsk normaltid)"].str.split(".", expand=True)

    #Creating a new dataset with only summer temperatures
    pasvik_summer = pasvik_rain[pasvik_rain["Måned"] == "apr"]

    #Changing type for Nedbør and År
    convert_dict = {'Nedbor i forhold til normalen 1991-2020 (vinter- eller sommerhalvaaret)': float,
                    'År': int
                    }
    pasvik_summer = pasvik_summer.astype(convert_dict)

    #Adding 2000 making År into year-values
    pasvik_summer["År"] += 2000

    #Renaming the column-names of the dataset Pasvik_summer
    pasvik_summer.rename(columns={"Navn": "Name", "Stasjon": "Station", 
                              "Tid(norsk normaltid)": "Date", 
                              "Nedbor i forhold til normalen 1991-2020 (vinter- eller sommerhalvaaret)":"Prec_norm",
                              "Nedbor (vinter- eller sommerhalvaaret)":"Prec_mm",
                              "Måned":"Month", "År":"Year"}, inplace=True)
    
    #Making the Date-column into a datetime-type
    pasvik_summer["Date"] = pd.to_datetime(list(pasvik_summer["Year"]), format="%Y")

    return pasvik_summer



def is_valid_function():
    """Takining input from user. 
    Recusivly asking for new input until the input is in valid format.

    Returns:
        list: list of integers, years on format YYYY.
    """
    print("An input:")
    input_years = input("")
    chosen_years = input_years.split(",")

    for i in range(len(chosen_years)):
        try:
            chosen_years[i] = int(chosen_years[i])
        except Exception as error:
            print(error)
            print(f"Your input {chosen_years[i]} is not a year in format YYYY.")
            print("Please input your years in the correct format.\n")
            chosen_years = is_valid_function()
            break

    if 2013 in chosen_years:
        print("The year 2013 is not available in the data.")
        print("Please chose another period without 2013.\n")
        chosen_years = is_valid_function()

    for i in chosen_years:
        if i < 2009 or i > 2023:
            print(f"The year {i} is outside of available period 2009-2023.")
            print("Please chose another period within scope.\n")
            chosen_years = is_valid_function()
    
    return chosen_years


def choose_year_function(dataset):
    """Running the is_valid function, marking the chosen years as choesn=TRUE in the dataset,
    calculating mean.

    Args:
        dataset (dataframe): a dataframe with the percipitation data

    Returns:
        list : 
            dataframe: the modified precipitation dataframe
            list: the chosen years user want to examine
            mean_prec: the mean precipitation over the chosen years.
    """
    
    #Making a new column based on chosen year-values and calculation mean precipitation
    print("Write a list of years you want to examine, seperated by ','")
    print("Available period: 2009-2023")
    print("INFO: The year '2013' is not available in the data")

    #Checking if the chosen years are valid input and storing them in list chosen_years
    chosen_years = is_valid_function()
    
    total_prec = float(0)
    dataset["Chosen"] = False

    #Setting the column "chosen" TRUE for chosen years
    for i in chosen_years:
        dataset.loc[dataset["Year"] == i, "Chosen"] = True
        total_prec += dataset.loc[dataset["Year"] == i, "Prec_mm"].values[0]
    #Calculating mean
    mean_prec = round(total_prec / len(chosen_years),2)

    return dataset, chosen_years, mean_prec



def graph_generator(chosen_dataset,name): 
    """Generating a graph and saving it as png

    Args:
        chosen_dataset (dataframe): dataframe of precipitation to be graphed
        name (string): a name to call the graph
    """
    chosen_chart = alt.Chart(chosen_dataset).mark_bar().encode(
    x= alt.X("Date").title("Year"),
    y=alt.Y("Prec_norm").title("Precipitation related to normality (1990-2020)"),
    color="Chosen",
    ) + alt.Chart().mark_rule(strokeDash=[12, 6], size=1).encode(y=alt.datum(100))
    chosen_chart.save(f"{name}.png")
    return


def save_to_file_function(information_dict, name_csv):
    """A function that will save the given dictionary as a csv-file

    Args:
        information_dict (dictionary): a dictionary with chosen periods from user
        name_csv (string): a name to call the file
    """
    df = pd.DataFrame.from_dict(information_dict, orient="index", columns= ["Prec_mm"])
    df.to_csv(f"{name_csv}.csv")
    return


def finished_screen(screen):
    """A dashing ending screen to say goodbye to user, using the asciimatics packadge

    Args:
        screen (asciimatics.screen): the screen the ending graphics will be displayed on
    """
    effects = [
        Cycle(
            screen,
            FigletText("P-PIG", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("THANKS YOU!", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])


#When running utilities.py, the is_valid_function() will be tested
if __name__ == "__main__":
    print("this is what the function returns:", is_valid_function())
    print("Successfully run Utilities.py")