""" 
Name:         Roger Silva Santos Aguiar
Function:     This is the Selection Sort algorithm implementation
Initial date: September 27, 2020
Last update:  September 27, 2020 
"""

class SelectionSort:
    def sort_array(self, my_array):
        array_index = 0                

        while array_index < len(my_array):            
            array_index_comparison = array_index + 1
            key = my_array[array_index]
            key_position = array_index

            while array_index_comparison < len(my_array):
                if my_array[array_index_comparison] < key:
                    key = my_array[array_index_comparison]
                    key_position = array_index_comparison
                array_index_comparison += 1

            if key < my_array[array_index]:
                aux = my_array[array_index]
                my_array[array_index] = key
                my_array[key_position] = aux
            array_index += 1
        
        return my_array