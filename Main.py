
import Utilities as ut

def main(): 
    choise = ut.input_function()
    if choise == 1:
        print("Main is now finished")
    elif choise == 2:
        return ut.graph_generator()