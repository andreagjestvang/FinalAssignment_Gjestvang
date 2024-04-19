# The utilities file with all functions in this analysis
import pandas as pd
import altair as alt

def input_function():
    """
    When you call this function it takes an input and returns the value:
    """
    user_input = input("Write 'Hei' or 'Graph':")
    if user_input == "Hei":
        print("You are predictable")
        return 1
    elif user_input == "Graph":
        return 2

def graph_generator(): 
    data_anscombe =  pd.read_csv("Anscombe_data.csv")

    anscombe_chart = alt.Chart(data_anscombe, title="Anscombe's Dataset").mark_point().encode(
    x= alt.X("x").scale(zero=False),
    y="y",
    color="dataset",
    column="dataset"
    )
    return anscombe_chart

def new_print(): 
    print("This sucks")