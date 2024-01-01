# Using the array module
from array import array
my_array = array('i', [1, 2, 3, 4, 5])  # 'i' denotes integer type

# Accessing elements using index
first_element = my_array[0]
second_element = my_array[1]

# Accessing elements using negative index
last_element = my_array[-1]

# Slicing array
subset = my_array[1:4]  # Returns elements from index 1 to 3

# Modifying an element
my_array[2] = 10

# Modifying multiple elements using slicing
my_array[1:4] = [20, 30, 40]

# Length of the array
length = len(my_array)

# Concatenating arrays
new_array = my_array + array('i', [6, 7, 8])

# Repetition
repeated_array = my_array * 2

# Length of the array
length = len(my_array)

# Concatenating arrays
new_array = my_array + array('i', [6, 7, 8])

# Repetition
repeated_array = my_array * 2
