def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2  # Finding the middle index

        # Sorting the first half
        merge_sort(arr, l, mid)
        # Sorting the second half
        merge_sort(arr, mid + 1, r)

        # Merging the sorted halves
        merge(arr, l, mid, r)

def merge(arr, l, mid, r):
    n1 = mid - l + 1  # Length of left subarray
    n2 = r - mid      # Length of right subarray

    # Creating temporary arrays
    left_half = arr[l:l + n1]
    right_half = arr[mid + 1:mid + 1 + n2]

    # Merging the temporary arrays back into arr[l:r+1]
    i = j = 0  # Initial indices of left_half and right_half
    k = l      # Initial index of merged subarray
    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Copying the remaining elements of left_half, if any
    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Copying the remaining elements of right_half, if any
    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1

# Example usage:
arr = [5, 2, 7, 3, 1, 6, 4]
merge_sort(arr, 1, 5)  # Sorting elements from index 1 to 5
print(arr)  # Output: [5, 1, 2, 3, 7, 6, 4]

'''
Merge sort has a time complexity of O(n log n) in all cases, where n is the number of elements in the array. 
This is because the array is divided into halves recursively until each sub-array contains only one element (log n operations), 
and then merges these sub-arrays back together (n operations). 
Hence, the overall time complexity is O(n log n).

The space complexity of merge sort is O(n) because it requires additional memory space to store temporary arrays during the merge process. 
However, since merge sort uses a divide-and-conquer approach and creates temporary arrays during recursion, 
the space complexity can be higher than other sorting algorithms like insertion sort or bubble sort.
'''
