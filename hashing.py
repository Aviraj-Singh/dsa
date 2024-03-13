# Number Hashing
arr = [1, 2, 3, 3, 3, 2, 0]

def findCount(n, arr):
    max_value = max(arr)  # Find the maximum value in arr
    arr1 = [0] * (max_value + 1)  # Initialize arr1 with zeros
    for i in range(len(arr)):
        if arr[i] == n:
            arr1[arr[i]] += 1
    return arr1

print(findCount(2, arr))

# Overall time complexity of the provided code is O(n + m) and space complexity is O(m)
# where, m is the maximum value in arr and n is the length of the input list arr.

# Charater Hashing
str = 'abcbcbcad'
def findAl(char, str):
    arr_hash = [0]*26 # assuing characcters will be only small letters, if not use 256
    for i in range(len(str)):
        arr_hash[ord(str[i])-ord('a')]+=1 #ord is used to get ascii value of the character
    return arr_hash[ord(char)-ord('a')]

print(findAl('d', str))

# Overall time complexity of the provided code is O(n) and space complexity is O(1)
# where, n is the length of the input string.
# The code uses an array arr_hash of size 26 to store the frequency of each lowercase alphabet character. Hence, O(1) space complexity
