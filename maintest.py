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

    def test_find_highest(self):
        result = main.find_highest(data.allData)
        self.assertAlmostEqual(result, )

    def test_find_lowest(self):
        result = main.find_highest(data.allData)
        self.assertAlmostEqual(result, )
if __name__ == '__main__':
    unittest.main()