



"""
2. Convert List to 1D Array

Write a NumPy program to convert a list
of numeric values into a one-dimensional NumPy array.
"""
import numpy as np

list1 = [1,2,3,4,5,6,7,8,9]

New_Array = np.array(list1)


print(New_Array)
#[1 2 3 4 5 6 7 8 9]


####################################################################


"""
3. Create 3x3 Matrix (2?10)

Write a NumPy program to create a 3x3 matrix 
with values ranging from 2 to 10.
"""

ThreeD = np.array(([1,2,3],[4,5,6],[7,8,9]))

print(ThreeD)
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

####################################################################

"""
4. Null Vector (10) & Update Sixth Value

Write a NumPy program to create a
 null vector of size 10 and update the sixth value to 11.
 
"""

big_array = np.zeros(shape=(10))

big_array[6] = 11

print(big_array)
#[ 0.  0.  0.  0.  0.  0. 11.  0.  0.  0.]


####################################################################

"""
5. Array from 12 to 38

Write a NumPy program to create an array 
with values ranging from 12 to 38.
"""


biggest_array = np.array(range(12,38))
print(biggest_array)
#[12 13 14 15 16 17 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31 32 33 34 35 36 37]



####################################################################

"""
6. Reverse Array

Write a NumPy program to reverse an array
 (the first element becomes the last).
"""


reverse_array = np.array(range(12,37)[::-1])

print(reverse_array)
#[36 35 34 33 32 31 30 29 28 27 26
# 25 24 23 22 21 20 19 18 17 16 15 14 13 12]


####################################################################


"""
7. Convert Array to Float Type

Write a NumPy program to convert an array to a floating type.
"""

float_array = np.array(range(1,5),float)

print(float_array)
#[1. 2. 3. 4.]


####################################################################

"""

8. 2D Array (Border 1, Inside 0)

Write a NumPy program to create a 
2D array with 1 on the border and 0 inside.
"""

two_array = np.ones((4,4))

two_array[2] = 0
two_array[1] = 0

print(two_array)

"""
[[1. 1. 1. 1.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [1. 1. 1. 1.]]
"""

####################################################################


"""
9. Add Border to Array (0s)

Write a NumPy program to add a border
 (filled with 0's) around an existing array.
"""

checkers = np.zeros((8,8))

checkers[::2,::2] = 1
checkers[::-2,::-2] = 1

print(checkers)
"""
[[1. 0. 1. 0. 1. 0. 1. 0.]
 [0. 1. 0. 1. 0. 1. 0. 1.]
 [1. 0. 1. 0. 1. 0. 1. 0.]
 [0. 1. 0. 1. 0. 1. 0. 1.]
 [1. 0. 1. 0. 1. 0. 1. 0.]
 [0. 1. 0. 1. 0. 1. 0. 1.]
 [1. 0. 1. 0. 1. 0. 1. 0.]
 [0. 1. 0. 1. 0. 1. 0. 1.]]
"""


####################################################################


"""
12. Append Values to Array

Write a NumPy program to append values to the end of an array.

Expected Output:

Original array:
[10, 20, 30]
"""

normal_array = np.array([12,20,30])

normal_array = np.append(normal_array,[40,50,60])

print(normal_array)
#[12 20 30 40 50 60]


####################################################################

"""
13. Create Empty and Full Array

Write a NumPy program to create an empty and full array.
"""

empty = np.zeros(10)
full = np.full([3,3],20)

print(empty)
print(full)
"""
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[[20 20 20]
 [20 20 20]
 [20 20 20]]
"""



####################################################################

"""
14. Celsius to Fahrenheit Conversion

Write a NumPy program to convert Centigrade 
degrees into Fahrenheit degrees. Centigrade 
values are stored in a NumPy array.

"""

def temp(array1):
    temps = np.array(array1)
    faran = np.round((5 * temps / 9 - 5 * 32 / 9), 2)
    return faran

print(temp([0, 12, 45.21, 34, 99.91]))
#[-17.78 -11.11   7.34   1.11  37.73]


####################################################################


"""
16. Array Elements Count & Memory Usage

Write a NumPy program to find the number 
of elements in an array. It also finds 
the length of one array element in bytes 
and the total bytes consumed by the elements.
"""


x = np.full((3,3),1)

print(x.itemsize)
#8

print(x.nbytes)
#72


y = np.array([1,2,3])

print(y.itemsize)
#8

print(y.nbytes)
#24


####################################################################

"""
17. 1D Array Element Check in Another Array

Write a NumPy program to test whether 
each element of a 1-D array is also present in a second array.

"""

array1 = np.array((0,10,20,40,60))
array2 = np.array((0, 40))


array = [True if x in array2 else False for x in array1]
print(array)
#[True, False, False, True, False]

print(np.in1d(array1,array2))
#[ True False False  True False]


####################################################################


"""
18. Common Values in Two Arrays

Write a NumPy program to find common values between two arrays.

"""

array1 = np.array([0,10,20,40,60])
array2 = np.array([10, 30, 40])

array = [x for x in array1 if x in array2]
print(array)
#[10, 40]


print(np.intersect1d(array1, array2))
#[10 40]



####################################################################


"""
19. Unique Elements of Array

Write a NumPy program to get the unique elements of an array.

"""


x = np.array(([10,10,20,20,30,30]))

print(np.unique(x))
#[10 20 30]


####################################################################

"""
20. Set Difference of Arrays

Write a NumPy program to find the set difference 
between two arrays. The set difference will return
 sorted, distinct values in array1 that are not in array2.
 
"""

x = np.array(([10,10,20,20,30,30]))
y = np.array(([10, 30, 40, 50, 70, 90]))

print(np.setdiff1d(x,y))
#[20]

print(np.setdiff1d(y,x))
#[40 50 70 90]


####################################################################

"""
21. Set Exclusive-Or of Arrays

Write a NumPy program to find the set exclusive-or 
of two arrays. Set exclusive-or will return sorted, 
distinct values in only one (not both) of the input arrays.
"""


x = np.array(([10,10,20,20,30,30]))
y = np.array(([10, 30, 40, 50, 70, 90]))


print(np.setxor1d(x,y))
#[20 40 50 70 90]


####################################################################


"""
22. Union of Two Arrays

Write a NumPy program to find the union of two
 arrays. Union will return a unique, sorted 
 array of values in each of the two input arrays.
 
"""

x = np.array(([10,10,20,20,30,30]))
y = np.array(([10, 30, 40, 50, 70, 90]))


print(np.union1d(x,y))
#[10 20 30 40 50 70 90]



####################################################################


"""
23. Test All Elements are True

Write a NumPy program to test whether 
all elements in an array evaluate to True.
"""

x = np.ones(10)

print(all(y for y in x if x is True))
#True


####################################################################


"""
24. Test Any Element is True

Write a NumPy program to test whether 
any array element along a given axis evaluates to True.

Note: 0 evaluates to False in NumPy.
"""

x = np.zeros(10)

print(all(y for y in x if x is True))
#True


####################################################################

"""
25. Repeat Array Entirely

Write a NumPy program to construct an array by repeating.
"""

x = np.array(([1, 2, 3, 4]))

print(np.repeat(x,2))
#[1 1 2 2 3 3 4 4]

print(np.tile(x,2))
#[1 2 3 4 1 2 3 4]


####################################################################

"""
26. Repeat Each Array Element

Write a NumPy program to repeat array elements.
"""

x = np.array(([1, 2, 3, 4]))

print(np.repeat(x,2))
#[1 1 2 2 3 3 4 4]

####################################################################

"""
27. Indices of Max/Min Along Axis

Write a NumPy program to find the 
indices of the maximum and minimum 
values along the given axis of an array.

"""


x = np.array(([1, 2, 3, 4]))

print(np.max(x))
#4

print(np.min(x))
#1

####################################################################

"""
29. Sort Array Along Axes

Write a NumPy program to sort along 
the first and last axes of an array.

Sample array: [[2,5],[4,4]]

"""

x = np.array(([[2,5],[4,4]]))
print(np.sort(x,0))
"""
[[2 4]
 [4 5]]
"""


print(np.sort(x,-1))
"""
[[2 4]
 [4 5]]
"""



####################################################################

"""
30. Sort Pairs by Names

Write a NumPy program to sort pairs of
 a first name and a last name and return
  their indices (first by last name, then by first name).

first_names = (Betsey, Shelley, Lanell, Genesis, Margery)
last_names = (Battle, Brien, Plotner, Stahl, Woolum)

"""



first_names = ("Betsey", "Shelley", "Lanell", "Genesis", "Margery")

x = np.array(first_names)
print(np.sort(x))

####################################################################


"""
31. Elements >10 & Their Indices

Write a NumPy program to get the values
 and indices of the elements that are bigger than 10 in a given array.
"""

x = np.array(([[10,20,30],[40,50,60]]))

print([z for y in x for z in y if z > 30])

#[40, 50, 60]



####################################################################

"""
34. Create Zeros and Ones Array

Write a NumPy program to create an array of ones and zeros.
"""


x = np.zeros(10)
x[::2] = 1
print(x)
#[1. 0. 1. 0. 1. 0. 1. 0. 1. 0.]


####################################################################


"""
35. Change Array Dimensions

Write a NumPy program to change an array's dimension.

"""

x = np.arange(1,10)

print(x)
#[1 2 3 4 5 6 7 8 9]

print(x.reshape(3,3))
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""



####################################################################

"""
36. Flatten Array

Write a NumPy program to create a contiguous flattened array.
"""

print(list(x.flat))
#[1, 2, 3, 4, 5, 6, 7, 8, 9]


####################################################################

x = x.reshape(3,3)
print(x.shape)
#(3,3)

