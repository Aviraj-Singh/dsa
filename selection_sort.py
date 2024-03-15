# Selection sort
arr = [10,9,22,1,56,5]
n = len(arr)
for i in range(0, n - 1):
    min_index = i
    for j in range(i + 1, n):  # Start from i+1 since arr[i] is already assumed to be minimum
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)

# The time complexity of selection sort is O(n^2) in the worst case, where n is the number of elements in the array.
# The space complexity of selection sort is O(1) because it only requires a constant amount of extra space for temporary variables regardless of the size of the input array.
