



"""
2. Convert List to 1D Array

Write a NumPy program to convert a list
of numeric values into a one-dimensional NumPy array.
"""
import numpy as np
from astropy.units.quantity_helper.function_helpers import concatenate
from numpy.array_api import astype

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

"""
38. Reshape Array (Keep Data)

Write a NumPy program to create another shape from an array without changing its data.
"""

x = x.reshape(3,3)
print(x.shape)
#(3,3)





####################################################################


"""
39. Change Array Data Type

Write a NumPy program to change an array's data type.
"""

####################################################################

"""
40. 3x5 Array Filled with 2s

Write a NumPy program to create a new array of 3*5, filled with 2.
"""

print(np.full((3,5),2))
"""
[[2 2 2 2 2]
 [2 2 2 2 2]
 [2 2 2 2 2]]
"""


####################################################################


"""
42. 3D Array with Diagonal Ones

Write a NumPy program to create a 3-D array with ones on a diagonal and zeros elsewhere.
"""

print(np.identity(3))
"""
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
"""



####################################################################

"""
43. 2D Array with Custom Diagonal Values

Write a NumPy program to create a 2-D array whose diagonal equals [4, 5, 6, 8] and 0's elsewhere.

"""

print(np.diagflat([1,2,3,4,5]))
"""
[[1 0 0 0 0]
 [0 2 0 0 0]
 [0 0 3 0 0]
 [0 0 0 4 0]
 [0 0 0 0 5]]
"""



####################################################################

"""
45. 30 Evenly Spaced Values (2.5?6.5)

Write a NumPy program to create a 1-D array of 30 evenly spaced elements between 2.5 and 6.5, inclusive.
"""


print(np.linspace(2.5, 6.5, 10))

"""
[2.5        2.94444444 3.38888889 3.83333333 4.27777778 4.72222222
 5.16666667 5.61111111 6.05555556 6.5       ]
"""

####################################################################


"""
46. 20 Log-Spaced Values (2?5)

Write a NumPy program to create a 1-D array of 20 elements spaced evenly on a log scale between 2. and 5., exclusive.
"""


print(np.logspace(2.,5.,10))
"""
[   100.            215.443469      464.15888336   1000.
   2154.43469003   4641.58883361  10000.          21544.34690032
  46415.88833613 100000.        ]
"""


####################################################################

"""
48. Create 2D Array with Specific Values

Write a NumPy program to create an array like the one below.

"""

print(np.triu(np.arange(1, 10)))

"""
[[1 2 3 4 5 6 7 8 9]
 [0 2 3 4 5 6 7 8 9]
 [0 0 3 4 5 6 7 8 9]
 [0 0 0 4 5 6 7 8 9]
 [0 0 0 0 5 6 7 8 9]
 [0 0 0 0 0 6 7 8 9]
 [0 0 0 0 0 0 7 8 9]
 [0 0 0 0 0 0 0 8 9]
 [0 0 0 0 0 0 0 0 9]]
"""


print(np.triu(np.arange(1, 4),-1))
"""
[[1 2 3]
 [1 2 3]
 [0 2 3]]
"""


####################################################################


"""
49. Collapse 3D Array to 1D

Write a NumPy program to collapse a 3-D array into a one-dimensional array.
"""

x = np.identity(3)

print(np.ravel(x,order="F"))
#[1. 0. 0. 0. 1. 0. 0. 0. 1.]



####################################################################

"""
50. Find 4th Element of Array

Write a NumPy program to find the 4th element of a specified array.
"""

print(x[1][0])
#0.0


####################################################################

"""
51. Change Two Array Axes

Write a NumPy program to change two array axes.
"""

x = np.array([[1,2,3]])

print(x.reshape(3,1))
"""
[[1]
 [2]
 [3]]
"""


####################################################################

"""
52. Move Array Axes to Alternate Positions

Write a NumPy program to move array axes to alternate positions. Other axes remain in their original order.
"""


x = np.zeros((2, 3, 4))
print(x)
"""
[[[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]

 [[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]
"""

print(np.moveaxis(x, 0, -1).shape)
#(3, 4, 2)


print(np.moveaxis(x, -1, 0).shape)
#(4, 2, 3)

"""
Explanation:

x = np.zeros((2, 3, 4)): This line creates a 3D
    array x with the given shape (2, 3, 4), filled with zeros.

print(np.moveaxis(x, 0, -1).shape): The np.moveaxis() 
    function takes three arguments: the input array, 
    the source axis, and the destination axis. In this 
    case, it moves axis 0 (the first axis) to the last 
    position (-1). As a result, the shape of the new 
    array is (3, 4, 2).

print(np.moveaxis(x, -1, 0).shape): This line moves 
    the last axis (-1) to the first position (0). 
    As a result, the shape of the new array is (4, 2, 3).
"""

####################################################################

"""
53. Move Axis to Desired Position

Write a NumPy program to move the specified axis backwards, until it lies in a given position.
"""

x = np.zeros((2,3,4,5))

np.moveaxis(x,2,3)

np.moveaxis(x,1,2)

print(np.moveaxis(x,3,1).shape)
#2534

####################################################################

"""
54. Inputs as Arrays with 1+ Dimensions

Write a NumPy program to convert specified inputs into arrays with at least one dimension.
"""

print(np.array(12,dtype="f"))
#12.0

print(np.arange(6.0).reshape(2,3))
"""
[[0. 1. 2.]
 [3. 4. 5.]]
"""

print(np.atleast_1d(1, [3, 4]))
#[array([1]), array([3, 4])]



####################################################################

"""
55. Inputs as Arrays with 2D/3D Views

Write a NumPy program to view inputs as arrays with
    at least two dimensions, three dimensions.
"""


print(np.atleast_1d(10))
#[10]

print((np.arange(4).reshape(2,2)).astype("f"))
"""
[[0. 1.]
 [2. 3.]]
"""


####################################################################.

"""
56. Insert New Axis in 2D Array

Write a NumPy program to insert a new axis within a 2-D array.

2-D array of shape (3, 4).
"""

x = np.arange(12)

x = x.reshape(3,4)


y = np.expand_dims(x, axis=1).shape

print(y)
#(3, 1, 4)






####################################################################.

#https://www.machinelearningplus.com/python/101-numpy-exercises-python/


"""
3. How to create a boolean array?
"""

print(np.full((3,3),True))
"""
[[ True  True  True]
 [ True  True  True]
 [ True  True  True]]
"""



####################################################################.


"""
4. How to extract items that satisfy a given
    condition from 1D array?
"""

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

x = np.where(arr % 2 != 0)

print(x)
#(array([1, 3, 5, 7, 9]),)




#Input
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#Solution
arr[arr % 2 == 1]

#> array([1, 3, 5, 7, 9])


####################################################################.


"""
5. How to replace items that satisfy
 a condition with another value in numpy array?
"""
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

for i, nums in np.ndenumerate(arr):
    if nums % 2 != 0:
        arr[i] = -1

print(arr)






arr[arr % 2 == 1] = -1
arr
#> array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])




####################################################################.


"""
6. How to replace items that satisfy 
    a condition without affecting the original array?
"""

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

out = arr.copy()

out[out % 2 == 1] = -1

print(out)
#[ 0 -1  2 -1  4 -1  6 -1  8 -1]





arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)

print(arr)
#[0 1 2 3 4 5 6 7 8 9]

print(out)
#array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])



####################################################################.


"""
7. How to reshape an array?
"""


x = np.arange(10)
print(x)

print(x.reshape(2,5))
"""
[[0 1 2 3 4]
 [5 6 7 8 9]]
"""




arr = np.arange(10)

arr.reshape(2, -1)  # Setting to -1 automatically decides the number of cols

#array([[0, 1, 2, 3, 4],
#[5, 6, 7, 8, 9]])


####################################################################.

"""
8. How to stack two arrays vertically?
"""

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

print(np.vstack((a,b)))
"""
[[0 1 2 3 4]
 [5 6 7 8 9]
 [1 1 1 1 1]
 [1 1 1 1 1]]
"""




####################################################################.

"""
9. How to stack two arrays horizontally?
"""

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

print(np.hstack((a,b)))

"""
[[0 1 2 3 4 1 1 1 1 1]
 [5 6 7 8 9 1 1 1 1 1]]
"""



####################################################################.

"""
10. How to generate custom sequences in numpy without hardcoding?
"""
a = np.array([1,2,3])

np.repeat(a,3)
np.tile(a,3)

print(np.concatenate([np.repeat(a,3),np.tile(a,3)]))
#[1 1 1 2 2 2 3 3 3 1 2 3 1 2 3 1 2 3]


####################################################################.

"""
11. How to get the common items between two python numpy arrays?
"""

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])


print(np.intersect1d(a,b))
#[2 4]






####################################################################.

"""
12. How to remove from one array those items that exist in another?
"""

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

print(np.setdiff1d(a,b))
#[1 2 3 4]





####################################################################.

"""
13. How to get the positions where elements of two arrays match?
"""

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

np.where(a == b)
# (array([1, 3, 5, 7]),)






####################################################################.

"""
14. How to extract all numbers between a given range from a numpy array?
"""

a = np.array([2, 6, 1, 9, 10, 3, 27])

ab = np.where((5 <= a) & (10 >= a))

print(a[ab])
#[ 6  9 10]





####################################################################.

"""
15. How to make a python function that handles scalars to work on numpy arrays?
"""

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])


def maxx(a, b):

    array_one = np.max(np.concatenate((a,b)))

    return array_one

print(maxx(a, b))
#9



####################################################################.

"""
16. How to swap two columns in a 2d numpy array?
"""
















