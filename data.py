
# Data is taken from: The Recycling Partnership: "State of Residential Recycling 2024"

class State:

    def __init__(self, state_name, single_household, multi_household, single_access, multi_access): #Roxanne Chambers
        self.state_name = state_name
        self.single_household = single_household
        self.multi_household = multi_household
        self.single_access = single_access  # % single-family with access
        self.multi_access = multi_access  # % multi-family with access

    def __eq__(self,other) -> bool: #Roxanne Chambers
        if (self is other or
            type(self) == type(other) and
            self.state_name == other.state_name and
            self.single_household == other.single_household and
            self.multi_household == other.multi_household):
            return True
        else:
            return False

    def __repr__(self): #Roxanne Chambers
        return ("{} \n"
                "Num of single households: {} \n"
                "Num of multi households: {} \n"
                "% of single with access: {} \n"
                "% of multi with access: {}\n").format(self.state_name,self.single_household,self.multi_household,self.single_access,self.multi_access)

    # def __str__(self):
    #     return ("State:", self.state_name,
    #             "Num of single households:", self.single_household,
    #             "Num of multi households", self.multi_household,
    #             "% of single with access", self.single_access,
    #             "% of multi with access", self.multi_access)


allData = [
    State("Alabama", 1428595, 459773, 61, 10),
    State("Alaska", 210501, 47484, 90, 18),
    State("Arizona", 1969978, 673354, 88, 11),
    State("Arkansas", 920325, 250086, 79, 14),
    State("California", 9435863, 3666618, 97, 89),
    State("Colorado", 1587838, 549388, 57, 12),
    State("Connecticut", 1120161, 265144, 93, 82),
    State("Delaware", 286653, 84285, 99, 89),
    State("Florida", 5303296, 2627676, 90, 16),
    State("Georgia", 2870892, 959056, 76, 19),
    State("Hawaii", 319884, 148043, 82, 25),
    State("Idaho", 537006, 112216, 76, 10),
    State("Illinois", 3698161, 1185519, 85, 41),
    State("Indiana", 2109149, 493389, 79, 11),
    State("Iowa", 1031386, 242373, 75, 19),
    State("Kansas", 940675, 201147, 69, 17),
    State("Kentucky", 1350441, 397394, 74, 8),
    State("Louisiana", 1343158, 408699, 54, 6),
    State("Maine", 462246, 107197, 94, 8),
    State("Maryland", 1667247, 563198, 98, 88),
    State("Massachusetts", 2036146, 610593, 93, 46),
    State("Michigan", 3210628, 769355, 82, 11),
    State("Minnesota", 1698474, 509287, 81, 33),
    State("Mississippi", 854876, 261644, 47, 6),
    State("Missouri", 1982224, 457762, 68, 6),
    State("Montana", 346876, 89098, 51, 6),
    State("Nebraska", 605568, 160960, 52, 11),
    State("Nevada", 820194, 309771, 80, 27),
    State("New Hampshire", 415928, 123109, 95, 6),
    State("New Jersey", 2547499, 724175, 94, 20),
    State("New Mexico", 595142, 197534, 95, 32),
    State("New York", 4708498, 2708254, 91, 87),
    State("North Carolina", 2986954, 1044371, 95, 15),
    State("North Dakota", 207666, 113141, 49, 6),
    State("Ohio", 3814578, 902303, 92, 8),
    State("Oklahoma", 1191617, 301826, 57, 11),
    State("Oregon", 1222867, 419584, 90, 86),
    State("Pennsylvania", 4265065, 840960, 95, 15),
    State("Rhode Island", 339287, 75405, 97, 6),
    State("South Carolina", 1422674, 538656, 97, 6),
    State("South Dakota", 258856, 88941, 52, 29),
    State("Tennessee", 2030621, 608631, 80, 6),
    State("Texas", 7126834, 2778713, 81, 20),
    State("Utah", 815697, 187546, 81, 20),
    State("Vermont", 212511, 50291, 93, 88),
    State("Virginia", 2451830, 734663, 80, 16),
    State("Washington", 2081215, 824401, 91, 33),
    State("West Virginia", 579237, 154914, 84, 6),
    State("Wisconsin", 1869571, 508107, 88, 72),
    State("Wyoming", 184050, 49139, 70, 6),
] #Roxanne Chambers




