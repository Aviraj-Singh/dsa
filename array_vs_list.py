# creating a list containing elements
# belonging to different data types
sample_list = [1, "Yash", ['a', 'e']]
print(type(sample_list))
print(sample_list)

# importing "array" for array creations
import array as arr
  
# creating an array with integer type
a = arr.array('i', [1, 2, 3])
print(type(a))
for i in a:
    print(i, end=" ")

# For understanding the difference between List and Python, please refer this article - https://www.geeksforgeeks.org/difference-between-list-and-array-in-python/
# I too read the above article and watched this video (https://www.youtube.com/watch?v=b4Jcj-mKtPo&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=2&ab_channel=MySirG.com)
