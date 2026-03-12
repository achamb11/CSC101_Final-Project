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
    #returns the % of the total of multi households with access
    total = 0
    totalPpl = 0
    if type(places) == list:
        for place in places:
            total += (place.multi_household*place.multi_access)
            totalPpl += place.multi_household
        return total/totalPpl
    elif type(places) == data.State:
        total += (places.multi_household * places.multi_access)
        totalPpl += places.multi_household
        return total/totalPpl
    else:
        return total

def single_total(places) -> float: #Roxanne Chambers
    # returns the % of the total of single households with access
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

def calculate_average(places) -> float: #Vidushi Goyal
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

#identifies the 3 highest states with access
def find_highest2(places) -> list:  #Vidushi Goyal
    sorted_list = [places[0],places[1],places[2]]
    for i in range (3,len(places)):
        if calculate_average(places[i])>calculate_average(sorted_list[0]):
            sorted_list[0] = places[i]
        elif calculate_average(places[i])>calculate_average(sorted_list[1]):
            sorted_list[1] = places[i]
        elif calculate_average(places[i])>calculate_average(sorted_list[2]):
            sorted_list[2] = places[i]
    return sorted_list

#identifies the 3 lowest states with access
def find_lowest2(places) -> list:  #Vidushi Goyal
    sorted_list = [places[0],places[1],places[2]]
    for i in range (3,len(places)):
        if calculate_average(places[i])<calculate_average(sorted_list[0]):
            sorted_list[0] = places[i]
        elif calculate_average(places[i])<calculate_average(sorted_list[1]):
            sorted_list[1] = places[i]
        elif calculate_average(places[i])<calculate_average(sorted_list[2]):
            sorted_list[2] = places[i]
    return sorted_list

#identifies the state type has "less" or "more" access than average
def check_state(places: list[data.State]):  #Vidushi Goyal
    overall_avg = calculate_average(places)
    result_names = {}
    for place in places:
        place_avg = calculate_average(place)
        if place_avg > overall_avg:
            result_names[place.state_name] = True #to account for that it can be multiple states
        elif place_avg < overall_avg:
            result_names[place.state_name]= False #to account for that it can be multiple states
    return result_names