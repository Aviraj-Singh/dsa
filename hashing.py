# Hashing
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
