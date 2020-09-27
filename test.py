""" 
Name:         Roger Silva Santos Aguiar
Function:     Test the Selection Sort methods
Initial date: September 27, 2020
Last update:  September 27, 2020 
"""

import unittest
from selection_sort_algorithm import SelectionSort

class TestSelectionSort(unittest.TestCase):
    # It creates an object of the class that will be tested
    test_functions = SelectionSort()

    def test_sort_array(self):
        # It creates an initial list to test the function
        unsorted_array = [64, 25, 12, 22, 11]
        # It calls the function and provides the previous array to the function
        sorted_array = self.test_functions.sort_array(unsorted_array)  
        # It checks if the arrays are similar      
        self.assertEqual(sorted_array, [11, 12, 22, 25, 64])    
    
    
if __name__ == '__main__':
    unittest.main()