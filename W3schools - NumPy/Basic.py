






########################################################
#          Page 1: Getting Started
########################################################


import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)
#[1 2 3 4 5]




import numpy as np

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
#[1 2 3 4 5]









########################################################
#          Page 2: NumPy Creating Arrays
########################################################



arr = np.array([1, 2, 3, 4, 5])

print(arr)
#[1 2 3 4 5]

print(type(arr))
#<class 'numpy.ndarray'>




"""
To create an ndarray, we can pass a list,
 tuple or any array-like object into the array() method, 
 and it will be converted into an ndarray:
 
"""

arr = np.array((1, 2, 3, 4, 5))

print(arr)
#[1 2 3 4 5]





"""
0-D Arrays

0-D arrays, or Scalars, are the elements in an array. 
    Each value in an array is a 0-D array.
"""

arr = np.array(42)

print(arr)
#42






"""
1-D Arrays

An array that has 0-D arrays as its elements
 is called uni-dimensional or 1-D array.

These are the most common and basic arrays.
"""

arr = np.array([1, 2, 3, 4, 5])

print(arr)
#[1 2 3 4 5]







"""
2-D Arrays
An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.
"""

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)
"""
[[1 2 3]
 [4 5 6]]
"""








"""
3-D arrays
An array that has 2-D arrays (matrices) as its
 elements is called 3-D array.

These are often used to represent a 3rd order tensor.
"""

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)
"""
[[[1 2 3]
  [4 5 6]]

 [[1 2 3]
  [4 5 6]]]
"""







"""
Check Number of Dimensions?
NumPy Arrays provides the ndim attribute that
 returns an integer that tells us how many
  dimensions the array have.
"""
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
#0

print(b.ndim)
#1

print(c.ndim)
#2

print(d.ndim)
#3










"""
Higher Dimensional Arrays
An array can have any number of dimensions.

When the array is created, you can define the
 number of dimensions by using the ndmin argument.
"""

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)

print('number of dimensions :', arr.ndim)

"""
[[[[[1 2 3 4]]]]]
number of dimensions : 5
"""








########################################################
#          Page 3: NumPy Array Indexing
########################################################


arr = np.array([1, 2, 3, 4])

print(arr[0])
#1

print(arr[1])
#2

print(arr[2] + arr[3])
#7







"""
Access 2-D Arrays
To access elements from 2-D arrays we can use comma
 separated integers representing the dimension and
  the index of the element.

Think of 2-D arrays like a table with rows and
 columns, where the dimension represents the row 
 and the index represents the column.
 
"""

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])
#2nd element on 1st row:  2


print('5th element on 2nd row: ', arr[1, 4])
#5th element on 2nd row:  10


"""

Access 3-D Arrays

To access elements from 3-D arrays we can use comma 
    separated integers representing the dimensions and 
    the index of the element.
    
"""

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])
#6







########################################################
#          Page 3: NumPy Array Slicing
########################################################


arr = np.array([1, 2, 3, 4, 5, 6, 7])


print(arr[4:])
#[5 6 7]


print(arr[:4])
#[1 2 3 4]






"""
Negative Slicing
Use the minus operator to refer to an index from the end:
"""

print(arr[-3:-1])
#[5 6]


print(arr[1:5:2])
#[2 4]


print(arr[::2])
#[1 3 5 7]






"""
Slicing 2-D Arrays
"""

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])
#[7 8 9]


print(arr[0:2, 2])
#[3 8]


print(arr[0:2, 1:4])
"""
[[2 3 4]
 [7 8 9]]
"""




########################################################
#          Page 4: NumPy Data Types
########################################################


"""
Data Types in NumPy
NumPy has some extra data types, and refer
 to data types with one character, like i for integers, 
 u for unsigned integers etc.

Below is a list of all data types in 
    NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

"""


arr = np.array([1, 2, 3, 4])

print(arr.dtype)
#int64



arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)





"""
Creating Arrays With a Defined Data Type

We use the array() function to create arrays, this
 function can take an optional argument: dtype that
  allows us to define the expected data type of the array elements:
  
"""

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)
#[b'1' b'2' b'3' b'4']
#|S1





arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)
#[1 2 3 4]
#int32




"""

Converting Data Type on Existing Arrays

The best way to change the data type of an 
    existing array, is to make a copy of the 
    array with the astype() method.

The astype() function creates a copy of the 
    array, and allows you to specify the 
    data type as a parameter.

The data type can be specified using a string, 
    like 'f' for float, 'i' for integer etc. or 
    you can use the data type directly like float 
    for float and int for integer.

"""


arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
#[1 2 3]

print(newarr.dtype)
#int32








arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
#[1 2 3]

print(newarr.dtype)
#int64







arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
#[ True False  True]

print(newarr.dtype)
#bool





########################################################
#          Page 4: Array Copy vs View
########################################################

"""
The Difference Between Copy and View

The main difference between a copy and a 
    view of an array is that the copy is a new array,
     and the view is just a view of the original array.

The copy owns the data and any changes 
    made to the copy will not affect original array,
     and any changes made to the original array
      will not affect the copy.

The view does not own the data and any
    changes made to the view will affect
     the original array, and any changes
      made to the original array will affect the view.
      
"""


arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()

arr[0] = 42

print(arr)
#[42  2  3  4  5]


print(x)
#[1 2 3 4 5]





arr = np.array([1, 2, 3, 4, 5])

x = arr.view()

arr[0] = 42

print(arr)
#[42  2  3  4  5]

print(x)
#[42  2  3  4  5]




"""
Check if Array Owns its Data
As mentioned above, copies owns the data,
 and views does not own the data, but how can we check this?

Every NumPy array has the attribute base 
    that returns None if the array owns the data.

Otherwise, the base  attribute refers to the original object.

"""


arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
#None

print(y.base)
#[1 2 3 4 5]






########################################################
#          Page 4: NumPy Array Shape
########################################################

"""
Get the Shape of an Array
NumPy arrays have an attribute called shape 
    that returns a tuple with each index having 
    the number of corresponding elements.
"""

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)
#(2, 4)




arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
#[[[[[1 2 3 4]]]]]

print('shape of array :', arr.shape)
#shape of array : (1, 1, 1, 1, 4)






########################################################
#          Page 5: NumPy Array Reshaping
########################################################

"""
Reshaping arrays

Reshaping means changing the shape of an array.

The shape of an array is the number 
    of elements in each dimension.

By reshaping we can add or remove 
    dimensions or change number of elements in each dimension.

"""


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
"""
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
"""



arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)
"""
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]

"""


"""
Can We Reshape Into any Shape?
Yes, as long as the elements required for
 reshaping are equal in both shapes.

We can reshape an 8 elements 1D array 
    into 4 elements in 2 rows 2D array but 
    we cannot reshape it into a 3 elements 3
     rows 2D array as that would require 3x3 = 9 elements.
"""





#Returns Copy or View?

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])


print(arr.reshape(2, 4).base)
#[1 2 3 4 5 6 7 8]

print(arr.reshape(2, 4))
"""
[[1 2 3 4]
 [5 6 7 8]]
"""








"""
Unknown Dimension

You are allowed to have one "unknown" dimension.

Meaning that you do not have to specify an exact 
    number for one of the dimensions in the reshape method.

Pass -1 as the value, and NumPy will calculate this number for you.
"""


newarr = arr.reshape(2, 2, -1)

print(newarr)
"""
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
"""



"""
Flattening the arrays

Flattening array means converting a multidimensional
    array into a 1D array.

We can use reshape(-1) to do this.
"""

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)
#[1 2 3 4 5 6]




"""
Note: There are a lot of functions for 
    changing the shapes of arrays in numpy flatten,
     ravel and also for rearranging the elements 
     rot90, flip, fliplr, flipud etc. These fall 
     under Intermediate to Advanced section of numpy.

"""


########################################################
#          Page 6: NumPy Array Iterating
########################################################


"""
Iterating means going through elements one by one.

As we deal with multi-dimensional arrays in numpy, 
    we can do this using basic for loop of python.

If we iterate on a 1-D array it will go through 
    each element one by one.

"""

arr = np.array([1, 2, 3])

for x in arr:
  print(x)

"""
1
2
3
"""





arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

"""
[1 2 3]
[4 5 6]
"""






arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)

"""
1
2
3
4
5
6
"""


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

"""
[[1 2 3]
 [4 5 6]]
 
[[ 7  8  9]
 [10 11 12]]
"""





arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)

"""
1
2
3
4
5
6
7
8
9
10
11
12
"""


"""
Iterating Arrays Using nditer()

The function nditer() is a helping function 
    that can be used from very basic to very 
    advanced iterations. It solves some basic 
    issues which we face in iteration, lets go 
    through it with examples.

Iterating on Each Scalar Element

In basic for loops, iterating through each scalar 
    of an array we need to use n for loops which can 
    be difficult to write for arrays with very high dimensionality.
    
"""

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

"""
1
2
3
4
5
6
7
8
"""









"""
Iterating Array With Different Data Types

We can use op_dtypes argument and pass it the expected datatype 
    to change the datatype of elements while iterating.

NumPy does not change the data type of the element in-place
    (where the element is in array) so it needs some other 
    space to perform this action, that extra space is called 
    buffer, and in order to enable it in nditer() we pass 
    flags=['buffered'].
    
"""

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

"""
b'1'
b'2'
b'3'
"""




#Iterating With Different Step Size

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

"""
1
3
5
7
"""







"""
Enumerated Iteration Using ndenumerate()

Enumeration means mentioning sequence number of 
    somethings one by one.

Sometimes we require corresponding index of the 
    element while iterating, the ndenumerate() method 
    can be used for those usecases.
"""

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

"""
(0,) 1
(1,) 2
(2,) 3
"""




arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

"""
(0, 0) 1
(0, 1) 2
(0, 2) 3
(0, 3) 4
(1, 0) 5
(1, 1) 6
(1, 2) 7
(1, 3) 8
"""







########################################################
#          Page 7: NumPy Joining Array
########################################################


"""
Joining NumPy Arrays

Joining means putting contents of two or 
    more arrays in a single array.

In SQL we join tables based on a key, 
    whereas in NumPy we join arrays by axes.

We pass a sequence of arrays that we want 
    to join to the concatenate() function, 
    along with the axis. If axis is not explicitly 
    passed, it is taken as 0.


"""


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)
#[1 2 3 4 5 6]







arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
"""
[[1 2 5 6]
 [3 4 7 8]]
"""







arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=0)

print(arr)
"""
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
"""



"""
Joining Arrays Using Stack Functions

Stacking is same as concatenation, the only 
    difference is that stacking is done along a new axis.

We can concatenate two 1-D arrays along the 
    second axis which would result in putting 
    them one over the other, ie. stacking.

We pass a sequence of arrays that we want 
    to join to the stack() method along with 
    the axis. If axis is not explicitly passed it is taken as 0.
    
"""

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)
"""
[[1 4]
 [2 5]
 [3 6]]
"""



"""
Stacking Along Rows

NumPy provides a helper function: hstack() to stack along rows.
"""
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)
#[1 2 3 4 5 6]






"""
Stacking Along Columns
NumPy provides a helper function: vstack()  to stack along columns.
"""


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)
"""
[[1 2 3]
 [4 5 6]]
"""






########################################################
#          Page 7: NumPy Splitting Array
########################################################

"""
Splitting NumPy Arrays

Splitting is reverse operation of Joining.

Joining merges multiple arrays into one and Splitting
 breaks one array into multiple.

We use array_split() for splitting arrays, we pass
 it the array we want to split and the number of splits.

"""



arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
#[array([1, 2]), array([3, 4]), array([5, 6])]

for sub_arr in newarr:
    print(sub_arr.tolist())

"""
[1, 2]
[3, 4]
[5, 6]
"""




"""
If the array has less elements than required, 
    it will adjust from the end accordingly.
"""

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)


print(newarr)
#[array([1, 2]), array([3, 4]), array([5]), array([6])]




"""
Split Into Arrays

The return value of the array_split() method 
    is an array containing each of the split as an array.

If you split an array into 3 arrays, you can 
    access them from the result just like any array element:
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
#[1 2]

print(newarr[1])
#[3 4]

print(newarr[2])
#[5 6]








"""
Splitting 2-D Arrays

Use the same syntax when splitting 2-D arrays.

Use the array_split() method, pass in the array you 
    want to split and the number of splits you want to do.
    
"""


arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)
"""
[array([[1, 2],
       [3, 4]]), array([[5, 6],
       [7, 8]]), array([[ 9, 10],
       [11, 12]])]
"""

print([x.tolist() for x in newarr])
#[[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]





arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)

"""
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]
"""


"""
Note: Similar alternates to vstack() and dstack() 
    are available as vsplit() and dsplit().
"""







########################################################
#          Page 8: NumPy Searching Arrays
########################################################


"""
Searching Arrays

You can search an array for a certain value, 
    and return the indexes that get a match.

To search an array, use the where() method.
"""


arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)
#(array([3, 5, 6]),)

"""
The example above will return a tuple: (array([3, 5, 6],)

Which means that the value 4 is present at index 3, 5, and 6.
"""







arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)
#(array([1, 3, 5, 7]),)






"""
Search Sorted

There is a method called searchsorted() which 
    performs a binary search in the array, and 
    returns the index where the specified value
     would be inserted to maintain the search order.
"""

#The searchsorted() method is assumed to be used on sorted arrays.

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)
#1






"""
Search From the Right Side

By default the left most index is returned, 
    but we can give side='right' to return the 
    right most index instead.
"""


arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)
#2







"""
Multiple Values

To search for more than one value, 
    use an array with the specified values.
"""

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)
#[1 2 3]


"""
The return value is an array: [1 2 3] 
    containing the three indexes where 2, 4, 6 would 
    be inserted in the original array to maintain the order.

"""



########################################################
#          Page 9: NumPy Sorting Arrays
########################################################


"""
Sorting Arrays

Sorting means putting elements in an ordered sequence.

Ordered sequence is any sequence that has an order 
    corresponding to elements, like numeric or alphabetical,
     ascending or descending.

The NumPy ndarray object has a function called sort(), that
    will sort a specified array.
    
"""


arr = np.array([3, 2, 0, 1])

"""
Note: This method returns a copy of the array, leaving the 
    original array unchanged.

"""

print(np.sort(arr))
#[0 1 2 3]



"""
Sorting a 2-D Array

If you use the sort() method on a 2-D array, 
    both arrays will be sorted:
"""

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))
"""
[[2 3 4]
 [0 1 5]]
"""



########################################################
#          Page 10: NumPy Filter Array
########################################################

"""
Filtering Arrays

Getting some elements out of an existing array and
    creating a new array out of them is called filtering.

In NumPy, you filter an array using a boolean index list.

A boolean index list is a list of booleans
    corresponding to indexes in the array.

If the value at an index is True that element 
    is contained in the filtered array, if the
    value at that index is False that element is
    excluded from the filtered array.
"""


arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)
#[41 43]

"""
The example above will return [41, 43], why?

Because the new array contains only the values 
    where the filter array had the value True, in 
    this case, index 0 and 2.
"""




"""
Creating the Filter Array

In the example above we hard-coded the True and False values,
    but the common use is to create a filter array based on
     conditions.
"""


arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
#[False, False, True, True]

print(newarr)
#[43 44]




"""
Creating Filter Directly From Array

The above example is quite a common task in NumPy and
    NumPy provides a nice way to tackle it.

We can directly substitute the array instead of
    the iterable variable in our condition and it
     will work just as we expect it to.

"""


arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
#[False False  True  True]


print(newarr)
#[43 44]




