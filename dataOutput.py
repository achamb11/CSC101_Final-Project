import main
import data
from main import calculate_average


def print_output():
    output = ""
    for state in data.allData:
        output += str(state.state_name) + "\n"
        output += "Total Households with Access:"
        output += str(main.calculate_average(state)) + "\n"
        output += "Single Households with Access:"
        output += str(state.single_access) + "\n"
        output += "Multi Households with Access:"
        output += str(state.multi_access) + "\n"
        output += "Is in upper half of states with access:"
        output += str(main.check_state(data.allData)[state.state_name]) + "\n"
        output += "Is in top 3 States with access:"
        if state in main.find_highest(data.allData):
            output += "True" + "\n"
            output += "Is in lower 3 states with access: False"
        else:
            output += "False" + "\n"
            if state in main.find_lowest(data.allData):
                output += "Is in lower 3 states with access: True"
            else:
                output += "Is in lower 3 states with access: False"

print(print_output())




