# Pascal's Triangle: Given an integer numRows, return the first numRows of Pascal's triangle.
# Example:
# Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Bruteforce Approach
def generate_pascals_triangle_bruteforce(numRows):
    if numRows == 0:
        return []
    
    triangle = [[1]]
    
    for _ in range(1, numRows):
        previous_row = triangle[-1]
        new_row = [1]
        
        for i in range(1, len(previous_row)):
            new_row.append(previous_row[i - 1] + previous_row[i])
            
        new_row.append(1)
        triangle.append(new_row)
        
    return triangle

# Example 1
numRows1 = 5
print(generate_pascals_triangle_bruteforce(numRows1))
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

# Example 2
numRows2 = 1
print(generate_pascals_triangle_bruteforce(numRows2))

# Efficient Approach:

def generate_pascals_triangle_efficient(numRows):
    triangle = []
    
    for i in range(numRows):
        row = [1] * (i + 1)
        
        for j in range(1, i):
            row[j] = row[j - 1] * (i - j + 1) // j
            
        triangle.append(row)
        
    return triangle

# Example 1
numRows1 = 5
print(generate_pascals_triangle_efficient(numRows1))
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

# Example 2
numRows2 = 1
print(generate_pascals_triangle_efficient(numRows2))
# Output: [[1]]
