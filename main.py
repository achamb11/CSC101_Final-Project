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

# EXAMPLES FOR calculate_total
# print("Total in",data.allData[2].state_name,calculate_total(data.allData[2]))
# print("Total for all:",calculate_total(data.allData))
#

def calculate_average(places) -> float: #Roxanne Chambers
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
# print("Average % in",data.allData[2].state_name,calculate_average(data.allData[2]))
# print("Average % for all states:",calculate_average(data.allData))
#

