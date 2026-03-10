# This is our senior project :)
import data


### THE FUNCTIONS ###

def calculate_total(places) -> float: #Roxanne Chambers
    #Returns  to total of people with access from a dataset
    total = 0
    if type(places) == list:
        for place in places:
            total += (place.single_household*place.single_access)/100
            total += (place.multi_household*place.multi_access)/100
        return total
    elif type(places) == data.State:
        total += (places.single_household * places.single_access) / 100
        total += (places.multi_household * places.multi_access) / 100
        return total
    else:
        return total

def multi_total(places) -> float: #Roxanne Chambers
    total = 0
    totalPpl = 0
    if type(places) == list:
        for place in places:
            total += (place.multi_household*place.multi_access)
            totalPpl += place.multi_household
        return total/totalPpl
    elif type(places) == data.State:
        total += (places.multi_household * places.multi_access)
        totalPpl += place.multi_household
        return total/totalPpl
    else:
        return total

def single_total(places) -> float: #Roxanne Chambers
    total = 0
    totalPpl = 0
    if type(places) == list:
        for place in places:
            total += (place.single_household*place.single_access)
            totalPpl += place.single_household
        return total/totalPpl
    elif type(places) == data.State:
        total += (places.single_household * places.single_access)
        totalPpl += places.single_household
        return total/totalPpl
    else:
        return total

# EXAMPLES FOR calculate_total
#print("Total in",data.allData[2].state_name,calculate_total(data.allData[2]))
#print("Total for all:"calculate_total(data.allData))

def calculate_average(places) -> float:
    #Returns average % access from all states
    totalPpl = 0
    totaAccess = 0
    perc = 0
    if type(places) == list:
        for place in places:
            totalPpl += place.single_household + place.multi_household
            totaAccess += calculate_total(place)
        perc = (totaAccess / totalPpl) * 100
        return perc
    elif type(places) == data.State:
        totalPpl += places.single_household + places.multi_household
        totaAccess += calculate_total(places)
        perc = (totaAccess / totalPpl) * 100
        return perc
    else:
        return perc

# EXAMPLES FOR calculate_average
#print("Average % in",data.allData[2].state_name,calculate_average(data.allData[2]))
# print("Average % for all states:",calculate_average(data.allData))

#identifies the 3 highest  states with access
def find_highest(places) -> list:  #Vidushi Goyal
    sorted_list = []
    for i in range (1,len(sorted_list)):
        key_state = sorted_list[i]
        key_val = calculate_average(key_state)
        j = i - 1
        while j>= 0 and calculate_average(sorted_list[j]) > key_val:
            sorted_list[j + 1] = key_state

    return [sorted_list[-1],sorted_list[-2],sorted_list[-3]]
#identifies the 3 lowest states with access
def find_lowest(places) -> list:  #Vidushi Goyal
    sorted_list = []
    for i in range (1,len(sorted_list)):
        key_state = sorted_list[i]
        key_val = calculate_average(key_state)

        j = i - 1
        while j >= 0 and calculate_average(sorted_list[j]) < key_val:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j+1] = key_state
    return [sorted_list[0],sorted_list[1],sorted_list[2]]

#identifies the state type has "less" or "more" access than average
def check_state(places: list[data.State]) -> str:  #Vidushi Goyal
    overall_avg = calculate_average(places)
    result_names = {}
    for place in places:
        place_avg = calculate_average(place)
        if place_avg > overall_avg:
            result_names[place.state_name] = True #to account for that it can be multiple states
        elif place_avg < overall_avg:
            result_names[place.state_name]= False #to account for that it can be multiple states
    return result_names

#print(check_state(data.allData))
