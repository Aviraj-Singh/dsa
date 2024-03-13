# Using Dictionary (Map)
# For array of numbers

arr = [1, 2, 3, 1, 1, 4] 
def find_count_of_numbers(arr):
    hash = {}
    for num in arr:
        if num not in hash:
            hash[num]=1
        else:
            hash[num]+=1
    return hash

print(find_count_of_numbers(arr))

# For string

def find_count_of_characters(string):
    count_dict = {}
    for ch in string:
        if ch not in count_dict:
            count_dict[ch] = 1
        else:
            count_dict[ch] += 1

    return count_dict

string = 'abcbcbcad'
print(find_count_of_characters(string))

'''
For array of numbers:

Time Complexity: O(n)
Space Complexity: O(n)
where n is the number of elements in the input list

For string of characters:

Time Complexity: O(m)
Space Complexity: O(m)
where m is the length of the input string
'''
