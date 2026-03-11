import data
import unittest
import main
allData = data.allData
#TEST FILE

class TestCases(unittest.TestCase): #Vidushi Goyal #not sure why tests are not working will still make all tests

    def test_calculate_total1(self):
        result = main.calculate_total(data.allData[0]) #testing Albama
        self.assertAlmostEqual(result, 917420.25)

    def test_calculate_total2(self): #testing Alaska
        result = main.calculate_total(data.allData[1])
        self.assertAlmostEqual(result, 197998.02)

    def test_calculate_total3 (self): #testing ALL
        result = main.calculate_total(data.allData)
        self.assertAlmostEqual(result, 88623239.38)

    def test_calculate_average1(self):
        result = main.calculate_average(data.allData[2])
        self.assertAlmostEqual(result, 68.39,2)

    def test_calculate_average2(self):
        result = main.calculate_average(data.allData[4])
        self.assertAlmostEqual(result, 94.76,2)

    def test_calculate_average3(self):
        result = main.calculate_average(data.allData)
        self.assertAlmostEqual(result, 72.61,2)

    def test_multi_total(self): #Roxanne Chambers
        result = main.multi_total(data.allData)
        self.assertAlmostEqual(result, 36.398061505161344)

    def test_single_total(self): #Roxanne Chambers
        result = main.single_total(data.allData)
        self.assertAlmostEqual(result, 84.71105956036557)

    def test_find_highest2(self):
        result = main.find_highest2(data.allData)
        self.assertAlmostEqual([result[0].state_name,result[1].state_name,result[2].state_name], ["Delaware","Maryland","Vermont"])

    def test_find_lowest2(self):
        result = main.find_lowest2(data.allData)
        self.assertAlmostEqual([result[0].state_name,result[1].state_name,result[2].state_name], ["North Dakota","Montana","Nebraska"])

    def test_check_state(self):
        result = main.check_state(data.allData)
        self.assertTrue(result,{'Alabama': False, 'Alaska': True, 'Arizona': False, 'Arkansas': False, 'California': True, 'Colorado': False, 'Connecticut': True, 'Delaware': True, 'Florida': False, 'Georgia': False, 'Hawaii': False, 'Idaho': False, 'Illinois': True, 'Indiana': False, 'Iowa': False, 'Kansas': False, 'Kentucky': False, 'Louisiana': False, 'Maine': True, 'Maryland': True, 'Massachusetts': True, 'Michigan': False, 'Minnesota': False, 'Mississippi': False, 'Missouri': False, 'Montana': False, 'Nebraska': False, 'Nevada': False, 'New Hampshire': True, 'New Jersey': True, 'New Mexico': True, 'New York': True, 'North Carolina': True, 'North Dakota': False, 'Ohio': True, 'Oklahoma': False, 'Oregon': True, 'Pennsylvania': True, 'Rhode Island': True, 'South Carolina': False, 'South Dakota': False, 'Tennessee': False, 'Texas': False, 'Utah': False, 'Vermont': True, 'Virginia': False, 'Washington': True, 'West Virginia': False, 'Wisconsin': True, 'Wyoming': False}
)
if __name__ == '__main__':
    unittest.main()