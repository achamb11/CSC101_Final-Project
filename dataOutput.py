import main
import data
from main import calculate_average

#Roxanne Chambers
def print_output() -> str:
    output = ""
    for state in data.allData:
        output += str(state.state_name) + ": \n"
        output += "Total Households in state: " + str(state.single_household+state.multi_household) + "\n"
        output += "Total Households with Access: "
        output += str(round(main.calculate_average(state),2)) + " % \n"
        output += "Single Households with Access: "
        output += str(state.single_access) + " % \n"
        output += "Multi Households with Access: "
        output += str(state.multi_access) + " % \n"
        output += "Is in upper half of states with access: "
        output += str(main.check_state(data.allData)[state.state_name]) + "\n"
        output += "Is in top 3 States with access: "
        if state in main.find_highest2(data.allData):
             output += "True" + "\n"
             output += "Is in lower 3 states with access: False"
        else:
            output += "False" + "\n"
            if state in main.find_lowest2(data.allData):
                output += "Is in lower 3 states with access: True"
            else:
                output += "Is in lower 3 states with access: False"
        output += "\n" "\n"

    output += "Average Household with Access (all Households):"
    output += str(round(main.calculate_average(data.allData),1)) + " % \n"
    output += "Average Household with Access (multi Households):"
    output += str(round(main.multi_total(data.allData), 1)) + " % \n"
    output += "Average Households with Access (single-family Households): "
    output += str(round(main.single_total(data.allData), 1)) + " % \n"
    output += "Overall states with best Access: "
    output += str(main.find_highest2(data.allData)[0].state_name) + ", "
    output += str(main.find_highest2(data.allData)[1].state_name) + ", "
    output += str(main.find_highest2(data.allData)[2].state_name) + "\n"
    output += "Overall states with worst Access: "
    output += str(main.find_lowest2(data.allData)[0].state_name) + ", "
    output += str(main.find_lowest2(data.allData)[1].state_name) + ", "
    output += str(main.find_lowest2(data.allData)[2].state_name) + "\n"

    output += "\n" "\n"
    output += "Sustainability tip: \nMake sure your containers are clean before recycling them!"
    return output

print(print_output())




