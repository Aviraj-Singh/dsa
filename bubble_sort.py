# Bubble sort
arr = [10, 9, 22, 1, 56, 5]
n = len(arr)
for i in range(n - 1, 0, -1):
    for j in range(0, i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)

# The time complexity of bubble sort is O(n^2) in the worst case, where n is the number of elements in the array.
# The space complexity of bubble sort is O(1) because it only requires a constant amount of extra space for temporary variables regardless of the size of the input array.
