#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
#and return its sum.
#Example:
#Input: [-2,1,-3,4,-1,2,1,-5,4],
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.


#The first solution that comes to mind, as always, is the brute force solution.

def brute_force_max_subarray(array):
    maximum = 0
    if len(array)==0:
        return None
    for i in range(len(array)):
        cum_sum = 0
        for j in range(i,len(array)):
            cum_sum += array[j]
            maximum = max(maximum, cum_sum)
    return maximum

array = [-2,1,-3,4,-1,2,1,-5,4]
print(brute_force_max_subarray(array))

#Since we are looping through two nested for loops the time complexity is O(n^2)
#There's a much faster way to solve this though, and that is by using the Kadane's algorithm.

def kadane(array):
    maximum = maxarray = array[0]
    for i in range(1,len(array)):
        maxarray = max(array[i], maxarray+array[i])
        maximum = max(maxarray, maximum)
    return maximum

print(kadane(array))

# Since this requires only one for loop, the time complexity is an efficiently O(n)!
