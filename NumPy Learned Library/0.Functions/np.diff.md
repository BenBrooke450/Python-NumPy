numpy.diff() in Python

 

numpy.diff(arr[, n[, axis]]) function is used when we calculate the n-th order discrete difference along the given axis. The first order difference is given by out[i] = arr[i+1] – arr[i] along the given axis. If we have to calculate higher differences, we are using diff recursively.

 

Syntax: numpy.diff()

 

Parameters: 

arr : [array_like] Input array. 

n : [int, optional] The number of times values are differenced. 

axis : [int, optional] The axis along which the difference is taken, default is the last axis.

Returns : [ndarray]The n-th discrete difference. The output is the same as a except along axis where the dimension is smaller by n. 




```python
# input array

arr = np.array([1, 3, 4, 7, 9])

print("Input array  : ", arr)

#Input array  :  [1 3 4 7 9]

 

print("First order difference  : ", np.diff(arr))

#First order difference  :  [2 1 3 2]

 

print("Second order difference : ", np.diff(arr, n=2))

#Second order difference :  [-1  2 -1]

 

print("Third order difference  : ", np.diff(arr, n=3))

#Third order difference  :  [ 3 -3]
``
 

 