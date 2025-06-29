
Numpy | Iterating Over Array


NumPy package contains an iterator object numpy.nditer. It is an efficient multidimensional iterator object using which it is possible to iterate over an array. Each element of an array is visited using Python’s standard Iterator interface.

 

 
```python
# creating an array using arrange

# method

a = np.arange(12)

# shape array with 3 rows and

# 4 columns

a = a.reshape(3, 4)

print('Original array is:')

print(a)

"""

Original array is:

[[ 0  1  2  3]

 [ 4  5  6  7]

 [ 8  9 10 11]]

 """

 

 

 

# Transpose of original array

b = a.T

 

 

print('Modified array is:')

for x in np.nditer(b):

    print(x)

 

"""

Modified array is:

0

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

"""
```