# Insertion sort
arr = [10,9,22,1,56,5]
n = len(arr)
for i in range(0, n):
    j=i
    while j>0 and arr[j-1]>arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j-=1
    
print(arr)

# The time complexity of insertion sort is O(n^2) in the worst case, where n is the number of elements in the array.
# The space complexity of insertion sort is O(1) because it only requires a constant amount of extra space for temporary variables regardless of the size of the input array.
# Note: Insertion sort tends to perform well on small arrays or nearly sorted arrays, making it a good choice for such cases.
