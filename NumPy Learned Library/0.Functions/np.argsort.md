np.argsort() returns the indices that would sort the array. This means it does not directly return the sorted values, but rather the indices that, when used to index the original array, would sort the array.

Key Characteristics:

 

Returns indices of the elements that would sort the array.
Useful when you want to rearrange the original array based on the sorted order of indices.
The original array remains unchanged.
 

 

 
```python
arr = np.array([3, 1, 2, 5, 4])

 

indices = np.argsort(arr)

 

print("Original array:", arr)

print("Indices of sorted array:", indices)

print("Sorted array using indices:", arr[indices])

"""

Original array: [3 1 2 5 4]

Indices of sorted array: [1 2 0 4 3]

Sorted array using indices: [1 2 3 4 5]

"""

 ```

 

np.argsort() returns an array of indices [1, 2, 0, 4, 3] because those are the positions in the original array that would result in a sorted array.
 

Using those indices to index the original array (arr[indices]) gives you the sorted array [1, 2, 3, 4, 5].
 

 

 

 

 

 
```python
import numpy as np

# Create a 2D array (4 rows and 3 columns)

arr = np.array([[3, 1, 4],
                [6, 2, 5],
                [9, 8, 7],
                [12, 10, 11]])

# Use np.argsort to get the indices that would sort each row (axis=1)

 

 

sorted_indices = np.argsort(arr, axis=1)

 

 

print(arr)

"""
Original array:
[[ 3  1  4]
 [ 6  2  5]
 [ 9  8  7]
 [12 10 11]]
 """

 

 

print(sorted_indices)

"""
[[1 0 2]
 [1 2 0]
 [2 1 0]
 [1 2 0]]
 """

 

 

# Use the sorted indices to rearrange the original array (to see the sorted rows)

sorted_arr = np.take_along_axis(arr, sorted_indices, axis=1)

 

 

 

print(sorted_arr)

"""
[[1 3 4]
 [2 5 6]
 [7 8 9]
 [10 11 12]]
 """

 
```
 

 

axis=1 sorts rows individually.
The result from np.argsort() is an array of indices, which you can use to reorder the elements of each row.
 
<br><br>
 
Ex-1
```python
import numpy as np
def sortTheStudents(score: list[list[int]], k: int) -> list[list[int]]:
    score = np.array(score)
    score = score[score[:, k].argsort()[::-1]]
    return score

print(sortTheStudents(score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2))
```
 

 
<br><br><br>
 

Here's a new example with a different matrix, and we'll still use [:, 0] to sort the array based on the first column.

 
```python
import numpy as np

# Create a new 2D array (4 rows and 3 columns)

arr = np.array([[15, 7, 2],
                [10, 5, 1],
                [30, 8, 4],
                [20, 6, 3]])

# Select the first column (index 0) and apply np.argsort to get the indices

 

sorted_indices = np.argsort(arr[:, 0])

 

print(arr)
"""
[[15  7  2]
 [10  5  1]
 [30  8  4]
 [20  6  3]]
"""

 

 

print(sorted_indices)

#[1 0 3 2]


# Use the sorted indices to reorder the entire array based on the sorted first column

sorted_arr = arr[sorted_indices]


print(sorted_arr)
"""
[[10  5  1]
 [15  7  2]
 [20  6  3]
 [30  8  4]]
 """

 ```